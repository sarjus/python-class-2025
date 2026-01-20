with open("input.txt","w") as file:
    file.write("Hello Python"+"\n")
with open("input.txt","a") as file:
    file.write("Hello World")
with open("input.txt","r") as file:
    content = file.readline()
print(content)