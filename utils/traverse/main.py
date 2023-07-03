import asyncio

from traverser import Traverser

from emsp_replacer import replace
from lp import lp

traversers = [
    Traverser(
        name="Custom 1",
        workflow_func=replace,
        target_folder_root=[
            "./source/_posts/",
            "./source/about/"
        ]
    ),
    Traverser(
        name="Latex Protector",
        workflow_func=lp,
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
