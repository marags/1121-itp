import re

# mystring = 'words'
# words = 'these are some words'
# myotherstring = f'I have something to say {words}'

# s = 'a\tb'
# print(s)

# raw_string = r'a\tb'
# print(raw_string)

pattern = r"\d+"
textA = "42 is my lucky number"

match = re.match(pattern, textA)
print(match)