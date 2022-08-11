n = int(input())
w = len(str(bin(n).replace('0b','')))
for i in range(1,n+1):
    deci = str(i).rjust(w,' ')
    binary = bin(i).replace('0b','').rjust(w,' ')
    octal = oct(i).replace('0o','').rjust(w,' ')
    Hexa = hex(i).replace('0x','').upper().rjust(w,' ')
    print(deci,octal,Hexa,binary)