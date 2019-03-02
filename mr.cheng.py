def factor(a,b,c):
    """
    this func will get the a,b,c and give us the root of bionomial
    """
    a = int(a)
    b = int(b)
    c = int(c)
    ac4 = (4*a)*c
    b2 = b**2
    delta = b2-ac4
    if delta < 0:
        return " There isn't any real root"
    elif delta == 0:
        delta = delta**0.5
        x = (-b+delta)/(2*a)
        if x < 0 :
            b = -(a*x)
        else:
            b = (a*x)
        b = str(b)
        a = str(a)
        print("zero : ",x)
        if x < 0:
            return "("+a+"x"+"+"+b+")"+"^2"
        else:
            return "("+a+"x"+"-"+b+")"+"^2"
    else:
        delta = delta**0.5
        x1 = (-b+delta)/(2*a)
        x2 = (-b-delta)/(2*a)
        if x1 < 0:
            b = -(a*x1)
        else:
            b = (a*x1)
        if x2 < 0 :
            c = -(a*x2)
        else:
            c = (a*x2)
        e = a
        n =int(b*c)
        if n<0:
            n *= -1
        for i in range(n,0,-1):
            if a%i == 0 and b % i == 0:
                a /= i
                b /= i
            if e%i ==0 and c%i == 0:
                e /= i
                c /= i        
        a = str(a)
        b = str(b)
        c = str(c)
        e = str(e)
        if x1 < 0 and x2 > 0:
            print("zeroes : ",x1,",",x2)
            return "("+a+"x"+"+"+b+")"+"("+e+"x"+"-"+c+")"
        elif x1 > 0 and x2 < 0:
            print("zeroes : ",x1,",",x2)
            return "("+a+"x"+"-"+b+")"+"("+e+"x"+"+"+c+")"
        elif x1 > 0 and x2 > 0:
            print("zeroes : ",x1,",",x2)
            return "("+a+"x"+"-"+b+")"+"("+e+"x"+"-"+c+")"
        else:
            print("zeroes : ",x1,",",x2)
            return "("+a+"x"+"+"+b+")"+"("+e+"x"+"+"+c+")"
    
def distribute(a,b,c,d):
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    z = str(a*c)
    x = str((a*d)+(b*c))
    i = str(b*d)
    return z+"x^2"+"+"+"("+x+"x"+")"+"+"+"("+i+")"

def valid_choice(selection):
    if selection == "f" or selection == "d" or selection == "a":
        return True
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
def valid_coef_a(a,b,c):
    try:
        a = int(a)
        b = int(b)
        c = int(c)
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
        if valid_coef_a(a,b,c) == True:
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
def factoor(x):
    factor = []
    for i in range(1,x+1):
        if x % i == 0:
            factor.append(i,x//i)
    return factor
def factor_polynomial(a,b,c):
    factor_a = factoor(a) 
    factor_c = factoor(c)
    for p in factor_a:
        e = p[0]
        f = p[1]
        for p2 in factor_c:
            g = p2[0]
            h = p2[1]
            if (e*h)+(p*g) == b:
                return "("+e+"x"+"+"+"("+h+"+"+")"+")"+"("+f+"x"+"+"+"("+g+"+"+")"+")"
'''