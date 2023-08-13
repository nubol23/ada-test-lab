def validate_date(date: str):
   valoraño = int(input("6 7 531:"))
   d, m, a =list(map(int, date.split()))
   if valoraño % 4 ==0 and valoraño % 100!=0:
      print(valoraño, "es un año bisiesto")
   else:
      print(valoraño , "no es un año bisiesto")
      return valoraño
   validate_date()

