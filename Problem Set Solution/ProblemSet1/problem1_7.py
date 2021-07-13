def problem1_7():
    b1 = float(input("Enter the length of one of the bases: "))
    b2 = float(input("Enter the length of the other base: "))
    h = float(input("Enter the height: "))
    A = 0.5*(b1+b2)*h
    print("The area of a trapezoid with bases "+str(b1)+" and "+str(b2)+" and height "+str(h)+" is "+str(A))