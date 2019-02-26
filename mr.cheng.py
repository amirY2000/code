'''
def factor(a,b,c):
    """
    this func will get the a,b,c and give us the root of bionomial
    """
    a = int(a)
    b = int(b)
    c = int(c)
    n = (b*c)
    s = b/a
    for i in range(1,2*n):
        for j in range(1,2*n):
            if (i+j) == s and (i*j) == c:
                a = str(a)
                i = str(i)
                j = str(j)
                return a + "x" + "+" + i + " "+a + "x" + "+"+j 
    return "no real roots"
def distribute(a,b,c,d):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    z = str(a*c)
    x = str((a*d)+(b*c))
    i = str(b*d)
    return z+"x^2"+"+"+" "+x+"x"+"+"+" "+i
def valid_choice(selection):
    if selection == "f" or selection == "d":
        return True
    return False
def valid_coef(a,b,c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        return True
    except ValueError:
        return False
def valid_coef_d(a,b,c,d):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    selection = input("Would you like to (f)actor or (d)istribute? ")
    while valid_choice(selection) == False:
        selection = input("Select a valid option: 'f' for factor and 'd' for distribute :")
    if selection == "f":
        a = input("what is a ? ")
        b = input("what is b ? ")
        c = input("what is c ? ")
        if valid_coef(a,b,c) == True:
            print(factor(a,b,c))
        else:
            print("One of your coefficients is not valid !!")
    if selection == "d":
        a = input("what is a ? ")
        b = input("what is b ? ")
        c = input("what is c ? ")
        d = input("what is d ? ")
        if valid_coef_d(a,b,c,d) == True:
            print(distribute(a,b,c,d))
        else:
            print("One of your coefficients is not valid !!")
'''
def advance_factor(a,b,c):
    if type(a) != str and type(b) != str and type(c) != str: 
        ac4 = (4*a)*c
        b2 = b**2
        delta = b2-ac4
        if delta < 0:
            return " There isn't any real root"
        elif delta == 0:
            delta = delta**0.5
            x = (-b+delta)/(2*a)
            return x
        else:
            delta = delta**0.5
            x1 = (-b+delta)/(2*a)
            x2 = (-b-delta)/(2*a)
            return x1 , x2
    else:
        return "One of your coefficients is not number!"
print(advance_factor(1,2,1))