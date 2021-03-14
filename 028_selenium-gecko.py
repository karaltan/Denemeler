#!/usr/bin/env python
from selenium import webdriver
import urllib.parse


def main():
    aranan = input("Ara: ")
    site = "https://eksisozluk.com/?q={}".format(urllib.parse.quote(aranan))
    driver = webdriver.Firefox()
    driver.set_window_size(1024, 768)
    try:
        driver.get(site)
        entry = driver.find_elements_by_class_name("content")
        for i in entry:
            print(i.text)
    except Exception as e:
        print("Hata {}".format(e))
        driver.quit()
    finally:
        driver.quit()


if __name__ == '__main__':
    main()
