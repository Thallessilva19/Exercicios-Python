import urllib.request
try:
    site=urllib.request.urlopen('https://www.google.com/search?q=instituto+consulplan&oq=in&gs_lcrp=EgZjaHJvbWUqDggCEEUYJxg7GIAEGIoFMgwIABBFGDkYsQMYgAQyDwgBEEUYOxiDARixAxiABDIOCAIQRRgnGDsYgAQYigUyBggDEEUYOzINCAQQABiDARixAxiABDIKCAUQABixAxiABDIHCAYQABiABDIGCAcQRRg80gEIMjI3MGowajSoAgCwAgE&sourceid=chrome&ie=UTF-8')
except:
    print('O site não está disponivel')
else:
    print('O site está disponivel')
    print(site.read())
