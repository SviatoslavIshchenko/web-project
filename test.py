import re
text_dot = "abcdeaf"
text_dot1 = r"a\ncdeaf"
pattern = r"a."
print(re.findall(pattern, text_dot))
print(re.findall(pattern, text_dot1))