def mirror(a, res=0):
    return mirror(a // 10, res*10 + a % 10) if a else res