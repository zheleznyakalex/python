import requests

r = requests.post ('https://httpbin.org/post', data={'key': 'value'})  # отправляем пост запрос
print (r.content)  # содержимое ответа и его обработка происходит так же, как и с гет-запросами, разницы никакой нет