from io import TextIOWrapper
from file_traverser import Response

from STL import STL


SKIP_ALL_SYNTAX = "<!--ht:skip-all-->"

stl = STL({
    # success
    "0": "No need of replacement",
    "1": "Replacement successful",
    
    # error
    "2": "Syntax count parity", # if the count of hint syntax is odd
    "3": "Missing | syntax"
})

syntax = "_!"
prefix = "{% hint"
suffix = "%}"


def replace_unit(s: str) -> str:
    # <text>|<hint-line1\nhint-line2\n...>
    
    s_info = s.split("|")

    if len(s_info) != 2:
        raise Exception("3")

    text = s_info[0]
    hints = s_info[1].split("\\n")
    
    hints = list(map(lambda h: f"\'{h}\'", hints))
    hints = ' '.join(hints)
    
    return f"{prefix} \'{text}\' {hints} {suffix}"


def replace_syntax_in_line(line: str) -> str:
    line_units = line.split(syntax)
    
    for (ind, s) in enumerate(line_units):
        # even -> content, no modification
        # odd -> hint items, replacement

        if ind % 2 != 0:
            line_units[ind] = replace_unit(s)
    
    return ''.join(line_units)


def workflow(file_path: str, file: TextIOWrapper, responser: Response):
    content = file.read().split("\n")

    has_syntax = False
    exception_pool = {}
    for (line_num, line) in enumerate(content):
        try:
            if line.startswith(SKIP_ALL_SYNTAX):
                return responser.add(f"s/{stl.get(0)}", {
                    "path": file_path
                })
            
            if line.startswith("<!--"):
                continue
            
            if syntax not in line:
                continue
            
            if line.count(syntax) % 2 != 0:
                raise Exception("2")
            
            has_syntax = True
            content[line_num] = replace_syntax_in_line(line)
        except Exception as e:
            if str(e) not in exception_pool:
                exception_pool[str(e)] = []

            exception_pool[str(e)].append(str(line_num + 1))

    if exception_pool:
        if '2' in exception_pool:
            responser.add(f"e/{stl.get(2)}", {
                "path": file_path,
                "msg": f"File has a odd number of hint syntax on line {', '.join(exception_pool['2'])}"
            })
        
        if '3' in exception_pool:
            responser.add(f"e/{stl.get(3)}", {
                "path": file_path,
                "msg": f"Usage of syntax should be _!...|..._!\nOn line {', '.join(exception_pool['3'])}"
            })
        
        return
    
    if has_syntax:
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
