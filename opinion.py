# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
import random

p = open("positive.txt", "r")
n = open("negative.txt", "r")
a = open("additional.txt", "r")

pos1 = set()
pos2 = set()

neg1 = set()
neg2 = set()

add1 = set()
add2 = set()
add3 = set()

line = p.readline()
line = p.readline()
while line[0] != "#":
    pos1.add(line.strip())
    line = p.readline()
line = p.readline()
while line:
    pos2.add(line.strip())
    line = p.readline()
p.close()

line = n.readline()
line = n.readline()
while line[0] != "#":
    neg1.add(line.strip())
    line = n.readline()
line = n.readline()
while line:
    neg2.add(line.strip())
    line = n.readline()
n.close()

line = a.readline()
line = a.readline()
while line[0] != "#":
    add1.add(line.strip())
    line = a.readline()
line = a.readline()
while line[0] != "#":
    add2.add(line.strip())
    line = a.readline()
line = a.readline()
while line:
    add3.add(line.strip())
    line = a.readline()
a.close()

t3mesta = "pfe/bin/t3mesta"
dictpath = "pfe/data/t3mesta"
print("\nLIHTNE EESTI KEELE MEELESTATUSE ANALÜÜSI TÖÖRIIST\n")
print("Vaikimisi t3mesta asukoht: ", t3mesta)
print("Vaikimisi t3mesta sõnastike asukoht: ", dictpath)

