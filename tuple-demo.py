# Writing (Overwrites)
with open("note.txt", "w") as file:
    for i in range(10):
        file.write(str(i)+"\n")

# Appending (Adds to the end)
with open("note.txt", "r") as file:
    lines = file.readlines()
s=0
for line in lines:
    line = line.strip()
    s= s+int(line)
print(s)