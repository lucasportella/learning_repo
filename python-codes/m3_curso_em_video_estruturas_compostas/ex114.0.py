import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('deu erro')
else:
    print('tudo certo')
    print(site.read())