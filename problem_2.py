print("Name: Md. Aminur Rab Ratul; ID: 300086571")
print('Counting total number of possible alignments: ')

#take input
n=int(input("Enter a value for n: "))
m=int(input("Enter a value for m: "))
k= min(n,m) #minimum of two numbers
alignments=0

#function for factorial
def factorial(f):
    i=1
    product=1
    while i<=f:
        product = product*i
        i=i+1
    return product


#function for binomial coefficient
def binomial_coefficient(a,b):
    t = factorial(a) / (factorial(b) * factorial(a - b))
    return t


#loop for number of alignments counting
for i in range (0,k+1):

    alignments = alignments+ (2**i)*binomial_coefficient(m,i)*binomial_coefficient(n,i)



print('alignments: ',int(alignments))

