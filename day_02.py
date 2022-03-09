names = ["jimmy", "tonny", "vinnie"]
print(names[1])

first_name = "fred"
print(first_name[1])
for name in names:
    print(name)


name = names[2]

if name is not "vinnie":
    print("you are not vinnie!!")
else:
    print("hey vinnie!!")


for num in range(10, 20, 2):
    if num == 14:
        #break
        continue
    print(num)

def this_does_nothing():
    pass


def greeting(param1=0, param2=0, param3=0, name="anon"):
    match name:
        case "jimmy":
            print ("hey whats up! " + name)
        case "tonny":
            print ("whats going on! " + name)
        case "vinnie":
            print ("whats that! " + name)
        

greeting(name=names[0])