import asyncio

from file_traverser import Traverser

import emsp_replacer, lp


traversers = [
    Traverser(
        name="EMSP Replacer",
        workflow_func=emsp_replacer.workflow,
        target_folder_root=[
            "./source/_posts/",
            "./source/about/"
        ]
    ),
    Traverser(
        name="Latex Protector",
        workflow_func=lp.workflow,
        target_folder_root=[
            "./source/_posts/",
            "./source/about/"
        ]
    )
]

async def main():
    for traverser in traversers:
        await traverser.run()

if __name__ == "__main__":
    asyncio.run(main())
