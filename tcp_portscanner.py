import socket
import threading
import sys


class Scanner:
    def __init__(self, ip, port_range):
        self.__lock = threading.Lock()
        self.ip = str(ip)
        self.port_range = int(port_range)
        self.open_ports = []
        self.__threads = []

    def scan(self, port: int):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect((self.ip, port))
                self.open_ports.append(port)
            except:
                pass

    def start(self):
        print(f"Scann ports on {self.ip}")
        for port in range(self.port_range):
            with self.__lock:
                thread = threading.Thread(target=self.scan, args=(port,))
                self.__threads.append(thread)

        for thread in self.__threads:
            thread.start()

        for thread in self.__threads:
            thread.join()


if __name__ == "__main__":
    scanner = Scanner(sys.argv[1], sys.argv[2])
    scanner.start()
    print(scanner.open_ports)
