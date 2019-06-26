import re
x = input()
new = re.sub('[\w]' ,'', x)
len(new)
