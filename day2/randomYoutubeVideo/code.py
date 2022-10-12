import requests, re, webbrowser

url = 'https://www.vtomb.com/'
response = requests.get(url)
print(re.findall("www.youtube.com/embed/\w{11}", response.text))
youtube = re.search("www.youtube.com/embed/\w{11}", response.text)

yewtube = re.sub('youtube.com', 'yewtu.be',youtube[0])


webbrowser.open(yewtube)

# https://stackoverflow.com/questions/2146383/https-connection-python
