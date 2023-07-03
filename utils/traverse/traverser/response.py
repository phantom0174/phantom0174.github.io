from .color import Colors

"""
pool: {
    "error/success": {
        "status_code": [
            {
                path: file_path,
                msg: message
            },
        ],
    },
}
"""

class Response:
    pool = {"s": {}, "e": {}}

    def __init__(self) -> None:
        None
    
    def clear(self):
        self.pool = {"s": {}, "e": {}}

    def add(self, result: str, payload: dict):
        """
        result:
            - type: str
            - format: "<pool type(e/s)>/status_code"
        
        payload: {
            path: ...,
            msg: ...
        }
        """

        result = result.split("/")

        if len(result) > 2:
            raise Exception(
                f"Result added has a invalid length!\nresult: {result}"
            )
        
        pool_type = result[0]
        status_code = result[1]

        if status_code not in self.pool[pool_type]:
            self.pool[pool_type][status_code] = []

        self.pool[pool_type][status_code].append(payload)


    def output_result(self):
        zone_msg = None
        
        for item in self.pool.items():
            type: str = item[0]
            type_info: dict = item[1]

            if not type_info:
                continue

            if type == "s":
                zone_msg = f"{Colors.OKBLUE}---- Success ----"
            elif type == "e":
                zone_msg = f"{Colors.FAIL}---- Errors ----"

            print(zone_msg)

            for status in type_info.items():
                status_code: str = status[0]
                status_resp: list = status[1]

                print(f"[ {status_code} ]")

                if type == "s":
                    status_resp = list(map(lambda r: r["path"], status_resp))

                    if len(status_resp) > 5:
                        result = '\n'.join(status_resp[:5]) + f"\nand {len(status_resp) - 5} other files...\n"
                    else:
                        result = '\n'.join(status_resp) + '\n'

                    print(result)
                    
                    continue

                # printing errors
                for resp in status_resp:
                    print(f"{resp['path']} -> \n    {resp['msg']}\n")

            print(Colors.ENDC)

