'''
num = [1, 2, 3, 200, True, []]
if 200 in num:
    num.insert(num.index(200),"-")
    num.remove(200)
print(num)

import turtle
turtle.forward(100)
turtle.left(1200)

dr_fr = {"январь": [["name","data"]["name","data"]]}
'''
def dict_append_sentence():
    a = ""
    c = []
    d = 0
    while a != "stop":
        d +=1
        a = input(f"world {d}, write stop to stop: ")
        c.append(a)
        if d >= 30:
            print("30 слов хватит")
            break
    try:
        c.remove("stop")
    finally:
        print()
    sl = {}
    h = len(c)
    y = 0
    for i in range (0,h):
    #dict.fromkeys(c)
    #.update(c[i]: str(c.count(c[i])))
    #sl = {c[i]: c.count(c[i]) for k in range(0, h)}
        sl[c[i]] = c.count(c[i])
    print(sl)
    return sl
    

aa = input("write start to start text_analisator")
if aa == "start":
    print(dict_append_sentence())
    input()

'''
s = {}


#s = "hello world"

#s = c.split(", ")


sl = dict.fromkeys(c)
sl = {c[0]: str(c.count(c[0])), c[1]: str(c.count(c[1]))}
print(sl)
'''

