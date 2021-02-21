#!/usr/bin/env python
import platform


def main():
    # detaylı bilgi için:  https://docs.python.org/3/library/platform.html#module-platform
    print(platform.machine())  # x86_64 veya çalıştığınız makinenin türü
    print(platform.platform())  # kernel bilgisi ve libc göker
    print(platform.processor())  # işlemci bilgisi çıkar ama bazı güncel işlemciler yok boş dönebilir.
    print(platform.release())  # sistem sürümü veya kernel sürümü
    print(platform.system())  # linux bsd vs döner


if __name__ == '__main__':
    main()
