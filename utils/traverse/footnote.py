"""
重新排序以亂序描述的腳註
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
    "2": "End-content footnote error",
    "3": "Footnote in-bijection error"
})

isolated = r"^\[\^[0-9]+\]\:"
inline = r"\[\^[0-9]+\]"


def get_footnote_num(s: str) -> int:
    return int(s[2:-1])

def create_footnote_str(num: int) -> str:
    return f"[^{num}]"


def is_list_equal(a: list, b: list) -> bool:
    A = set(a)
    B = set(b)

    return (A == B)


def get_end_content_FT(line: str) -> str:
    FT = re.search(isolated, line)
    if FT:
        FT = FT.group()
    if not FT:
        FT = ""

    return FT[:-1]


def repositioning(content: list[str], do: list[int], eca: list[int], ecln: list[int]) -> list[str]:
    """
    
    整個 reposition 的過程如下：

    假如
        do = [1 3 5 2 4]
        eca = [1 2 3 4 5]

    而在調用此函數之前，do 在 content 中應該已經變成 [1 2 3 4 5] 的順序
    所以還需要做的，就是將 eca 中的東西依照其在 do 中出現的位置加權進行排序

    所以，eca 應該要變成 [1 3 5 2 4]，同 do。

    然而在實際過程中，需要將 content 中的 end-content FTs 取出變成 repos_core，
    再將 repos_core 每行的開頭轉換成其在 do 中出現的位置轉換，
    再進行自動排序即可將行數移動到正確的位置。

    此過程經過測試，可處裡亂序輸入。

    get_end_content_FT 為得出 end-content 開頭處的 FT（不包含 ":"）
    get_footnote_num 可以再將得到的東西進行轉換，得到正確的 FT 編號
    
    """
    ini_ecln = ecln[0]
    end_ecln = ecln[-1]

    repos_core = content[ini_ecln:end_ecln + 1]

    for (i, line) in enumerate(repos_core):
        FT = get_end_content_FT(line)
        new_footnote_num = do.index(get_footnote_num(FT)) + 1
        repos_core[i] = repos_core[i].replace(FT, f"{create_footnote_str(new_footnote_num)}")

    repos_core = list(sorted(repos_core, key=lambda x: get_footnote_num(get_end_content_FT(x))))

    content = content[:ini_ecln] + repos_core + content[end_ecln + 1:]
    return content

temp_syntax = "(^TEMP)"

def workflow(file_path: str, file: TextIOWrapper, responser: Response):
    content: list[str] = file.read().split("\n")

    disturbed_order: list[int] = [] # the order of footnote appearance in the content
    end_content_appearance: list[int] = []
    end_content_line_num: list[int] = []

    abort = False

    footnote_counter = 1
    for (index, line) in enumerate(content):
        if line.startswith(SKIP_ALL_SYNTAX):
            return responser.add(f"s/{stl.get(0)}", {
                "path": file_path
            })
        
        if line.startswith("<!--"):
            continue

        # dealing with end-content footnotes
        results = re.findall(isolated, line)

        if results:
            if len(results) != 1:
                responser.add(f"e/{stl.get(2)}", {
                    "path": file_path,
                    "msg": f"Pattern of \'[^X]:\' occurred more than once at line {index + 1}"
                })
                abort = True
                continue
            
            end_content_appearance.append(get_footnote_num(results[0][:-1]))
            end_content_line_num.append(index)
            continue
        
        # dealing with in-content footnotes
        results = re.findall(inline, line)

        if results:
            for match in results:
                disturbed_order.append(get_footnote_num(match))
                temp_replace = create_footnote_str(footnote_counter)

                content[index] = content[index].replace(match, f"{temp_replace[0]}{temp_syntax}{temp_replace[1:]}")

                footnote_counter += 1

            content[index] = "".join(content[index].split(temp_syntax))
            
    
    # does not have any footnotes
    if not disturbed_order:
        return responser.add(f"s/{stl.get(0)}", {
            "path": file_path
        })

    if abort:
        return

    # testing for bijection
    if not is_list_equal(disturbed_order, end_content_appearance):
        return responser.add(f"e/{stl.get(3)}", {
            "path": file_path,
            "msg": f"In-content has FTs of {disturbed_order.sort()}\n" + \
                    f"While end-content has FTs of {end_content_appearance.sort()}"
        })
    
    is_do_ordered = True
    for (ind, num) in enumerate(disturbed_order):
        if num != ind + 1:
            is_do_ordered = False

    same_order = True
    for (ft_num1, ft_num2) in zip(disturbed_order, end_content_appearance):
        if ft_num1 != ft_num2:
            same_order = False

    if is_do_ordered and same_order:
        return responser.add(f"s/{stl.get(0)}", {
            "path": file_path
        })

    # repositioning and renaming of end-content footnotes
    content = repositioning(
        content=content,
        do=disturbed_order,
        eca=end_content_appearance,
        ecln=end_content_line_num
    )

    file.seek(0)
    file.write("\n".join(content))
    file.truncate()

    responser.add(f"s/{stl.get(1)}", {
        "path": file_path
    })
