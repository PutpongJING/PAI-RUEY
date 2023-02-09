from itertools import permutations 
import operator
import math

op = ['+', '-', '*', '/']

def factorial(number):
   if number == 1:
      return 1
   else:
      return number * factorial(number-1)

def all_probability(get_input):
    perm = permutations(get_input) 
    return perm

def get_operation(data):
  op_list = []
  for i in op:
    for j in op:
      for k in op:
        add_op = [i, j ,k]
        op_list.append(add_op)
  return op_list

def main():
  while True:
    P1, P2, P3, P4, P5 = 0,0,0,0,0
    print('- - - - - - - - - - -')
    print('Welcome to 24 game.\nGame that use 4 inputted numbers for calculating various way to get the answer: 24')
    get_input = input("Number input(only 4 random numbers): ")
    test_subject = get_input.split()
    print('- - - - - NUMBER - - - - - -')
    print(test_subject)
    print('- - - - - ANSWER- - - - - -')
    for i in all_probability(test_subject):
        for j in get_operation(op):
            exp1 = i[0] + j[0]+ i[1] + j[1] + i[2] + j[2] + i[3]# 1+2+3+4
            exp2 = "(" + i[0] + j[0]+ i[1] + ")" + j[1] + "(" + i[2] + j[2] + i[3] +")"#(1+2)+(3+4)
            exp3 = "(" + "(" +i[0] + j[0]+ i[1] + ")" + j[1] + i[2] + ")" + j[2] + i[3]#((1+2)+3)+4
            exp4 = i[0] + j[0] + "(" + i[1] + j[1] + "(" + i[2] + j[2] + i[3] + ")" + ")"# 1+(2+(3+4))
            exp5 = "(" + i[0] + j[0]+ "(" + i[1] + j[1] + i[2] + ")" + ")" + j[2] + i[3]#(1+(2+3))+4
            if P1 == 1 and P2 == 1 and P3 == 1 and P4 ==1:#จำนวนรูปแบบที่ต้องการแสดง
               break
            12/(3-(5/2))
            try:
                if eval(exp1) == 24 and P1 == 0:
                    print(f"{i[0]} {j[0]} {i[1]} {j[1]} {i[2]} {j[2]} {i[3]} = {int(eval(exp1))}")
                    P1 = 1
                elif eval(exp2) == 24 and P2 == 0:
                    print(f"( {i[0]} {j[0]} {i[1]} ) {j[1]} ( {i[2]} {j[2]} {i[3]} ) = {int(eval(exp2))}")
                    P2 = 1
                elif eval(exp3) == 24 and P3 == 0:
                    print(f"( ( {i[0]} {j[0]} {i[1]} ) {j[1]} {i[2]} ) {j[2]} {i[3]} = {int(eval(exp3))}")
                    P3 = 1
                elif eval(exp4) == 24 and P4 == 0:
                    print(f"{i[0]} {j[0]} ( {i[1]} {j[1]} ( {i[2]} {j[2]} {i[3]} ) ) = {int(eval(exp4))}")
                    P4 = 1
                elif eval(exp5) == 24 and P5 == 0:
                    print(f"( {i[0]} {j[0]} ( {i[1]} {j[1]} {i[2]} ) ) {j[2]} {i[3]}  = {int(eval(exp5))}")
                    P5 = 1
            except ZeroDivisionError:
               ...

    print('- - - - - - - - - - - - - -')
    print('Thank you for using our 24 game generator.')
main()
            # if eval(exp1) == 24:
            #     print(f"{exp1} = {eval(exp1)}")
            # elif eval(exp2) == 24:
            #     print(f"{exp2} = {eval(exp2)}")
            # elif eval(exp3) == 24:
            #     print(f"{exp3} = {eval(exp3)}")
            # elif eval(exp4) == 24:
            #     print(f"({exp4}  = {eval(exp4)}")