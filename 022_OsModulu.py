#!/usr/bin/env python
import os


def main():
    # detaylı bilgi için:  https://docs.python.org/3/library/os.html#module-os
    print(os.name)  # posix ( linux üzerinde )
    print(os.ctermid())  # /dev/tyy kullanılan terminal. Muhtemelen windows üzerinde çalışmayacaktır
    # print(os.environ)  # çalıştığınız ortam bilgileri, renk shell çalışılan dizin vs.
    print(os.getcwd())  # çalışılan dizin
    print(os.uname())  # terminalden uname çıktısının aynısı
    print(os.get_terminal_size())  # satır ve sutün olarak çalıştığınız terminal boyutu döner
    print(os.cpu_count())  # çalışılan sistemdeki CPU çekirdek sayısı döner.
    print(os.getloadavg())  # sistem yükü döner (1 5 15) dakika aralığında


if __name__ == '__main__':
    main()
