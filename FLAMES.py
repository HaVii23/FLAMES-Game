def nameProcessing():
    name1 = "NATARAJAN"
    name2 = "DHANAM"
    cut = 0
    totNameLen = len(name1) + len (name2)
    for a in name1:
        for b in name2:
            if (a==b):
                name2=name2.replace(b,'',1)
                cut +=1
    flamesCount = totNameLen - (cut*2)
    return flamesCount

def flameFinder():
    flames = ("Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings")
    a = 2
    b = 0
    j = 1
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
                    a += 1
            b = 0
        j+=1
    return flames

flameStatus = flameFinder()
print("Predicted Relationship :",*flameStatus)
