def D(a,b,c):
    return b**2 - 4*a*c
def quadratic_solve(a,b,c):
    if D(a,b,c) < 0:
      return "Нет вещественных корней"
print(quadratic_solve(2,3,4))