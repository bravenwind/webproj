import requests
from bs4 import BeautifulSoup

res = '''
<html>
<head><title class="t" id="ti">웹 사이트 제목</title></head>
<body>
<p id="p1">test1</p>
<a id="p1">test11</p>
<p class="a">test2</p>
<p class="a">test3</p>
<a class="a">test4</p>
<a>a 태그</a>
<b>b 태그</b>
<c>c 태그</c>
</body>
</html>
'''

soup = BeautifulSoup(res, 'html.parser')
# print(soup.prettify())

# .(점) 클래스, #(샵) 아이디

p = soup.select('p') # 모든 p 태그
print(p)

p_a = soup.select('.a') # 클래스 이름이 a인 것 모두
print(p_a)

p_id = soup.select('#p1') # id가 p1인 것 모두
print(p_id)

p_tags = soup.select('p.a') # p태그 중에서 클래스가 a인 것 모두
print(p_tags)

p_ids = soup.select('p#p1') # p태그 중에서 id가 p1인 것 모두
print(p_ids)