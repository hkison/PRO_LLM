string = "swiss"

def first_not_doubled_alphabet(string) :
    string_noSpace = string.replace(" ","")
    count = {}
    for i in string_noSpace :
        try: count[i] += 1
        except: count[i] = 1
    for k,v in count.items():
        if v == 1:
            return k
    return -1

print(first_not_doubled_alphabet(string))

#dauert 6:49.41
