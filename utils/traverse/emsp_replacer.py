"""

寫中文文章時用來把前面兩個全形空格換成 html 專用的語法

"""

from io import TextIOWrapper
from .async_traverser import Response


def workflow(file_path: str, file: TextIOWrapper, responser: Response):
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
