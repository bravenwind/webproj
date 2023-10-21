import requests
from bs4 import BeautifulSoup

res = '''
<html>
<head><title class="t" id="ti">웹 사이트 제목</title></head>
<body>
<p id="p1">test1</p>
<p class="nice">test2</p>
<p id="p3">test3</p>
</body>
</html>
'''

soup = BeautifulSoup(res, 'html.parser')
# print(soup.prettify())
# p = soup.find_all('p', id='p3')
# print(p)

p = soup.find('p', {'class':'nice'})
print(p)