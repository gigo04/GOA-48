
#num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
#num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
#if num1 > num2:
  #  print(f"{num1} უფრო დიდია ვიდრე {num2}")
#elif num1 < num2:
 #   print(f"{num2} უფრო დიდია ვიდრე {num1}")
#else:
 #   print("ორივე რიცხვი ტოლია")


#

#score = int(input("შეიყვანეთ ქულა (0-100): "))
#if score >= 90 and score <= 100:
 #   print("შესანიშნავი")
#elif score >= 70 and score <= 89:
#    print("კარგი")
#elif score >= 50 and score <= 69:
#    print("დამაკმაყოფილებელი")
#elif score >=0  and score <= 49:
#    print("დამაკმაყოფილებელი")
#else:
#    print("error")



celsius = int(input("შეიყვანეთ გრადუსი:"))
if celsius <0:
    print("freeze")
elif celsius >=0 and celsius <=15:
    print("cold")
elif celsius >=16 and celsius <=30:
    print("hot")
elif celsius >30:
    print("very hot")