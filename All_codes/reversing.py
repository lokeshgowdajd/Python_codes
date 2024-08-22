"""def reversString(string):
    revers=" "

    rever_string=str(string)

    print(rever_string[::-1])
reversString("lokesh")    """

def reversString(string):
    revers=""

    string=str(string)

    for i in string:
        revers=i+revers

    print(revers)  
reversString("lokesh")      