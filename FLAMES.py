""" 
    FLAMES GAME

Author  : Hari Vignesh A 
E-mail  : harivignesh201@gmail.com
Created : 08/08/2022 - 23:21

"""
import sys
import os
os.system('cls')
START   ="=====================================***START***======================================"
END     ="======================================***END***======================================="

def nameProcessing():
    name1 = input('Enter First Name  : ');    name1 = name1.upper().replace(' ','')
    name2 = input('Enter Second Name : ');    name2 = name2.upper().replace(' ','')
    if (name1 == name2):
        print("\nSame Name DON\'T HAVE FLAMES😒\n")
        print(END,'\n');    sys.exit()
    else:
        if (name1.isalpha() ==True and name2.isalpha()== True):
            cut = 0
            totNameLen = len(name1) + len (name2)
            for a in name1:
                for b in name2:
                    if (a==b):
                        name2=name2.replace(b,'',1)
                        cut +=1
                        break
            flamesCount = totNameLen - (cut*2)
            return flamesCount
        else:
            print("\nASAP Rename your Name with \"ONLY ALPHABETS\"🤯..!!!\n\n")
            print(END,'\n');    sys.exit();     

def flameFinder():
    flames = ("FRIENDS👫👭👬", "LOVE👩‍❤️‍👨👩‍❤️‍👩👨‍❤️‍👨", "AFFECTION🥰", "MARRIAGE💍❣️", "ENEMY😠", "SIBLINGS😍")
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
                    a += 1
            b = 0
        j+=1
    return flames

print(START,'\n')
flameStatus = flameFinder()
print("\nPredicted Relationship >>>",*flameStatus)
print(END,'\n')

