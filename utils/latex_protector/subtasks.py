"""
Status Code

- Success

0: continue / protection success
1: no need of protection


- Error

3: skip_syntax_error
4: syntax maximum error
5: unclosed syntax error
6: non consecutive syntax error
"""

from .color import Colors
from .settings import (
    skip_all_syntax,
    skip_some_syntax,
    tag_i,
    tag_e
)


def eigenize(contents: list[str]) -> dict:
    """
    The first step of protection.

    Count the number of eigenstring ($$) in each line,
    and return a dict (payload) in form of <eigenstring-count, line-number>.

    Syntax <skip_some_syntax> is encoded as -1.

    Will return a status of 1 if contents include <skip_all_syntax>.

    Param
    -----
    contents: 
        The contents to be eigenized.

    Return
    ------
    Under normal circumstances:
        {
            status: 0,
            payload: the eigenized contents
        }

    If contents include <skip_all_syntax>:
        {
            status: 1
            payload: []
        }
    """

    eigen_info: list[list] = []

    for (i, line) in enumerate(contents):
        if line.startswith(skip_some_syntax):
            eigen_info.append([-1, i])
        elif line.startswith(skip_all_syntax):
            return {
                "status": 1,
                "payload": []
            }
        else:
            count = line.count("$$")
            if count > 0:
                eigen_info.append([count, i])
    
    return {
        "status": 0,
        "payload": eigen_info
    }


def ignore_eigeninfo(eigen_info: list[list]) -> dict:
    """
    The second step of protection.

    Remove any eigen-info pair between two <skip_some_syntax> 
    in the eigen-info from the previous step, and return a refined dict of it.

    Param
    -----
    eigen_info: 
        The eigeninfo to be refined.

    Return
    ------

    Under normal circumstances:
        {
            status: 0,
            payload: refined eigen-info
        }

    If the number of <skip_some_syntax> is odd, in other words,
    there is one or more section(s) in the contents where it is not
    enclosed by two <skip_some_syntax>.
        {
            status: 3,
            msg: the error message
        } 

    """
    remove_pos = []
    skip_syntax_count = 0
    
    cur_pos = 0
    ignore = False
    while (cur_pos < len(eigen_info)):
        num = eigen_info[cur_pos][0]

        if num == -1:
            skip_syntax_count += 1
            ignore = not ignore
            
            if not ignore:
                remove_pos.insert(0, cur_pos)

        if ignore:
            remove_pos.insert(0, cur_pos)

        cur_pos += 1

    if skip_syntax_count % 2 != 0:
        return {
            "status": 3,
            "msg": f"Number of skip-some syntax should be even, In-file count: {skip_syntax_count}"
        }

    for pos in remove_pos:
        del eigen_info[pos]

    return {
        "status": 0,
        "payload": eigen_info
    }


def check_eigen_info(eigen_info: list[list]) -> dict:
    """
    The third step of protection.

    Check various syntax error that could occurred in the contents:
    
    1. Number of eigenstring is greater than 2 on the same line.
    
    2. Number of eigenstring is odd in the contents.
        In other words, there exists one or more section(s) in the contents
        where it is not enclosed by two eigenstring ($$).

    Param
    -----
    eigen_info:
        The eigeninfo to be checked.

    Return
    ------

    Under normal circumstances:
        {
            status: 0
        }

    When the number of eigenstring is greater than 2 on the same line:
        {
            status: 4,
            msg: the error message
        }

    When the number of eigenstring is not even in the contents:
        {
            status: 5,
            msg: the error message
        }
    """

    eigenstring_count = 0
    for info in eigen_info:
        num = info[0]

        if num > 2:
            return {
                "status": 4,
                "msg": f"Number of $$ should not be greater than 2 on the same line\n"
                       f"Number: {num} | On line: {info[1] + 1}"
            }
        
        eigenstring_count += num
    
    if eigenstring_count % 2 != 0:
        return {
            "status": 5,
            "msg": f"Number of $$ should be even, In-file count: {eigenstring_count}"
        }
    
    return {
        "status": 0
    }


def check_eigen_block(eigen_info: list[list]) -> dict:
    """
    The fourth step of protection.

    Check whether there is a obstacle (such as a line with two eigenstring) 
    blocking between an eigenstring pair. (Composed by an opening $$ and a closing $$).

    Param
    -----
    eigen_info:
        The eigeninfo to be checked.

    Return
    ------

    Under normal circumstances:
        {
            status: 0
        }

    When the eigenstring pair is blocked:
        {
            status: 6,
            msg: the error message
        }
    """

    cur_pos = 0
    while (cur_pos < len(eigen_info) - 1):
        if eigen_info[cur_pos][0] == 1:
            if eigen_info[cur_pos + 1][0] != 1:
                cur_line = eigen_info[cur_pos][1]
                succ_line = eigen_info[cur_pos + 1][1]

                return {
                    "status": 6,
                    "msg": f"$$...$$ on different lines should not be blocked by a line with two $$\n"
                           f"Line: {cur_line + 1} is blocked by line: {succ_line + 1}"
                }
            
            cur_pos += 1
        
        cur_pos += 1

    return {
        "status": 0
    }


def get_insertion_cmd(contents: list[str], eigen_info: list[list]) -> list[list]:
    """
    The final step of protection.
    
    Pack the insertion, of a <p> after every opening eigenstring, 
    and after every closing eigenstring, as a list of insertion commands.

    Param
    -----
    contents:
        The original contents

    eigen_info:
        The eigeninfo from the previous steps.

    Return
    ------
    {
        status: 0,
        payload: the insertion commands
    }

    """

    insert_cmds: list[list] = []

    cur_pos = 0
    while (cur_pos < len(eigen_info)):
        num = eigen_info[cur_pos][0]
        
        cur_line = eigen_info[cur_pos][1]
        succ_line = cur_line
        if num == 1:
            succ_line = eigen_info[cur_pos + 1][1]        

        if not contents[cur_line - 1].startswith(tag_i):
            insert_cmds.insert(0, [cur_line, tag_i])
        if succ_line + 1 >= len(contents) or not contents[succ_line + 1].startswith(tag_e):
            insert_cmds.insert(0, [succ_line + 1, tag_e])

        if num == 1:
            cur_pos += 1
        cur_pos += 1
    
    return {
        "status": 0,
        "payload": insert_cmds
    }


def output_result(SUCCESS, ERROR) -> dict:
    for item in SUCCESS.items():
        k = item[0]
        files = item[1]

        if len(files) == 0:
            continue

        if k == "0":
            print(f"{Colors.OKGREEN}Protect Successful:{Colors.ENDC}")
        elif k == "1":
            print(f"{Colors.OKCYAN}No Need of Protection:{Colors.ENDC}")
        
        result = ""
        if len(files) > 5:
            result = '\n'.join(files[:5]) + f"\nand {len(files) - 5} other files...\n"
        else:
            result = '\n'.join(files) + '\n'

        print(result)

    for item in ERROR.items():
        vs = item[1]

        for v in vs:
            print(f"{Colors.FAIL}{v[0]} |:{Colors.ENDC}\n{v[1]}\n")
