def getInt(prompt,max,min=1):
    while 1:
        try:
            ret = int(input(prompt))
            if ret <= max and ret >=min:
                return ret
            else:
                print("invalid input")
        except:
            print("invalid input")
def getChoiceFromListOfNamedItems(prompt,list):
        i = 0
        for item in list:
            i+=1
            print(str(i) + ":" + item.name)
        attack = getInt(prompt,list.__len__())
        return list[attack-1]