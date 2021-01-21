
import requests
import json

a = requests.get("https://baconipsum.com/api/?type=meat-and-filler")

a = json.loads(a.content)

print(type(a))
print(a[0]) # выводим первый сгенерированный текст

