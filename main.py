import re

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo1 = phoneNumberRegex.search('My number is 503-484-4699')
print(mo1.group())