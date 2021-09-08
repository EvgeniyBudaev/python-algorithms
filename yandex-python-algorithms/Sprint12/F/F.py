# text = str(input())
text = 'A man, a plan, a canal: Panama'
text_lower = text.lower()

symbols = "!@#+-=*`~_[]{}/\$.,;: "

for char in symbols:
    text_lower = text_lower.replace(char, "")

backward = text_lower[::-1]

if text_lower == backward:
    print(True)
else:
    print(False)
