import os
import random
os.path.exists('fortunedat.txt')
True
# i = 1
# t = '%\n'
# fin = open('fortunedat.txt')
# for line in fin:
#      with_commas = (line.split(t))
#      i = i + 1
#      tuple_fortunes = tuple(with_commas)
#      print(tuple_fortunes)
#      if i == 20:
#
#         break
#
# for t, element in enumerate(fin, start =1):
#      (t, element)
#      i = i + 1
#      print(var.split('%'))
#      if i == 20:
#           break


with open('fortunedat.txt', 'r') as file_handler:
     options = file_handler.read()
     line = options.split('%')
     line_position = random.randint(0, len(line)-1)
     print(line[line_position])


#
# fortunes = fin.split('%')
# print(fortunes)


#
# for t, element in enumerate(fin, start =1):
#     print(t, element)


# for pair in zip(t, fin):
#     print(pair)
#     i = i + 1
#     if i == 15443:
#         break

    # print(fin.count('%'))
#
# def fortunes(**fin):
#     print(type(fin))
#     for t, value in fin.items():
#         print(f"{t}: {value}")