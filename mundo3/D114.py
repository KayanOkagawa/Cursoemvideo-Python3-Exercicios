import urllib.request
import urllib.error

print('\n\033[07;36mTESTE DO SITE PUDIM\033[m')
print('-=' * 30)

try:
    teste = urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[01;31mSite Pudim não está disponivel\033[m')
else:
    print('\033[01;32mSite Pudim está disponivel\033[m')
