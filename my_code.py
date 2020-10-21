# Collaborators (including web sites where you got help: (enter none if you didn't need help)
name=input("please enter your name: ")
age=input("please enter your age: ")
grade=input("please enter your grade: ")
school=input("please enter your school: ")
directory={}
directory.update({'name':name, 'age':age,'grade':grade,'school':school})
for key_name, value_name in directory.items():
    print(f"Your {key_name} is {value_name}")
