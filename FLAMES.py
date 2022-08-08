name1 = "NATARAJAN"
name2 = "DHANAM"
flames = "FLAMES"
j = 1
cut = 0
totNameLen = len(name1) + len (name2)
for a in name1:
    for b in name2:
        if (a==b):
            name2=name2.replace(b,'',1)
            cut +=1
flameCutCount = totNameLen - (cut*2)
a = 2
b = 0
while(j<6):
    print(j)
    if(len(flames) != 1):
        for i in flames*a:
            b += 1 
            if(b == flameCutCount):
                Ind = flames.index(i)
                flames = flames.replace(i,"",1)
                flames = flames[Ind:] + flames [:Ind]
                a += 1
                print("FLAMES :",flames)
        b = 0
    j+=1

