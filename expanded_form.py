def expanded_form(num):
    snum = str(num)[::-1]
    i =1
    s =""
    for c in snum:
        print(int(c)*i)
        ex = int(c)*i
        if(ex != 0):
            s = str(ex) + " + " + s


        i *= 10

    print(s.rsplit('+', 1)[0].strip())
    return  s

expanded_form(12)
