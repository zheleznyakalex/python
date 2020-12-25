def my_decorator(fn):
   def wrapper():
       fn()
   return wrapper  # возвращается задекорированная функция, которая заменяет исходную

# выведем незадекорированную функцию
def my_function():
   pass
print(my_function)  # <function my_function at 0x7f938401ba60>

# выведем задекорированную функцию
@my_decorator
def my_function():
   pass
print(my_function)  # <function my_decorator.<locals>.wrapper at 0x7f93837059d8>