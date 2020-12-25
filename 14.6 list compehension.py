map(func, list1)  # итератор, но никаких вычислений не будет произведено
list(map(...))  # только здесь появляется объект

[func(i) for i in list1]  # сразу готовый объект


[func(i) for i in list1] == list(map(func, list1))  # результат один и тот же