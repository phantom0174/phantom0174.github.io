"""
重新排序以亂序描述的腳註
"""

from io import TextIOWrapper
from .file_traverser import Response
from .STL import STL

import re


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
    ini_ecln = ecln[0]
    end_ecln = ecln[-1]

    repos_core = content[ini_ecln:end_ecln + 1]

    for (i, line) in enumerate(repos_core):
        FT = get_end_content_FT(line)
        new_footnote_num = do.index(get_footnote_num(FT)) + 1
        repos_core[i].replace(FT, f"{create_footnote_str(new_footnote_num)}")

    repos_core = list(sorted(repos_core, key=lambda x: get_footnote_num(get_end_content_FT(x))))

    content = content[:ini_ecln] + repos_core + content[end_ecln + 1:]
    return content


def workflow(file_path: str, file: TextIOWrapper, responser: Response):
    content = file.read().split("\n")

    disturbed_order: list[int] = [] # the order of footnote appearance in the content
    end_content_appearance: list[int] = []
    end_content_line_num: list[int] = []

    abort = False

    footnote_counter = 1
    for (index, line) in enumerate(content):
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
                content[index].replace(match, create_footnote_str(footnote_counter))
                footnote_counter += 1
    
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
