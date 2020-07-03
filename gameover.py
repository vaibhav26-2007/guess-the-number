import random
lst = [75]
c = random.choice(lst)
t=5
print("WELCOME")
print("select number between 0 to 100")
while(True):
 n1=int(input("enter the number so u can win by guessing:"))
 t=t-1
 print("number of guesses remainimg:",t)
 if t<=0:
  print("you have 0 guess remaining your Game Over:")
  break
 else:
  if n1==c:
   print("perfect you have won")
   break
  elif n1>c:
   print("less than this")
   continue
  else:
   print("add more to the guessed number")
  continue


