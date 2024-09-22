import hashlib
import threading
from pathlib import Path


class CrackHash:
    def __init__(self, password_hash: str, wordlist: str, threads: int):
        self.wordlist = Path(wordlist)
        if not self.wordlist.exists():
            raise AttributeError
        self.password_hash = password_hash
        self.threads = threads
        self.__thread_list = []

        self.password = None

    def cut_wordlist(self):
        with self.wordlist.open('r', errors='replace') as file:
            lines = file.readlines()
            division_num = len(lines) // self.threads

            for _ in range(self.threads):
                yield [word.replace("\n", "") for word in lines[:division_num]]
                del lines[:division_num]

    def crack_hash(self, wordlist: list):
        password_hash = self.password_hash
        for word in wordlist:
            # Just change sha1 on your hash type 
            if hashlib.sha1(word.encode()).hexdigest() == password_hash:
                self.password = word

    def crack(self):
        for words in self.cut_wordlist():
            self.__thread_list.append(threading.Thread(target=self.crack_hash, args=(words,)))

        for thread in self.__thread_list:
            thread.start()

        for thread in self.__thread_list:
            thread.join()

        return self.password
