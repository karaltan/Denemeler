#!/usr/bin/python3


def main():
    # isistance örneği, isistance(veri, veritürü)
    # sorulanan verinin türünün doğru olup olmadığını kmontrol eder örn.
    a = 256
    if isinstance(a, int):
        print("Veri int türünde")
    else:
        print("Veri int değil")

    # başka bir örnek
    liste = ["Gnu", "Linux", "python", "editor", "code"]
    if isinstance(liste, list):
        print("Veri liste türünde")
    else:
        print("veri liste türünde değil")

    # başka bir örnek
    isim = "python"
    if isinstance(isim, str):
        print("veri string türünde")
    else:
        print("veri string türünde değil")


if __name__ == "__main__":
    main()
