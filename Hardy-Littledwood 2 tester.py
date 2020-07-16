import sympy

m = 0
n = 0

mSelect = [1,100,200,300,400,500]
nSelect = [100,200,300,400,500,600]

"""while m < 2:
    m = int(input("First number 'm':"))
while n <= m:
    n = int(input("Second number 'n':"))"""


for m in mSelect:
    n = nSelect[mSelect.index(m)]
    addset = []
    nset = []
    common = []

    for x in range(m+1, m+n+1):
        if sympy.isprime(x):
            addset.append(x)
    for x in range(2,n+1):
        if sympy.isprime(x):
            nset.append(x)

    for x in addset:
        if x in nset:
            common.append(x)

    if len(addset) <= len(nset):
        print("Conjecture true")

    print("m =", m, "n =", n)
    print("Common primes:" , common)
    print("Number of commons:", len(common))
    print("")
        
