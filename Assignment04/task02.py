name="output.txt"
f = open(name, "w")
cont = input("Enter text to write to the file : ")
f.write(cont+"\n")
print("Data successfully written to " , name)
f.close()

f = open(name , "a")
add = input("Enter additional text to append: ")
f.write(add)
print("Data successfully appended.")
f.close()

f = open(name , "r")
reading_file = f.read()
print("Final content of output.txt :\n" , reading_file)
f.close()