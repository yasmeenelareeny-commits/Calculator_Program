print("Welcome To Our Calculator Program")
num_1 = float(input("enter the first number :"))
num_2 = float(input("enter the second number :"))
operator = input(" choose the operator what you want from ( + , - ,* ,/ , % ) :").strip()
result = None
if operator == "+" :
  result = num_1 + num_2
elif operator =="-" :
  result = num_1 - num_2
elif operator =="*" :
    result = num_1 * num_2
elif operator == ("/") :
  if num_2 != 0:
    result = num_1 / num_2
  else :
      print("You cannot divide by zero")
elif operator =="%" :
    if num_2 != 0:
      result = num_1 % num_2
    else :
      print("You cannot perform modulo by zero")
else:
  print(" invalid operator ! ")
print ("the result =  ", result)


