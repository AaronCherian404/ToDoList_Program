import sys
import os

def PrintUsage(*args):
    print("Usage :-")
    print('$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list')
    print("$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order")
    print("$ ./task del INDEX            # Delete the incomplete item with the given index")
    print("$ ./task done INDEX           # Mark the incomplete item with the given index as complete")
    print("$ ./task help                 # Show usage")
    print("$ ./task report               # Statistics")
    pass
def Content():
    path=r"text.txt"
    lineno=1
    if os.stat(path).st_size==0:
        print("There are no pending tasks!")
    else:
        with open(path,"r") as file:
            for line in file:
                p=line[0]
                line=line[2:len(line)-1]            #Adjusts for accurate input
                print(str(lineno)+". "+line+" ["+p+"]")
                lineno+=1
    

def Adding(A,B):
    path=r"text.txt"
    file_obj=open(path,"a")
    s=A+" "+B+"\n"
    with open(path,'r') as file:
        lines=file.readlines()
        if s in lines:
            print('Added task: "'+B+'"')
        else:
            file_obj.write(A+" "+B+"\n")    #adds to file
            print('Added task: "'+B+'" with priority '+A) 
    file_obj.close()
    Sorting()

def Deleting(a):
    path=r"text.txt"
    a_file = open(path, "r")
    lines = a_file.readlines()
    a_file.close()
    a_file = open(path, "w")         
    lineno=1         #c checks if the required element is present
    c=0
    for line in lines:
        if lineno==a:
            c=1
            print("Deleted task #"+str(a))
        else:
            a_file.write(line)
        lineno+=1
    a_file.close()    
    if c==0:
        print("Error: task with index #"+str(a)+" does not exist. Nothing deleted.")
def Sorting():
    path=r"text.txt"
    data=[]
    with open(path,"r") as file:
        for line in file:
            data.append(line.strip())
    data.sort()                     #sorts in ascending order
    with open(path,"w") as file:
        for line in data:
            file.write(line+"\n")
def Completed(a):
    path=r"text.txt"
    a_file = open(path, "r")
    path2=r"completed.txt"
    new_file=open(path2,'a')
    lines = a_file.readlines()
    a_file.close()
    a_file = open(path, "w")
    c=0
    lineno=1 #checks if the required element is present
    for line in lines:
        if lineno!=a:
            a_file.write(line)
        else:
            line=line[2:len(line)-1]
            new_file.write(line+"\n")
            c=1
        lineno+=1
    a_file.close()
    new_file.close()
    if c==1:
        print("Marked item as done.")
    else:
        print("Error: no incomplete item with index #"+str(a)+" exists.")

def Reporting():
    path=r"text.txt"
    a_file = open(path, "r")
    lines = a_file.readlines()
    a_file.close()
    print("Pending : "+str(len(lines)))     #reads from the text.txt file
    lineno=1
    with open(path,"r") as file:
        for line in file:
            p=line[0]
            line=line[2:len(line)-1]
            print(str(lineno)+". "+line+" ["+p+"]")
            lineno+=1
    path2=r"completed.txt"
    b_file = open(path2,"r")
    lines = b_file.readlines()
    b_file.close()
    print("Completed : "+str(len(lines)))     #reads from the completed.txt file
    lineno=1
    with open(path2,'r') as file:
        for line in file:
            line=line[:len(line)-1]
            print(str(lineno)+". "+line)
            lineno+=1


if __name__ == "__main__":          #driver function
    f1=0
    arg1=0
    try:                            #try and except blocks catch for missing numbers
        arg1 = str(sys.argv[1])
    except IndexError:
        f1=1                        #f1 checks if it should call PrintUsage function
    
    if f1==1 or arg1=="help":
        PrintUsage(arg1)
    elif arg1=="add":
        try:
            arg2=sys.argv[2]
            arg3=sys.argv[3]
            Adding(arg2,arg3)
        except:
            print("Error: Missing tasks sting. Nothing added!")
    elif arg1=="del":
        try:
            arg2=sys.argv[2]
            Deleting(int(arg2))
        except:
            print("Error: Missing NUMBER for deleting tasks.")
    elif arg1=="ls":
        Content()
    elif arg1=="done":
        try:
            arg2=sys.argv[2]
            Completed(int(arg2))
        except:
            print("Error: Missing NUMBER for marking tasks as done.")
    elif arg1=="report":
        Reporting()

