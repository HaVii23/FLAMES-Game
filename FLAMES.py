def nameProcessing():
    name1 = input('Enter First Name  : ');    name1 = name1.upper().replace(' ','')
    name2 = input('Enter Second Name : ');    name2 = name2.upper().replace(' ','')
    cut = 0
    totNameLen = len(name1) + len (name2)
    print(name1,name2)
    for a in name1:
        for b in name2:
            if (a==b):
                name2=name2.replace(b,'',1)
                cut +=1
                print(b)
                break
    flamesCount = totNameLen - (cut*2)
    print(flamesCount)
    return flamesCount

def flameFinder():
    flames = ("FRIENDS", "LOVE", "AFFECTION", "MARRIAGE", "ENEMY", "SIBLINGS")
    a = 10;    b = 0;    j = 1
    flamesCutCount = nameProcessing()
    while(j<6):
        if(len(flames) != 1):
            for i in flames*a:
                b += 1 
                if(b == flamesCutCount):
                    Ind = flames.index(i)
                    flameList = list(flames)
                    flameList.remove(i)
                    flames= tuple(flameList)
                    flames = flames[Ind:] + flames [:Ind]
                    print(flames)
                    a += 1
            b = 0
        j+=1
    return flames

print("====================================***START***======================================\n")
flameStatus = flameFinder()
print("\nPredicted Relationship >>>",*flameStatus)

print("\n=====================================***END***=======================================")
