text = " Hello, Python!"
text = text.strip()
print(text)
text = text.replace('!','?')
print(text)
text = text.upper()
print(text)
text = text.lower()
print(text)
assert text == "hello, python?", "Получилось что то не то"