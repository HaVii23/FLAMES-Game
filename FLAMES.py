name1 = "NATARAJAN"
name2 = name2Alt= "DHANAM"
flames = "FLAMES"
totNameLen = len(name1) + len (name2)
cut = 0
for a in name1:
    for b in name2Alt:
        if (a==b):
            name2Alt=name2Alt.replace(b,'',1)
            cut +=1
#---------------2----------------
flameCutCount = totNameLen - (cut*2)
print(flameCutCount)
b = 0
a = 2
j = 1

while(j<6):
    print(j)
    if(len(flames) != 1):
        for i in flames*a:
            b += 1 
            print(i)
            if(b == flameCutCount):
                Ind = flames.index(i)
                flames = flames.replace(i,"",1)
                # print("FLAMES : ",flames)
                flames = flames[Ind:] + flames [:Ind]
                # print("Altered FLAMES :", flames )
                a += 1
        b = 0
    j+=1

