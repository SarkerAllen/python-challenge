import requests
import re

number = re.compile("(\d+)")
rs = '12345'


def target():
    global rs
    for i in range(401):
        content = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + rs).text
        # rs = re.findall(number, content)

        if re.findall(number, content):
            if len(re.findall(number, content)) == 2:
                rs = re.findall(number, content)
                content = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + rs[0]).text
                if content.find("You've been misleaded to here.") != -1:
                    print("not numbers {} It's the number{}".format(rs[0], rs[1]))
                    rs = rs[1]
            # print(rs[-1])
            # rs = rs[-1]
            else:
                rs = re.search(number, content).group(1)
                print(rs)
        else:
            if re.findall("Yes. Divide by two and keep going.", content):
                print(content)
                rs = str(int(rs) / 2)
            else:
                print(i, content)
                break


if __name__ == '__main__':
    target()

# http://www.pythonchallenge.com/pc/def/peak.html
