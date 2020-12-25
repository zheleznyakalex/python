def make_adder(x):
   def adder(n):
       return x + n # захват переменной "x" из nonlocal области
   return adder  # возвращение функции в качестве результата
# функция, которая будет к любому числу прибавлять пятёрку
add_5 = make_adder(5)
print(add_5(10))  # 15
print(add_5(100))  # 105