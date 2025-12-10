file = open("My Project.txt","w")
file.write("Welcome to My Project\n")
file.write("The file topic is Python.\n")
file.close()

file = open("My Project.txt","r")
content = file.read()
print("Content:\n",content)
file.close()

file= open("My Project.txt","a")
file.write("Introduction.\n")
file.close()