"""
MORE ON IF STATEMENTS

--- if-elif-else STATEMENT ---

--- OR OPERATION ---
if ((condition1 == True) or (condition2 == True)) :
   print("something") -> if at least one of the two conditions is true
 else:
   print("something else") ->  if both conditions are false

--- AND OPERATION ---
if ((condition == True) and (condition2 == True)):
    print("something") -> if both conditions are true
else:
    print("something else") -> if at least one of the conditions is false

--- while STATEMENTS ---
while (condition == true):
    print("something") -> this will be performed repeatedly until condition == false

The while statement requires that at some point the condition will become false, otherwise
we are trapped in an infinite loop.

If we need a "safety net" for the while-loop to terminate, then we can use a break
statement.

the "break" statement will terminate the loop even if the condition inside the
corresponding "while" is true
"""

def main() -> None:
    # EXAMPLE 1
    for ii in range(1,101):
      if (ii % 2 == 0):
        print(str(ii) + " even number")
      elif (ii % 3 == 0):
        print(str(ii) + " is divisible by 3")
      elif(ii % 5 == 0):
        print(str(ii) + " is divisible by 5")
      else:
        print(str(ii) + " is not divisible by 2 nor 3 nor 5")

    print('\n') # /n: special character denoting new line

    # EXAMPLE 2
    for ii in range(1,101):
      if ((ii % 2 == 0) or (ii % 3 == 0) or (ii % 5 == 0)):
        print(str(ii))
      else:
        print(str(ii) + " is not divisible by 2 nor 3 nor 5")

    print('\n')

    # EXAMPLE 3
    jj = 0
    while (jj<100):
        jj = jj + 1
        print("iteration " + str(jj))
        if (jj == 50):
            break
    print("total number of iterations is ", str(jj))

if __name__ == "__main__":
    main()
