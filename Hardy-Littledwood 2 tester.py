import sympy

m = 0
n = 0

while m < 2:
    m = int(input("First number 'm':"))
while n <= m:
    n = int(input("Second number 'n':"))

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

print("Common primes:" , common)
print("Number of commons:", len(common))
        
