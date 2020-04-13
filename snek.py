

#SnekLang

#its just python BUT with prettier words

"""

noms function-name(thing):
    snek?  :

    snek??

    snek???

    HISS!()



OR

[0,1,2,3,4,5,6,7,8,9]

> - move to the right
< - move to the left
+ - increment the box
- - decrement the box


snneeeeeeeeeekkkkkkkkkkkkkkkkkkkkkkkkkkkk!

! print out the character 0-25
snek! -> a
snnek! -> b
sneeek! ->
snek! -> s
snnek! -> t
"""

def screamInfinitely():
    print("HISS")
    screamInfinitely()

def speakSnek(num):
    #chr(97) -> a
    return chr(num+97+18)

def uhhhhSnek(state, snek):
    s = 0;
    n = 0;
    e = 0;
    k = 0;



    for c in snek :
        if(c == 's'):
            s += 1;
        elif( c == 'n'):
            n += 1;
        elif( c == 'e'):
            e += 1;
        elif( c == 'k'):
            k += 1;
        elif( c != '\n'):
            screamInfinitely()

    state[k-s % len(state)] += n-e;

    return(speakSnek(state[k-s % len(state)]))


# takes in a string that is in SnekLang(tm)
def snekify(program):
    state = [0,0,0,0,0,0,0,0]

    #count all the s's
    #count all the n's
    #count all the e's
    #count all the k's

    sneks = program.split('!')
    sneks.pop()

    #print(sneks)

    snekout = ''

    for snek in sneks:
        snekout += uhhhhSnek(state, snek)

    return snekout


#snekify("snek!sneeeeeekk!sneeeeeeeeeeeeeeeeeeekkk!sneeeeeeeeekkkk!sneeeeeeeeeeeeeeekkkkk!")

#main.snek

name = input("write the name of the .snek file you want to parse\n")

file = open(name)
#print(file.read().strip())
print(snekify(file.read().strip()))
