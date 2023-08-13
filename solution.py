def validate_date(date: str) -> str:
   d, m, a = list(map(int, date.split()))

ano = int(input("introduzca un año")) 


if ano%4==0:
   print("año comun")

elif ano %100==0:
   print("año bisiesto")

elif ano %400==0:
   print("año comun")

elif ano< 1800:
   print("no dentro del periodo del calendario gregoriano")

else:
   print("año comun")