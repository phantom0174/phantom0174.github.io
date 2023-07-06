from .color import Colors


LEVEL_MSG_PREFIX = {
    "s": f"{Colors.OKBLUE}==== Success ====",
    "i": f"{Colors.INFO}==== Infos ====",
    "e": f"{Colors.FAIL}==== Errors ===="
}


class Response:
    """
    pool: {
        "s/i/e": { -> level
            "status": [
                { -> responses
                    path: file_path,
                    msg: message
                },
            ],
        },
    }
    """

    pool = {"s": {}, "i": {}, "e": {}}

    def clear(self):
        self.pool = {"s": {}, "i": {}, "e": {}}

    def add(self, result: str, payload: dict) -> None:
        """
        result:
            - type: str
            - format: "<pool type(s/i/e)>/status" (s: success, i: info, e: error)
        
        payload: {
            path: ...,
            msg: ...
        }
        """

        result_info = result.split("/")

        if len(result_info) > 2:
            raise Exception(
                f"Result added has a invalid length!\nresult: {result}"
            )
        
        level = result_info[0]
        status = result_info[1]

        if status not in self.pool[level]:
            self.pool[level][status] = []

        self.pool[level][status].append(payload)

    def __indent_lines(self, content: str) -> str:
        """
        transforming:
        a
        b
        into:
            a
            b
        """

        indented = list(map(lambda line: "    " + line, content.split("\n")))
        indented = "\n".join(indented)
        return indented

    def __level_output(self, lvl: str, responses: list) -> None:
        """
        By default, the message of successful responses won't be outputted.
        """

        if lvl == "s":
            responses = list(map(lambda r: r["path"], responses))

            if len(responses) > 5:
                result = '\n'.join(responses[:5]) + f"\nand {len(responses) - 5} other files...\n"
            else:
                result = '\n'.join(responses) + '\n'

            print(result)
        
        elif lvl in ["i", "e"]:
            for resp in responses:
                indented_lines = self.__indent_lines(resp['msg'])
                print(f"{resp['path']} ->\n{indented_lines}\n")

    def output_result(self) -> None:
        for (level, level_statuses) in self.pool.items():

            if not level_statuses:
                continue

            print(LEVEL_MSG_PREFIX[level])

            for (status, responses) in level_statuses.items():
                print(f"< {status} >")
                
                try:
                    self.__level_output(level, responses)
                except:
                    # setting the color back to white when outputting errors
                    print(Colors.ENDC)
                    raise

            print(Colors.ENDC)

