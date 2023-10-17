def validate_date(date: str):
   valoraño = int(input("Introduzca la fecha:"))
   d, m, a =list(map(int, date.split()))
   if valoraño % 4 ==0 and valoraño % 100!=0:
      print(valoraño, "es un año bisiesto")
   else:
      print(valoraño , "no es un año bisiesto")
      return valoraño
   validate_date()
      


# Inicializar una cadena vacia
def triangulo(n):
    res = ""
    for i in range(1,n + 1 ):
        for j in range(1, i+1):
         res += "*"
         res +="/n"
         return res
        n = int(input("Ingrese (n):"))
        print(triangulo(n))
