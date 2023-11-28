while True:
    try:
        s = input()
        l = 0
        u = 0
        n = 0
        space = 0

        for t in s:
            c = ord(t)
            if(ord('a')<=c and ord('z')>=c):
                l+=1
            elif(ord('A') <= c and ord('Z') >= c):
                u+=1
            elif(ord('0')<= c and ord('9')>=c):
                n+=1
            if(t==' '):
                space+=1
        
        print(l,u,n,space)

    except EOFError:
        break