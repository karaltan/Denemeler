#!/usr/bin/env python
from scipy.interpolate import interp1d


def main():
    X_nem = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    Y_isi = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105]
    intp = interp1d(X_nem, Y_isi, fill_value="extrapolate")
    print(intp.x, intp.y)
    print(intp(125))  # X 125 olunca Y 130 olur.


if __name__ == '__main__':
    main()
