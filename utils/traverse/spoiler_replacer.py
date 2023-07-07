from io import TextIOWrapper
from .file_traverser import Response

from .STL import STL

SKIP_ALL_SYNTAX = "<!--sprp:skip-all-->"

stl = STL({
    # success
    "0": "No need of replacement",
    "1": "Replacement successful",
    
    # info
    "2": "Syntax count parity" # if the count of spoiler syntax is odd
})

replace_state_output = {
    "0": "{% spoiler ",
    "1": " %}"
}


def replace_syntax(s: str) -> str:
    state = 0
    ind = 0
    while ind < len(s):
        if not (s[ind] == '|' and ind + 1 < len(s) and s[ind + 1] == '|'):
            ind += 1
            continue
        
        s = s[:ind] + replace_state_output[str(state)] + s[ind + 2:]
        state = (state + 1) % 2
        ind += 3
    
    return s


def workflow(file_path: str, file: TextIOWrapper, responser: Response):
    content = file.read().split("\n")

    has_replaced = False
    odd_count_lines_num : list[str] = []
    for (line_num, line) in enumerate(content):
        if line.startswith(SKIP_ALL_SYNTAX):
            return responser.add(f"s/{stl.get(0)}", {
                "path": file_path
            })
        
        if line.startswith("<!--"):
            continue
        
        if "||" not in line:
            continue
        
        if line.count("||") % 2 != 0:
            odd_count_lines_num.append(str(line_num + 1))
            continue

        has_replaced = True
        content[line_num] = replace_syntax(line)
    
    if odd_count_lines_num:
        responser.add(f"i/{stl.get(2)}", {
            "path": file_path,
            "msg": f"File has a odd number of spoiler syntax on line {', '.join(odd_count_lines_num)},\n" \
                 + f"consider using <!--sprp:skip-all--> ?"
        })

    if has_replaced:
        file.seek(0)
        file.write("\n".join(content))
        file.truncate()

        responser.add(f"s/{stl.get(1)}", {
            "path": file_path
        })
    else:
        responser.add(f"s/{stl.get(0)}", {
            "path": file_path
        })
