a = "listen"
b = "silent"



def anagramm(a,b):
    a = a.lower()
    b = b.lower()
    a_NoSpace = a.replace(" ","")
    b_NoSpace = b.replace(" ","")

    a_splited = list(a_NoSpace)
    b_splited = list(b_NoSpace)

    return all(a_splited.count(x) == b_splited.count(x) for x in 'abcdefjhijklmnopqrstuvwxyz')

print(anagramm(a,b))

#dauert 16:39.27 ohne LLM