import pickle
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

# alex = Student('alex',84)
# alex1 = Student('老王',33)
# alex2 = Student('周老板',22)
# alex3= Student('小汤',11)
# alex4 = Student('刘晓松',6)
# with open('stu','wb') as f:
#     pickle.dump(alex,f)
#     pickle.dump(alex1,f)
#     pickle.dump(alex2,f)
#     pickle.dump(alex3,f)
#     pickle.dump(alex4,f)

# with open('stu','rb') as f:
#     while True:
#         try:
#             alex = pickle.load(f)
#             print(alex.__dict__)
#             print(alex.name)
#             print(alex.age)
#         except EOFError:
#             break

