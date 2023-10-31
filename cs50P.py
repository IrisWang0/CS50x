# name = input("what is your name?")
# print("hello," + name)


# x = 1
# y = 1
# z = x + y
# print(z)


# def plus1(a):
#     print( a + 1 )

# b = input('please enter a number:')
# b = int(b)
# plus1(b)


# def main():
#     name = input("what's your name?")
#     hello(name)

# def hello(to="world"):
#     print("hello,", to)

# main()


# def main():
#     x = int(input("what's x?"))
#     print("x squared is", square(x))
# def square(n):
#     return n * n
# main()


# x = int(input("what's x?"))
# y = int(input("what's y?"))
# if x < y:
#     print("x is less than y")
# if x > y:
#     print("x is greater than y")
# if x == y:
#     print("x is equal to y")
    

# def main():
#     x = int(input("what's x?"))
#     if is_even(x):
#        print("Even")
#     else:
#        print("Odd")
     
# def is_even(n):
#     return True if n % 2 == 0 else False

# main()


# def main():
#      x = int(input("what's x?"))
#      if is_even(x):
#         print("Even")
#      else:
#         print("Odd")
     
# def is_even(n):
#      return n % 2 == 0

# main()


# name = input("what's your name?")

# match name:
#     case "Harry" | "Hermione" | "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")


# i = 3
# while i != 0:
#     print("meow")
#     i = i -1


# i = 0
# while i < 3:
#     print("meow")
#     i += 1


# for i in [0, 1, 2]:
#     print("meow")


# for i in range(3):
#     print("meow")


# for _ in range(3):
#     print("meow")


# print("meow\n" * 3, end="")


# print("meow\n" * 3)



# while True:
#     n = int(input("what's n?"))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")




# def main():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         n = int(input("what's n?"))
#         if n > 0:
#             return n 

# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()



# students = ("a", "b", "c")
# for student in students:
#     print(student)


# students = ("a", "b", "c")
# for i in students:
#     print(i)


# students = ["a", "b", "c"]
# for i in range(len(students)):
#     print(i + 1, students[i])


# students = ["a", "b", "c"]
# for i in range(2):
#     print(i + 1, students[i])



# def main():
#     print_column(3)

# def print_column(height):
#     for _ in range(height):
#         print("#")
# main()



# def main():
#     print_row(4)

# def print_row(width):
#     print("?"* width)

# main()



# def main():
#     print_square(5)

# def print_square(size):
#     for i in range(size):
#         print_row(size)

# def print_row(width):
#     print("#" * width)

# main()



# def main():
#     print_column(5)

# def print_column(height):
#     print("#\n" * height, end="")

# main()



# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)

# main()



# def main():
#      x = int(input("what's x?"))
#      print_square(x)

# def print_square(size):
#     for i in range(size):
#             print("#")

# main()



# def main():
#      x = int(input("what's x?"))
#      print_square(x)

# def print_square(size):
#     for i in range(size):
#             print("#", end="")

# main()




# def main():
#      x = int(input("what's x?"))
#      print_square(x)

# def print_square(size):
#     for i in range(size):
#             for j in range(size):
#                 print("#", end="")
#             print('\n')

# main()



# def main():
#      x = int(input("what's x?"))
#      print_square(x)

# def print_square(size):
#     for i in range(size):
#             for j in range(size):
#                 print("#", end="")
#             print()
# main()



# def main():
#      x = int(input("what's x?"))
#      print_square(x)

# def print_square(size):
#     for i in range(size):
#             for j in range(size):
#                 print("#", end="")

# main()



# def main():
#      x = int(input("what's x?"))
#      print_square(x)

# def print_square(size):
#     for i in range(size):
#             print("#" * size)

# main()




# 序列 = [1, 2, 3, 4, 5]

# for i in range(len(序列)):  
#     print(i)  


# 序列 = [1, 2, 3, 4, 5]
# for i in range(len(序列)):  
#     print(序列 [i])  



# for i in range(1, 10):
#       for j in range(1, i+1):
#             print('{}*{}={}\t'.format(j, i, i*j), end='')
#       print('\n')



# try:
#     x = int(input("what is x?"))
#     print(f"x is (x)")
# except ValueError:
#     print("x is not an integer")


# try:
#     x = int(input("what is x?"))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")


# while True:
#     try:
#         x = int(input("what is x?"))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break

# print(f"x is {x}")



# while True:
#     try:
#         x = int(input("what is x?"))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         print(f"x is {x}") 
   


# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("what is x?"))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break

# main()



# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("what is x?"))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break
#     return x

# main()



# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             x = int(input("what is x?"))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x 

# main()



# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("what is x?"))
#         except ValueError:
#             print("x is not an integer")

# main()



# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("what is x?"))
#         except ValueError:
#             pass

# main()



# def main():
#     x = get_int("what is x?")
#     print(f"x is {x}")

# def get_int(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             pass

# main()



# import random

# coin = random.choice(["heads", "tails"])
# print(coin)


# from random import choice



# import random

# number = random.randint(1,10)
# print(number)



# import random

# cards = ["jack", "queen", "king"]
# random.shuffle(cards)
# for x in cards:
#     print(x)



# import statistics
# print(statistics.mean([100,91]))


# import sys
# print("hello, my name is", sys.argv[2])


# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("hello, my name is", sys.argv[1])



# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")

# for arg in sys.argv[1:]:
#     print("hello, my name is", arg)


# import cowsay
# import sys

# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1])



# def main():
#     x = int(input("what is x?"))
#     print("x square is", square(x))

# def square(n):
#     return n * n

# from calculator import main
# # if __name__ == "__main__":
# main()


# from calculator import square

# def main():
#     test_square()

# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared is not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared is not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared is not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared is not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 squared is not 0")

# if __name__ == "__main__":
#     main()



# from calculator import square

# def test_assert():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0



# names = []

# for _ in range(3):
#     names.append(input("What's your name?" ))

# for name in sorted(names):
#     print(f"hello, {name}")



from calculator import square
  
  
def test_square():
    assert square(3) == 9