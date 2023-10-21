import requests
from bs4 import BeautifulSoup

res = '''
<html>
<head><title class="t" id="ti">웹 사이트 제목</title></head>
<body>
<p id="p1" class="a">test1</p>
<p class="b">test2</p>
<p class="b">test3</p>
<a class="a">test4</p>
<a>b 태그</a>
<a id="a1">c 태그</a>
</body>
</html>
'''

soup = BeautifulSoup(res, 'html.parser')
# print(soup.prettify())

# body 태그의 자식을 가져오는데
# p태그인 자식을 가져옴
print(soup.select('body p'))

# body 태그의 자식을 가져오는데
# 클래스 이름이 b인 것
print(soup.select('body .b'))

# body 태그의 자식을 가져오는데
# id 이름이 p1인 것
print(soup.select('body #p1'))

# body 태그의 자식을 가져오는데
# a태그인데 아이디가 a1인 것
print(soup.select('body a#a1'))