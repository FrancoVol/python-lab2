from sys import argv
tasks=[]
flag=True
file = argv[1]
txt = open(file)
for line in txt.read().splitlines():
    tasks.append(line)
txt.close()
while flag==True:
    print('''Choose one task:
[1. insert a new task
 2. remove a task
 3. show all existing tasks
 4. close the program]''')
    a=int(input())
    if a==1:
        print("Insert the task you want to add:")
        tasks.append(input())
    elif a==2:
        print ("Insert the task you want to remove:")
        rmv=input()
        for search in tasks:
            if rmv==search:
                tasks.remove(rmv)
    elif a==3:
        tasks.sort()
        print("The tasks are:")
        for task in tasks:
            print(task)
    elif a==4:
        flag=False
    else:
        print ("Wrong command. Retry.")
tasks.sort()
txt = open(file, "w")
for task in tasks:
    txt.write(task + "\n")
txt.close()