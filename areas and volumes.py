print("area and volume")
shape = str(input("shape :"))
if(shape == "cube"):
    b = int(input("side :"))
    a = 4*b*b                       
    c = 6*b*b                                     
    d = b*b*b                                       
    temp = f"curved surface area: {a}"
    print(temp)
    nikhil = f"total surface area: {c}"
    print(nikhil)
    v = f"volume: {d}"
    print(v)
elif(shape == "cuboid"):
    b = float(input("length :"))
    a = float(input("bradth :"))                     
    c = float(input("height :"))
    d = 2*c*b+2*c*a
    e = 2*b*a+2*a*c+2*c*b
    f = a*b*c
    temp = f"curved surface area: {d}"
    print(temp)
    nikhil = f"total surface area: {e}"
    print(nikhil)
    v = f"volume: {f}"
    print(v)
elif(shape == "cone"):
    b = float(input("radius :"))
    c = int(input("height :"))
    a = float(input("slant height :"))
    d = 22/7*b*a
    e = 22/7*b*a+22/7*b*b
    f = 1/3*22/7*b*b*c
    temp = f"curved surface area: {d}"
    print(temp)
    nikhil = f"total surface area: {e}"
    print(nikhil)
    v = f"volume:  {f}"
    print(v)
elif(shape == "cylinder"):
    b = float(input("radius :"))
    c = float(input("height :"))
    d = 2*22/7*b*c
    e = 2*22/7*b*c+2*22/7*b*b
    f = 22/7*b*b*c
    temp = f"curved surface area: {d}"
    print(temp)
    nikhil = f"total surface area: {e}"
    print(nikhil)
    v = f"volume: {f}"
    print(v)
elif(shape =="sphere"):
    b = float(input("radius :"))
    d = 4*22/7*b*b
    e = 4*22/7*b*b
    f = 4/3*22/7*b*b*b
    temp = f"curved surface area: {d}"
    print(temp)
    nikhil = f"total surface area: {e}"
    print(nikhil)
    v = f"volume: {f}"
    print(v)
elif(shape == "hemisphere"):
    b = float(input("radius :"))
    d = 2*22/7*b*b
    e = 3*22/7*b*b
    f = 2/3*22/7*b*b*b
    temp = f"curved surface area: {d}"
    print(temp)
    nikhil = f"total surface area: {e}"
    print(nikhil)
    v = f"volume: {f}"
    print(v)
else:
    print("syntax error")



