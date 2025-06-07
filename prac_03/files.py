name = input("what is your name: ")
out_file = open("name.txt","w")
print(name,file=out_file,end="")
out_file.close()

