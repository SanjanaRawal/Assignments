marks = {"Anne" : 90  ,
         "Joy" : 76 ,
         "Alice" : 85 ,
         "Nick" : 43}
name = input("Enter the student's name : ")

if name in marks.keys() :
    print(f"{name}'s marks : {marks[name]}")
else :
    print("Student not found.")