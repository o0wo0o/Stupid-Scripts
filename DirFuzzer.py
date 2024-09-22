from anyio import open_file, run, create_task_group
import httpx
import argparse


class AsyncDirFuzzer:

    def __init__(self, base_url: str, wordlist: str, bad_header: str, timeout: int):
        self.base_url = base_url
        self.wordlist = wordlist
        self.timeout = timeout
        self.answer_list = []
        self.bad_header = bad_header

    async def scan(self, url: str) -> None:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, timeout=self.timeout)
            print(".")
            if response.status_code != self.bad_header:
                self.answer_list.append(url.strip('\n') + " return " + str(response.status_code))

    async def start(self) -> None:
        async with create_task_group() as tg:
            async with await open_file(self.wordlist) as file:
                async for line in file:
                    tg.start_soon(self.scan, self.base_url + line.strip('\n'))
        print(self.answer_list)


if __name__ == "__main__":
    ####################################################################################################################
    # 🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡
    # 🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡
    # 🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡
    parser = argparse.ArgumentParser(prog="4a$t $cAnn9r")
    parser.add_argument("-u", "--url", help="base url address of target site", type=str)
    parser.add_argument("-eh", "--eheader", help="title to be exclude", type=int)
    parser.add_argument("-w", "--wordlist",
                        default="/usr/share/wordlists/wfuzz/webservices/ws-dirs.txt",
                        type=str)
    args = parser.parse_args()
    # 🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡
    # 🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡
    # 🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡🤡
    ####################################################################################################################
    print("start")
    scanner = AsyncDirFuzzer(args.url, args.wordlist, args.eheader, 1)
    run(scanner.start)
    print("stop")
