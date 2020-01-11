import os
print(1)
# print(os.getcwd())
# # print(os.path.dirname(os.getcwd()))
# print(os.path.realpath(__file__))
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(__file__))