import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    l=[]
    for x in range(10):
        l.append(random.random()*5+30)
    print(l)