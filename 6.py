scores = {"Alice": 85, "Bob": 90, "Michael": 20}
scores["Zakhar"]=100
scores["Bob"] = 95
print(scores.get("Zakhar"),scores.get("Adolf"))
scores.pop("Michael")
print(scores, len(scores))
assert "Michael" not in scores
for i in scores.keys():
    print(i)
for i in scores.values():
    print(i)