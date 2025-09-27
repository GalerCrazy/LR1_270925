t = """
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""

t = t.strip().lower()
t = t.replace("!",".")
#t = t.replace("\n"," ")
#t = t.replace("\t"," ")
t = [s.strip() for s in t.split(".") if s.strip()]
print(t)

s1 = t[0].split()
print(s1.count("python"))
assert t[0].startswith("python")
assert t[0].endswith("language")
s = sum([len(i) for i in s1])
a = sum([i.count("a") for i in s1])
try:
    data = s1.index("data")
except:
    print("Нет такого элемента")
s1 = "-".join(s1)
print(s1)

words = set(t[0].split() + t[1].split() + t[2].split())
Wortbuch = dict()
print(words)
for i in words:
    Wortbuch[i] = t[0].count(i) + t[1].count(i) + t[2].count(i)
print(Wortbuch)

def clean_text(text):
    s = set("!?.,")
    text = text.strip().lower()
    for i in s: text = text.replace(i, " ")
    text = text.split()
    return " ".join(text)