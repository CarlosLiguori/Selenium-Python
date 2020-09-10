#Sep/2020
# Test: Open Browsers and test with Google page, verify if the request was correct sent.
from time import sleep
from pprint import pprint
from selenium import webdriver
from urllib.parse import urlparse
import re

browser = list(str())
browser_list = [webdriver.Firefox(), webdriver.Ie(), webdriver.Opera()]
a = dict()
b = str

for browser in browser_list:
    browser.get('http://www.google.com')


print('Browser Open!')
print()

assunto = input('Search Google or type url: ')
print()

for browser in browser_list:
    janela = browser.find_element_by_name('q')
    janela.send_keys(assunto)
    janela.submit()
    sleep(1)
    a = urlparse(browser.current_url)
    print(f'Browser: {browser}')
    print(f'url: {a}')
    b = a[4]
    print(b)
    b = a[4].replace("+", " ")  # Remove Special Chars '+' from url
    c = b.count(assunto)        # Verify how many times the 'search' shows on the url. If = 1 then search was sent correctly)
    if c == 1:
        print(f'The search/url "{assunto}" shows {c} times on the url. '
              f'The Browser "{browser}" requested was concluded CORRECTELY!')
    else:
        print(f'The search/url "{assunto}" is NOT on the url, ERROR on Browser "{browser}"!')
    print()

print('*** END ***')
