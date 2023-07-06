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
    "3": "Invalid use of | syntax"
})

syntax = "_!"
prefix = "{% hint"
suffix = "%}"


def replace_unit(s: str) -> str:
    # <text>|<hint-line1\nhint-line2\n...>
    
    s = s.split("|")

    if len(s) != 2:
        raise Exception(stl.get(3))

    text = s[0]
    hints = s[1].split("\\n")
    
    hints = list(map(lambda s: f"\'{s}\'", hints))
    hints = ' '.join(hints)
    
    return f"{prefix} \'{text}\' {hints} {suffix}"


def replace_syntax_in_line(line: str) -> str:
    line = line.split(syntax)
        
    new_line = []
    for (ind, s) in enumerate(line):
        # content -> even; hidden -> odd
        if ind % 2 == 0:
            new_line.append(s)
        else:
            replace_syntax = replace_unit(s)
            new_line.append(replace_syntax)
    
    return ''.join(new_line)


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
                raise Exception(stl.get(2))
            
            has_syntax = True
            content[line_num] = replace_syntax_in_line(line)
        except Exception as e:
            if str(e) not in exception_pool:
                exception_pool[str(e)] = []

            exception_pool[str(e)].append(str(line_num + 1))

    if has_syntax:
        file.seek(0)
        file.write("\n".join(content))
        file.truncate()

        responser.add(f"s/{stl.get(1)}", {
            "path": file_path
        })

    if exception_pool:
        if stl.get(2) in exception_pool:
            responser.add(f"e/{stl.get(2)}", {
                "path": file_path,
                "msg": f"File has a odd number of hint syntax on line {', '.join(exception_pool[stl.get(2)])}"
            })
        
        if stl.get(3) in exception_pool:
            responser.add(f"e/{stl.get(3)}", {
                "path": file_path,
                "msg": f"On line {', '.join(exception_pool[stl.get(3)])}"
            })
        return
    
    responser.add(f"s/{stl.get(0)}", {
        "path": file_path
    })
