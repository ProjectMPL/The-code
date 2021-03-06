import time

Variables = list(range(32714))
for _ in range(32714):
    Variables[_] = 0

latastdata = 0

FStatement = "test."

ValStatement = "val."
ValStatement2 = "value."

DataStatement = "data."

class test_functions():
    F1 = "testprint"
    F2 = "count_to("
    endB = ")"

    #test.testprint
    #test.count_to(NUM)

class value_functions():
    F1 = "set("
    F2 = "get("
    F3 = "add("
    F4 = "sub("
    F5 = "del_data("
    F6 = "sld("
    endB = ")"

    #val.add(BASE,ADD,STORE)
    #val.sub(BASE,SUB,STORE)
    #val.set(STORE,DATA)
    #val.get(BASE)

class data():
    F1 = "set("
    F2 = "read("
    F3 = "sld("
    endB = ")"

    #data.set(DATA,PATH)

def splitStr(string):
    previous_character = string[0]
    groups = []
    newword = string[0]
    for x, i in enumerate(string[1:]):
        if i.isalpha() and previous_character.isalpha():
            newword += i
        elif i.isnumeric() and previous_character.isnumeric():
            newword += i
        else:
            groups.append(newword)
            newword = i

        previous_character = i

        if x == len(string) - 2:
            groups.append(newword)
            newword = ''
    return groups

while True:
    line = input(">>> ")
    if line.startswith(FStatement):
        if test_functions.F1 in line:
            print("Hello World!")
        elif test_functions.F2 in line and line.endswith(test_functions.endB):
            split = splitStr(line)
            for i in range(int(split[6])):
                print(i+1)
        else:
            print("Function invalid")
    elif line.startswith(ValStatement) or line.startswith(ValStatement2):

        #data s/r done

        if value_functions.F1 in line and "," in line and line.endswith(value_functions.endB):
            var = splitStr(line)
            print("Value: "+var[4]+" set to: "+ var[6])
            Variables[int(var[4])] = int(var[6])
            latestdata = Variables[int(var[4])]
        elif value_functions.F2 in line and line.endswith(value_functions.endB):
            var = splitStr(line)
            print(Variables[int(var[4])])
            latestdata = Variables[int(var[4])]
        elif value_functions.F3 in line and line.endswith(value_functions.endB):
            var = splitStr(line)
            Variables[int(var[8])] = Variables[int(var[4])] + Variables[int(var[6])]
            print("set value:"+str(var[8])+" to:"+ str(Variables[int(var[8])]))
            latestdata = Variables[int(var[8])]
        elif value_functions.F4 in line and line.endswith(value_functions.endB):
            var = splitStr(line)
            Variables[int(var[8])] = Variables[int(var[4])] - Variables[int(var[6])]
            print("set value:"+str(var[8])+" to:"+ str(Variables[int(var[8])]))
            latestdata = Variables[int(var[8])]
        elif value_functions.F5 in line and line.endswith(value_functions.endB):
            var = splitStr(line)
            
            print("Data of value:"+var[6]+ " Succesfully deleted ("+ str(Variables[int(var[6])])+")")
            Variables[int(var[6])] = 0
        elif value_functions.F6 in line and line.endswith(value_functions.endB):
            var = splitStr(line)
            Variables[int(var[4])] = latestdata
            print("Data of value:"+var[4]+ " Succesfully set to latest ("+ str(latestdata)+")")
        else:
            print("Function invalid")

    elif line.startswith(DataStatement):
        if data.F1 in line and line.endswith(data.endB):
            var = splitStr(line)
            file = open("Data/save_"+str(var[6])+".txt","w+")
            print("Saved data:"+str(var[4])+" to:"+ str(var[6]))
            file.write(var[4])
            file.close() 
        elif data.F2 in line and line.endswith(data.endB):
            var = splitStr(line)
            file = open("Data/save_"+str(var[4])+".txt","r")
            data1 = file.read()
            print(data1)
            latestdata = data1
            file.close()
        elif data.F3 in line and line.endswith(data.endB):
            var = splitStr(line)
            print("Data:"+var[4]+ " Succesfully set to latest ("+ str(latestdata)+")")
            file = open("Data/save_"+str(var[4])+".txt","w+")
            data1 = file.write(str(latestdata))
            file.close()
    else:
        print("Function invalid")
    time.sleep(0.1)
