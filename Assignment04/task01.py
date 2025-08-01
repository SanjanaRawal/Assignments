name = "sample.txt"
try :
    f = open(name, "r")
    l = f.readlines()
    print("Reading file content : \n")
    for i in range(0, len(l)):
        print("Line ", i, " : ", l[i])
except FileNotFoundError :
    print(f"Error: The file {name} was not found ")