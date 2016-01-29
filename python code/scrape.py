from  bs4 import BeautifulSoup
import requests
page = requests.get('http://www.bbc.com/')
_content = page.content

file = open('bbc.txt','w')
file.write(_content)
file.close 

soup = BeautifulSoup(open("bbc.txt"),"lxml")
soup = BeautifulSoup("<html>data</html>")
print soup.head
