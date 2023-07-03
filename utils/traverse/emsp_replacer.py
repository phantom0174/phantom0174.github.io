from io import TextIOWrapper
from traverser import Response


def replace(file_path: str, file: TextIOWrapper, responser: Response):
    content = file.read().split("\n")

    has_esmp = False
    for (index, lines) in enumerate(content):
        if lines.startswith("　　"):
            has_esmp = True
            content[index] = "&emsp;&emsp;" + content[index][2:]
    
    if has_esmp:
        file.seek(0)
        file.write('\n'.join(content))
        file.truncate()
        
        responser.add("s/EMSP replaced!", {
            "path": file_path
        })
    else:
        responser.add("s/No need to replace EMSP", {
            "path": file_path
        })
