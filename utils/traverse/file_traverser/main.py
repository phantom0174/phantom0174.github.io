import os
import asyncio

from .timer import Timer
from .color import Colors
from .response import Response

from typing import Callable
from io import TextIOWrapper


class Traverser:
    name = ""
    async_tasks = []
    resp_handler = Response()
    workflow_function: Callable[[str, TextIOWrapper, Response], None] | None = None
    target_folder_root: list[str] = []

    def __init__(self, name: str, workflow_func, target_folder_root: list) -> None:
        """
        Param
        -----
        name:
            The name of this traverser.

        workflow_func:
            Custom function to handle the parsing process of each file.

        target_folder_root: 
            A list of folders to be protected.
            Each path must ends with '/'.

            ex: [ './source/_posts/', './source/about/' ]
        """
        self.name = name
        self.workflow_function = workflow_func
        self.target_folder_root = target_folder_root
    

    def __traverse_folder(self, root_path: str) -> None:
        for filename in os.listdir(root_path):
            if filename.endswith('.md'):
                self.async_tasks.append(self.__main_process(f'{root_path}{filename}'))
            elif filename.find('.') == -1:
                self.__traverse_folder(f'{root_path}{filename}/')


    async def __main_process(self, file_path) -> None:
        with open(file_path, 'r+', encoding='utf-8') as file:
            if not self.workflow_function:
                raise Exception(f"Workflow function of traverser {self.name} is None!")

            self.workflow_function(file_path, file, self.resp_handler)


    async def __parallel_process(self):
        timer = Timer()

        print(f'{Colors.OKGREEN}[{self.name}] Process started{Colors.ENDC}\n')

        timer.toggle()
        await asyncio.gather(*self.async_tasks)
        time_needed = timer.toggle()
        
        self.resp_handler.output_result()
        
        print(f'{Colors.OKGREEN}[{self.name}] Process completed in {time_needed:.3f}ms{Colors.ENDC}\n')


    async def run(self):
        for entry in self.target_folder_root:
            self.__traverse_folder(f'{entry}')
        
        await self.__parallel_process()
        self.async_tasks.clear()
        self.resp_handler.clear()
