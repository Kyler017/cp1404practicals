name = input("what is your name: ")
out_file = open("name.txt","w")
print(name,file=out_file,end="")
out_file.close()

in_file = open("name.txt","r")
print(f"Hi!{name}!")
in_file.close()

with open("numbers.txt") as in_file:
    i = 0
    for line,_ in zip(in_file,range(2)):
        i += int(line)
    print(i)

with open("numbers.txt") as in_file:
    i = 0
    for line in in_file:
        i += int(line)
    print(i)