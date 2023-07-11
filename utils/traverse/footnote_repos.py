"""

重新排序文章中呈現亂序的腳註。

縮寫：
    FT: footnote 腳註

名詞定義：
    inline FT (inline-FT): 出現在文章中的腳註，一行可出現多個。
    isolated FT (iso-FT): 出現在文章末的腳註，一行只可出現一個，作為連接 inline FT 的部分。

"""

from io import TextIOWrapper
from .file_traverser import Response
from .STL import STL

import re

SKIP_ALL_SYNTAX = "<!--ft:skip-all-->"

stl = STL({
    # success
    "0": "No need of repositioning",
    "1": "Reposition successful",
    
    # error
    "2": "End-content footnote error", # multiple occurrence of iso-FT in one line
    "3": "Footnote in-bijection error" # bijection does not relate between inline-FTs and iso-FTs
})

isolated = r"\[\^[0-9]+\]\:"
inline = r"\[\^[0-9]+\]"

# utils func

def get_ft_num(s: str) -> int:
    return int(s[2:-1])


def create_ft_str(num: int) -> str:
    return f"[^{num}]"


def is_list_equal(a: list, b: list) -> bool:
    A = set(a)
    B = set(b)

    return (A == B)


def extract_iso_ft(line: str) -> str:
    FT = re.search(isolated, line)
    if FT:
        FT = FT.group()
    if not FT:
        FT = ""

    return FT[:-1]


def repositioning(content: list[str], inline_order: list[int], iso_order_index: list[int]) -> list[str]:
    """
    
    整個 reposition 的過程如下：

    假如
        inline order = [1 3 5 2 4]
        iso order = [1 2 3 4 5]

    而在調用此函數之前，inline FTs 在 content 中應該已經變成 [1 2 3 4 5] 的順序
    所以還需要做的，就是將 iso order 中的東西依照其在 inline order 中出現的位置進行排序。

    所以，iso order 應該要變成 [1 3 5 2 4]，同 inline order。

    然而在實際過程中，需要直接對 content 進行操作（其包含 iso order 的資訊）
    首先，將 content 中的 iso-FTs 區段取出變成 repos_core， (re-position core)
    再將 repos_core 每行的開頭轉換成其在 inline order 中出現的位置，
    再進行自動排序即可將行數移動到正確的位置。

    此過程經過測試，可處裡亂序輸入。

    extract_iso_ft 為得出開頭處的 iso-FT（不包含 ":"）
    get_ft_num 可以再將得到的東西進行轉換，得到正確的 FT 編號
    
    """
    
    ini_core = iso_order_index[0]
    end_core = iso_order_index[-1]

    repos_core = content[ini_core:end_core + 1]
    repos_core = list(filter(lambda x: x.strip(), repos_core)) # remove empty lines

    for (i, line) in enumerate(repos_core):
        ft = extract_iso_ft(line)
        new_footnote_num = inline_order.index(get_ft_num(ft)) + 1
        repos_core[i] = repos_core[i].replace(ft, f"{create_ft_str(new_footnote_num)}")

    repos_core = list(sorted(repos_core, key=lambda x: get_ft_num(extract_iso_ft(x))))

    content = content[:ini_core] + repos_core + content[end_core + 1:]
    return content

# main workflow

temp_syntax = "(^TEMP)"

def workflow(file_path: str, file: TextIOWrapper, responser: Response):
    content: list[str] = file.read().split("\n")

    inline_order: list[int] = [] # the order of inline-FT appearance in the post
    iso_order: list[int] = [] # the order of isolated-FT appearance in the post
    iso_order_index: list[int] = [] # the line-index of the FTs in iso_order

    abort = False

    footnote_counter = 1
    for (index, line) in enumerate(content):
        if line.startswith(SKIP_ALL_SYNTAX):
            return responser.add(f"s/{stl.get(0)}", {
                "path": file_path
            })
        
        if line.startswith("<!--"):
            continue

        if results := re.findall(isolated, line): # dealing with iso-FT
            if len(results) != 1:
                responser.add(f"e/{stl.get(2)}", {
                    "path": file_path,
                    "msg": f"Pattern of \'[^X]:\' occurred more than once at line {index + 1}"
                })
                abort = True
                continue
            
            iso_order.append(get_ft_num(results[0][:-1]))
            iso_order_index.append(index)
        elif results := re.findall(inline, line): # dealing with inline-FT
            for match in results:
                inline_order.append(get_ft_num(match))
                temp_replace = create_ft_str(footnote_counter)
                content[index] = content[index].replace( # replacing inline-FT with temp-FTs
                    match,
                    f"{temp_replace[0]}{temp_syntax}{temp_replace[1:]}"
                )
                footnote_counter += 1

            # transforming the temp-FTs back to inline-FTs
            content[index] = "".join(content[index].split(temp_syntax))
    
    # does not have any FTs
    if not inline_order:
        return responser.add(f"s/{stl.get(0)}", {
            "path": file_path
        })

    if abort:
        return

    # testing for bijection
    if not is_list_equal(inline_order, iso_order):
        return responser.add(f"e/{stl.get(3)}", {
            "path": file_path,
            "msg": f"Order of inline-FTs is {inline_order.sort()}\n" + \
                    f"While order of iso-FTs is {iso_order.sort()}"
        })
    
    is_inline_ordered = True
    for (ind, num) in enumerate(inline_order):
        if num != ind + 1:
            is_inline_ordered = False

    same_order = True
    for (ft_num1, ft_num2) in zip(inline_order, iso_order):
        if ft_num1 != ft_num2:
            same_order = False

    if is_inline_ordered and same_order:
        return responser.add(f"s/{stl.get(0)}", {
            "path": file_path
        })

    # repositioning and renaming of end-content footnotes
    content = repositioning(content, inline_order, iso_order_index)

    file.seek(0)
    file.write("\n".join(content))
    file.truncate()

    responser.add(f"s/{stl.get(1)}", {
        "path": file_path
    })
