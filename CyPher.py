def Caesar(message,key):
    output = ""
    if not (i <= 126 for i in message) and (i >= 33 for i in message):
        print("Just Strings Allowed") 
        return
    try:
        int(key)
    except:
        print("Key is not a number")
        return
    else:
        b = int(key)
    for i in range(len(message)):
        a = ord(message[i])
        if((a + b) > 126):
            output += chr((a + b)-94)
        else:
            output += chr(a + b)
    return output
def Main():
    a = input("Give a message: ")
    b = input("Give a key as a number: ")
    c = Caesar(a,b)
    print("Caesar Text:",c)
Main()
