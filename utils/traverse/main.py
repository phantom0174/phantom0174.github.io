import asyncio

from traverser import Traverser

from custom1 import custom1
from lp import lp

traversers = [
    Traverser(
        name="Custom 1",
        workflow_func=custom1,
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
        # print(traverser.workflow_function)

if __name__ == "__main__":
    asyncio.run(main())