numbers = []
for i in range(5):
    num = float(input("please enter numbers: "))
    numbers.append(num)
print(f"The first number is：{numbers[0]}")
print(f"The last number is：{numbers[-1]}")
print(f"The smallest number is：{min(numbers)}")
print(f"The larges number is：{max(numbers)}")
print(f"The average number is：{sum(numbers)/len(numbers)}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
names = input("please enter usernames:")
if names in usernames:
    print("Access granted")
if names not in usernames:
    print("Access denied")