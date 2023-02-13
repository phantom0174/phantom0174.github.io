import os
import asyncio

from .timer import Timer
from .color import Colors
from .subtasks import (
    eigenize,
    ignore_eigeninfo,
    check_eigen_info,
    check_eigen_block,
    get_insertion_cmd,
    output_result
)


class Protector:
    async_tasks = []

    success_pool = {
        "0": [],
        "1": []
    }

    error_pool = {
        "3": [],
        "4": [],
        "5": [],
        "6": []
    }

    def __traverse_folder(self, root_path: str) -> None:
        for filename in os.listdir(root_path):
            if filename.endswith('.md'):
                self.async_tasks.append(self.__main_process(f'{root_path}{filename}'))
            elif filename.find('.') == -1:
                self.__traverse_folder(f'{root_path}{filename}/')

    def __init__(self, target_folder_root: list) -> None:
        """
        Param
        -----

        target_folder_root: 
            A list of folders to be protected.
            Each path must ends with '/'.

            ex: [ './source/_posts/', './source/about/' ]
        """
        for entry in target_folder_root:
            self.__traverse_folder(f'{entry}')

    def __throw_into_error_pool(self, file_path: str, response: dict):
        self.error_pool[str(response["status"])].append([
            file_path, response["msg"]
        ])

    def __throw_into_success_pool(self, file_path: str, response: dict):
        self.success_pool[str(response["status"])].append(file_path)

    async def __main_process(self, file_path) -> None:
        with open(file_path, 'r', encoding='utf-8') as file:
            contents = file.read().split('\n')
        
        # ---
        response = eigenize(contents)
        if response["status"] > 2:
            return self.__throw_into_error_pool(file_path, response)

        response = ignore_eigeninfo(response["payload"])
        if response["status"] > 2:
            return self.__throw_into_error_pool(file_path, response)
        
        eigen_info = response["payload"]

        response = check_eigen_info(eigen_info)
        if response["status"] > 2:
            return self.__throw_into_error_pool(file_path, response)
        
        response = check_eigen_block(eigen_info)
        if response["status"] > 2:
            return self.__throw_into_error_pool(file_path, response)
        
        response = get_insertion_cmd(contents, eigen_info)
        if len(response["payload"]) == 0:
            return self.__throw_into_success_pool(file_path, {
                "status": 1
            })

        for cmd in response["payload"]:
            contents.insert(cmd[0], cmd[1])
        # ---


        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(contents))

        return self.__throw_into_success_pool(file_path, {
            "status": 0
        })

    async def __parallel_process(self):
        timer = Timer()

        print(f'{Colors.OKGREEN}[Latex Protector] Start Analyzing...{Colors.ENDC}\n')
    
        timer.toggle()
        await asyncio.gather(*self.async_tasks)
        time_needed = timer.toggle()
        
        output_result(self.success_pool, self.error_pool)
        
        print(f'{Colors.OKGREEN}[Latex Protector] Completed in {time_needed:.3f}ms{Colors.ENDC}\n')

    def protect(self):
        asyncio.run(self.__parallel_process())
