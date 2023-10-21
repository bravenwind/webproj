import requests
from bs4 import BeautifulSoup

res = '''
<html>
<head><title class="t" id="ti">웹 사이트 제목</title></head>
<body>
<ul>
    <li>hello</li>
    <li>사과</li>
    <li>떡볶이</li>
</ul>
</body>
</html>
'''

soup = BeautifulSoup(res, 'html.parser')
# print(soup.prettify())

ul = soup.find('ul')
li = ul.findAll('li')
print(li)

for i in li:
    print(i, i.get_text())

# for i in range(0, len(li), 1):
#     print(li[i], li[i].get_text())
