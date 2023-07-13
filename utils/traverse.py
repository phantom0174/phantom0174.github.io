import asyncio

from traverse import (
    Traverser, emsp_replacer, lp, spoiler_replacer, footnote_repos
)

traversers = [
    Traverser(
        name="EMSP Replacer",
        workflow_func=emsp_replacer.workflow,
        target_folder_root=[
            "./source/_posts/",
        ]
    ),
    Traverser(
        name="Latex Protector",
        workflow_func=lp.workflow,
        target_folder_root=[
            "./source/_posts/",
            "./source/about/"
        ]
    ),
    Traverser(
        name="Spoiler Replacer",
        workflow_func=spoiler_replacer.workflow,
        target_folder_root=[
            "./source/_posts/",
        ]
    ),
    Traverser(
        name="Footnote Reposer",
        workflow_func=footnote_repos.workflow,
        target_folder_root=[
            "./source/_posts/",
        ]
    )
]

async def main():
    for traverser in traversers:
        await traverser.run()

if __name__ == "__main__":
    asyncio.run(main())
