"""

融進 async-traverser 之後的版本，初代版本請見：
https://phantom0174.github.io/2023/01/lightweight-hexo-latex-rendering/
https://phantom0174.github.io/2023/01/latex-protector/

"""

from io import TextIOWrapper
from .async_traverser import Response

from .latex_protector.subtasks import *
from .latex_protector.subtasks import status_code_translator as sct


def workflow(file_path: str, file: TextIOWrapper, responser: Response):
    contents = file.read().split("\n")

    # ---
    response = eigenize(contents)
    if response["status"] == 1:
        return responser.add(f"s/{sct['1']}", {
            "path": file_path
        })

    response = ignore_eigeninfo(response["payload"])
    if response["status"] > 2:
        return responser.add(f"e/{sct[str(response['status'])]}", {
            "path": file_path,
            "msg": response["msg"]
        })
    
    eigen_info = response["payload"]

    response = check_eigen_info(eigen_info)
    if response["status"] > 2:
        return responser.add(f"e/{sct[str(response['status'])]}", {
            "path": file_path,
            "msg": response["msg"]
        })
    
    response = check_eigen_block(eigen_info)
    if response["status"] > 2:
        return responser.add(f"e/{sct[str(response['status'])]}", {
            "path": file_path,
            "msg": response["msg"]
        })
    
    response = get_insertion_cmd(contents, eigen_info)
    if len(response["payload"]) == 0:
        return responser.add(f"s/{sct['1']}", {
            "path": file_path
        })

    for cmd in response["payload"]:
        contents.insert(cmd[0], cmd[1])
    
    file.seek(0)
    file.write('\n'.join(contents))
    file.truncate()
    # ---

    return responser.add(f"s/{sct['0']}", {
        "path": file_path
    })