while True:
    choice = input("\n1 - Lisa sõnu sõnaraamatusse\n"
                   "2 - Arvuta meelestatuse skoore\n"
                   "3 - Muuda t3mesta asukohta\n"
                   "4 - Muuda t3mesta sõnastike asukohta\n"
                   "5 - Välju\n")
    if choice == '1':
        while True:
            which = input("\n1 - Keskmine positiivne meelestatus (hea, tore)"
                          "\n2 - Tugev positiivne meelestatus (parim, suurepärane)"
                          "\n3 - Keskmine negatiivne meelestatus (nõme, halb)"
                          "\n4 - Tugev negatiivne meelestatud (jäle, õudne)"
                          "\n5 - Eitavad sõnad (väga, täiega)"
                          "\n6 - Vähendavad sõnad (üpris, üsna)"
                          "\n7 - Tugevdavad sõnad (ei, mitte)"
                          "\nT - Tagasi\n")
            if which.lower() not in "1234567t":
                print("Vali väärtus vahemikust 1-8!")
                continue
            if which.lower() == 't':
                break
            addword = input("Sisesta sõna:\n")
            addword = addword.strip().lower()
            s2 = addword.encode('utf-8')
            p = Popen([t3mesta, "-path", dictpath], stdout=PIPE, stdin=PIPE)
            stdout = p.communicate(s2)[0]
            s3 = stdout.decode("utf-8")
            parts = s3.split("\n")
            for line in parts:
                if line[-2:] == "//":
                    addword = line.split("+")[0].strip()
            if which == '1':
                pos1.add(addword)
            elif which == '2':
                pos2.add(addword)
            elif which == '3':
                neg1.add(addword)
            elif which == '4':
                neg2.add(addword)
            elif which == '5':
                add1.add(addword)
            elif which == '6':
                add2.add(addword)
            else:
                add3.add(addword)
        continue
    elif choice == '2':
        answers = dict()
        answers[0] = ["Ei suuda otsustada?", "Üsna erapooletu..", "Äkki proovid olla natuke konkreetsem?"]
        answers[1] = ["Pole paha", "Pigem positiivne"]
        answers[2] = ["Keegi on täna heas tujus..", "Ära muretse, kõik hea möödub.", "Päris eufooriline"]
        answers[3] = ["Võiks olla parem?", "Pigem negatiivne"]
        answers[4] = ["Päris kriitiline, või mis?", "Wow, kui kuri!", "Üsna depressiivne.."]

        print("\nT - tagasi")
        s = input("Sinu arvamus:\n")
        finish = False
        while s:
            if s.lower() == 't':
                break
            opinion = 0
            phrases = []
            s2 = s.encode('utf-8')
            p = Popen([t3mesta, "-path", dictpath], stdout=PIPE, stdin=PIPE)
            stdout = p.communicate(s2)[0]
            phrase = stdout.decode("utf-8")
            parts = phrase.split("\n")
            phrases2 = []
            words2 = []
            
            last = False
            words = []
            for line in parts:
                if line[-2:] == "//":
                    if not last:
                        last = True
                        lemma = line.split("+")[0]
                        lemma = lemma.strip().lower()
                        words2.append(lemma)
                        #lemmas.append(lemma.strip())
                        if lemma in pos1:
                            words.append(1)
                        elif lemma in pos2:
                            words.append(2)
                        elif lemma in neg1:
                            words.append(3)
                        elif lemma in neg2:
                            words.append(4)
                        elif lemma in add1:
                            words.append(5)
                        elif lemma in add2:
                            words.append(6)
                        elif lemma in add3:
                            words.append(7)
                        else:
                            words.append(0)
                        if finish:
                            phrases.append(words)
                            phrases2.append(words2)
                            words2 = []
                            words = []
                            finish = False
                else:
                    last = False
                    if len(line)>0 and line[-1] in ".,:;!?":
                        finish = True
            phrases.append(words)
            phrases2.append(words2)

            #print(phrases)
            #print(phrases2)

            scores = {1:2, 2:4, 3:-2, 4:-4}

            opinions = []
            for m in range(0, len(phrases)):
                phrase = phrases[m]
                ops = []
                for i in range(0, len(phrase)):
                    if phrase[i] in [1,2,3,4]:
                        ops.append(i)
                if ops:
                    breaks = [0]
                    for i in range(1, len(ops)):
                        breaks.append((ops[i]+ops[i-1])//2)
                    breaks.append(len(ops))
                    for i in range(1, len(breaks)):
                        opinion = scores[phrase[ops[i-1]]]
                        s = phrases2[m][ops[i-1]] + ": "
                        if opinion> 0:
                            s += "+"
                        s += str(opinion)
                        if sum(phrase[breaks[i-1]:breaks[i]]) == phrase[ops[i-1]]:
                            opinions.append(opinion)
                            if opinion > 0:
                                opp = "+" + str(opinion)
                            else:
                                opp = opinion
                            print(opp, " - ", s)
                            continue
                        j = ops[i-1]
                        k = ops[i-1]
                        while j>breaks[i-1] or k<breaks[i]-1:
                            if j>breaks[i-1]:
                                j -= 1
                                if phrase[j] == 5:
                                    s += ", " + phrases2[m][j] +" => "
                                    if opinion>0:
                                        opinion = -2
                                        s += str(opinion)
                                    else:
                                        opinion = 2
                                        s += "+" + str(opinion)
                                elif phrase[j] == 6:
                                    if opinion > 0:
                                        opinion -= 1
                                        s += ", " + phrases2[m][j] +": -1"
                                    if opinion < 0:
                                        opinion += 1
                                        s += ", " + phrases2[m][j] +": +1"    
                                elif phrase[j] == 7:
                                    if opinion > 0:
                                        opinion += 1
                                        s += ", " + phrases2[m][j] +": +1"
                                    if opinion < 0:
                                        opinion -= 1
                                        s += ", " + phrases2[m][j] +": -1" 
                            if k<breaks[i]-1:
                                k += 1
                                if phrase[k] == 5:
                                    s += ", " + phrases2[m][k] +" => "
                                    if opinion>0:
                                        opinion = -2
                                        s += str(opinion)
                                    else:
                                        opinion = 2
                                        s += "+" + str(opinion)
                                elif phrase[k] == 6:
                                    if opinion > 0:
                                        opinion -= 1
                                        s += ", " + phrases2[m][k] +": -1"
                                    if opinion < 0:
                                        opinion += 1
                                        s += ", " + phrases2[m][k] +": +1"    
                                elif phrase[k] == 7:
                                    if opinion > 0:
                                        opinion += 1
                                        s += ", " + phrases2[m][k] +": +1"
                                    if opinion < 0:
                                        opinion -= 1
                                        s += ", " + phrases2[m][k] +": -1" 
                        opinions.append(opinion)
                        if opinion > 0:
                            opp = "+" + str(opinion)
                        else:
                            opp = opinion
                        print(opp, " - ", s)
                                                   
                        
                    a = 0
                    b = len(phrase)
                    if len(ops)==1:
                        k = -1
                        j = ops[0]
                    else:
                        breaks = [0, len(ops)]
                        for i in range(1, len(ops)):
                            breaks
                        
                        
                    
            #print(phrases)
            #print(phrases2)
                
            #print(opinions)
            print("Üldine arvamus: ", sum(opinions))
            opinion = sum(opinions)
            if opinion == 0:
                print(random.choice(answers[0]))
            elif opinion > 0 and opinion < 5:
                print(random.choice(answers[1]))
            elif opinion > 0:
                print(random.choice(answers[2]))
            elif opinion < 0 and opinion > -5:
                print(random.choice(answers[3]))
            else:
                print(random.choice(answers[4]))

            print("\nT - tagasi")
            s = input("Sinu arvamus:\n")
    elif choice == '3':
        t3mesta = input("T3mesta asukoht:\n")
    elif choice == '4':
        dictpath = input("T3mesta sõnaraamatute asukoht:\n")
    elif choice == '5':
        w1 = open("positive.txt", "w")
        w2 = open("negative.txt", "w")
        w3 = open("additional.txt", "w")
        w1.write("#1 keskmiselt positiivsed +2\n")
        for lemma in sorted(pos1):
            w1.write(lemma + "\n")
        w1.write("#3 tugevalt positiivsed +4\n")
        for lemma in sorted(pos2):
            w1.write(lemma + "\n")
        w2.write("#1 keskmiselt negatiivsed -2\n")
        for lemma in sorted(neg1):
            w2.write(lemma + "\n")
        w2.write("#3 tugevalt negatiivsed -4\n")
        for lemma in sorted(neg2):
            w2.write(lemma + "\n")
        w3.write("#1 eitus")
        for lemma in sorted(add1):
            w3.write(lemma + "\n")
        w3.write("#2 laengu vähendajad\n")
        for lemma in sorted(add2):
            w3.write(lemma + "\n")
        w3.write("#3 laengu suurendajad\n")
        for lemma in sorted(add3):
            w3.write(lemma + "\n")
        w1.close()
        w2.close()
        w3.close()        
        break
    else:
        print("Vali väärtus vahemikust 1-5!")

    

        
