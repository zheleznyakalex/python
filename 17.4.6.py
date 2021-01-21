N_max = int (input ("Определите размер очереди:"))

queue = [0 for _ in range (N_max)]  # инициализируем список с нулевыми элементами
order = 0  # будем хранить сквозной номер задачи
head = 0  # указатель на начало очереди
tail = 0  # указатель на элемент следующий за концом очереди

while True:
    cmd = input ("Введите команду:")
    if cmd == "empty":
        if is_empty ():
            print ("Очередь пустая")
        else:
            print ("В очереди есть задачи")
    elif cmd == "size":
        print ("Количество задач в очереди:", size ())
    elif cmd == "add":
        if size () != N_max:
            add ()
        else:
            print ("Очередь переполнена")
    elif cmd == "show":
        if is_empty ():
            print ("Очередь пустая")
        else:
            show ()
    elif cmd == "do":
        if is_empty ():
            print ("Очередь пустая")
        else:
            do ()
    elif cmd == "exit":
        for _ in range (size ()):
            do ()
        print ("Очередь пустая. Завершение работы")
        break
    else:
        print ("Введена неверная команда")

def is_empty(): # очередь пуста?
    # да, если указатели совпадают и в них содержится ноль
    return head == tail and queue[head] == 0