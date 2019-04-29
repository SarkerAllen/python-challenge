import requests
import re

content = requests.get("http://www.pythonchallenge.com/pc/def/equality.html").text
answer = re.sub('\n|\t|\r', '', content)
answer = re.findall("<!--(.*?)-->", answer)
key = re.findall("[a-z]+[A-Z]{3}([a-z])[A-Z]{3}[a-z]+", str(answer))
print(''.join(key))
