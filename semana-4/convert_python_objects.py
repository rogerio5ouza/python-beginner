'''
Podemos converter objetos de tipos em Python em Strings JSON:

- dict
- list
- tuple
- string
- int
- float
- True
- False
- None

'''
import json

print(json.dumps({"nome": "Joao", "idade": 30}))
print(json.dumps(["maca", "bananas"]))
print(json.dumps(("maca", "bananas")))
print(json.dumps("ola"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
