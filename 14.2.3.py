def rec_sum(n):
   if n == 1:  # терминальный случай
       return 1
   return n + rec_sum(n - 1)  # рекурсивный вызов
rec_sum(5)
print(rec_sum(5))