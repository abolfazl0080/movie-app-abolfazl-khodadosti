data = [
    {"id":1, "name":"alice", "score":3},
    {"id":2, "name":"Bob", "score":7.87},
    {"id":3, "name":"charlie", "score":9.001},
    {"id":4, "name":"david", "score":11},
    {"id":5, "name":"eve", "score":13},
    {"id":6, "name":"frank", "score":8},
    {"id":7, "name":"grance", "score":9},
    {"id":8, "name":"hannah", "score":9.2},
    {"id":9, "name":"isaac", "score":8.86},
]

for person in data:
    score = int(person["score"])
    if score != person["score"]:
        person["score"] = score + 1
    if person["score"] >= 10:
        person["status"] = "Passed"
    else:
        person["status"] = "Fail"
print(data)
