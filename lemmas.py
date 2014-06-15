# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE


################################### POSITIVE ######################################

f = open("positive.tbl", "r")
w = open("positive.txt", "w")


line = f.readline()
line = f.readline()

pos1 = set()
pos2 = set()

#1
s = ""
while line[0] != "#":
    s += " " + line.strip() + " "
    line = f.readline()


s2 = s.encode('utf-8')
p = Popen(["pfe/bin/t3mesta", "-path", "pfe/data/t3mesta"], stdout=PIPE, stdin=PIPE)
stdout = p.communicate(s2)[0]
phrase = stdout.decode("utf-8")

parts = phrase.split("\n")

last = False
for line in parts:
    if line[-2:] == "//":
        if not last:
            last = True
            lemma = line.split("+")[0]
            pos1.add(lemma.strip())
    else:
        last = False

w.write("#1 keskmiselt positiivsed +2\n")
for lemma in sorted(pos1):
    w.write(lemma + "\n")


#2
s = ""
line = f.readline()
while line:
    s += " " + line.strip() + " "
    line = f.readline()

s2 = s.encode('utf-8')
p = Popen(["pfe/bin/t3mesta", "-path", "pfe/data/t3mesta"], stdout=PIPE, stdin=PIPE)
stdout = p.communicate(s2)[0]
phrase = stdout.decode("utf-8")

parts = phrase.split("\n")

last = False
for line in parts:
    if line[-2:] == "//":
        if not last:
            last = True
            lemma = line.split("+")[0]
            pos2.add(lemma.strip())
    else:
        last = False

w.write("#3 tugevalt positiivsed +4\n")
for lemma in sorted(pos2):
    w.write(lemma + "\n")

w.close()
f.close()



################################### NEGATIVE ######################################

f = open("negative.tbl", "r")
w = open("negative.txt", "w")


line = f.readline()
line = f.readline()

pos1 = set()
pos2 = set()

#1
s = ""
while line[0] != "#":
    s += " " + line.strip() + " "
    line = f.readline()


s2 = s.encode('utf-8')
p = Popen(["pfe/bin/t3mesta", "-path", "pfe/data/t3mesta"], stdout=PIPE, stdin=PIPE)
stdout = p.communicate(s2)[0]
phrase = stdout.decode("utf-8")

parts = phrase.split("\n")

last = False
for line in parts:
    if line[-2:] == "//":
        if not last:
            last = True
            lemma = line.split("+")[0]
            pos1.add(lemma.strip())
    else:
        last = False

w.write("#1 keskmiselt negatiivsed +2\n")
for lemma in sorted(pos1):
    w.write(lemma + "\n")


#2
s = ""
line = f.readline()
while line:
    s += " " + line.strip() + " "
    line = f.readline()

s2 = s.encode('utf-8')
p = Popen(["pfe/bin/t3mesta", "-path", "pfe/data/t3mesta"], stdout=PIPE, stdin=PIPE)
stdout = p.communicate(s2)[0]
phrase = stdout.decode("utf-8")

parts = phrase.split("\n")

last = False
for line in parts:
    if line[-2:] == "//":
        if not last:
            last = True
            lemma = line.split("+")[0]
            pos2.add(lemma.strip())
    else:
        last = False

w.write("#3 tugevalt negatiivsed +4\n")
for lemma in sorted(pos2):
    w.write(lemma + "\n")

w.close()
f.close()




################################### ADDITIONAL ######################################

f = open("additional.tbl", "r")
w = open("additional.txt", "w")


line = f.readline()
line = f.readline()

pos1 = set()
pos2 = set()

#1
s = ""
while line[0] != "#":
    s += " " + line.strip() + " "
    line = f.readline()


s2 = s.encode('utf-8')
p = Popen(["pfe/bin/t3mesta", "-path", "pfe/data/t3mesta"], stdout=PIPE, stdin=PIPE)
stdout = p.communicate(s2)[0]
phrase = stdout.decode("utf-8")

parts = phrase.split("\n")

last = False
for line in parts:
    if line[-2:] == "//":
        if not last:
            last = True
            lemma = line.split("+")[0]
            pos1.add(lemma.strip())
    else:
        last = False

#w.write("#1 keskmiselt positiivsed +2\n")
w.write("#1 eitus")
for lemma in sorted(pos1):
    w.write(lemma + "\n")


#2
pos3 = set()
s = ""
line = f.readline()
while line[0] != "#":
    s += " " + line.strip() + " "
    line = f.readline()

s2 = s.encode('utf-8')
p = Popen(["pfe/bin/t3mesta", "-path", "pfe/data/t3mesta"], stdout=PIPE, stdin=PIPE)
stdout = p.communicate(s2)[0]
phrase = stdout.decode("utf-8")

parts = phrase.split("\n")

last = False
for line in parts:
    if line[-2:] == "//":
        if not last:
            last = True
            lemma = line.split("+")[0]
            pos3.add(lemma.strip())
    else:
        last = False

w.write("#2 laengu vähendajad\n")
for lemma in sorted(pos3):
    w.write(lemma + "\n")


#3
s = ""
line = f.readline()
while line:
    s += " " + line.strip() + " "
    line = f.readline()

s2 = s.encode('utf-8')
p = Popen(["pfe/bin/t3mesta", "-path", "pfe/data/t3mesta"], stdout=PIPE, stdin=PIPE)
stdout = p.communicate(s2)[0]
phrase = stdout.decode("utf-8")

parts = phrase.split("\n")

last = False
for line in parts:
    if line[-2:] == "//":
        if not last:
            last = True
            lemma = line.split("+")[0]
            pos2.add(lemma.strip())
    else:
        last = False

w.write("#3 laengu suurendajad\n")
for lemma in sorted(pos2):
    w.write(lemma + "\n")

w.close()
f.close()
  
