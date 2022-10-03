
from urllib.request import urlopen
#conn = httplib.HTTPConnection


url = 'https://random-ize.com/random-youtube/'

a = urlopen(url)
print(a)

# https://stackoverflow.com/questions/2146383/https-connection-python
