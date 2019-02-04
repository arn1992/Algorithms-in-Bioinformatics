genetic_code = {'TTT': 'F ', 'CTT': 'L ', 'ATT': 'I ', 'GTT': 'V ',
                'TTC': 'F ', 'CTC': 'L ', 'ATC': 'I ', 'GTC': 'V ',
                'TTA': 'L ', 'CTA': 'L ', 'ATA': 'I ', 'GTA': 'V ',
                'TTG': 'L ', 'CTG': 'L ', 'ATG': 'M ', 'GTG': 'V ',
                'TCT': 'S ', 'CCT': 'P ', 'ACT': 'T ', 'GCT': 'A ',
                'TCC': 'S ', 'CCC': 'P ', 'ACC': 'T ', 'GCC': 'A ',
                'TCA': 'S ', 'CCA': 'P ', 'ACA': 'T ', 'GCA': 'A ',
                'TCG': 'S ', 'CCG': 'P ', 'ACG': 'T ', 'GCG': 'A ',
                'TAT': 'Y ', 'CAT': 'H ', 'AAT': 'N ', 'GAT': 'D ',
                'TAC': 'Y ', 'CAC': 'H ', 'AAC': 'N ', 'GAC': 'D ',
                'TAA': '* ', 'CAA': 'Q ', 'AAA': 'K ', 'GAA': 'E ',
                'TAG': '* ', 'CAG': 'Q ', 'AAG': 'K ', 'GAG': 'E ',
                'TGT': 'C ', 'CGT': 'R ', 'AGT': 'S ', 'GGT': 'G ',
                'TGC': 'C ', 'CGC': 'R ', 'AGC': 'S ', 'GGC': 'G ',
                'TGA': '* ', 'CGA': 'R ', 'AGA': 'R ', 'GGA': 'G ',
                'TGG': 'W ', 'CGG': 'R ', 'AGG': 'R ', 'GGG': 'G '}

##seq = "TTTCAATACTAGCATGACCAAAGTGGGAACCCCCTTACGTAGCATGACCCATATATATATATATA"



f = open('input.txt', "r")

line = f.readline()

l=''
while line:

    #print(line)
    l+="".join( line.splitlines())

    line = f.readline()
f.close()
print('DNA Sequence:',l)
print('All six reading frames:')
'''file=open('input.txt','r')
s=file.readline()'''


"5’3’ Frame 1"
def code2proten(orf, genetic_code):
    protein = ''
    for i in range(0, len(orf), 3):
        if len(orf) >= i+3:
         codon = orf[i:i + 3]
         protein +=genetic_code[codon]

        else:
            break

    return protein


#print(l)

'''file=open('input.txt','r')
s=file.readline()'''


f=code2proten(l, genetic_code)
print('5’3’ Frame 1: ',f)

"5’3’ Frame 2"
def code2proten1(orf, genetic_code):
    protein = ''
    for i in range(1, len(orf), 3):
        if len(orf) >= i+3:
         codon = orf[i:i + 3]
         protein +=genetic_code[codon]

        else:
            break

    return protein
f1=code2proten1(l, genetic_code)
print('5’3’ Frame 2: ',f1)

"5’3’ Frame 3"
def code2proten2(orf, genetic_code):
    protein = ''
    for i in range(2, len(orf), 3):
        if len(orf) >= i+3:
         codon = orf[i:i + 3]
         protein +=genetic_code[codon]

        else:
            break

    return protein
f2=code2proten2(l, genetic_code)
print('5’3’ Frame 3: ',f2)


"3’5’ Frame 1"
def code2proten3(orf, genetic_code):
    protein = ''
    a=orf[::-1]
    a1 = a.translate(str.maketrans({'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}))

    for i in range(0, len(a1), 3):
        if len(a) >= i+3:
         codon = a1[i:i + 3]
         protein +=genetic_code[codon]

        else:
            break

    return protein
f3=code2proten3(l, genetic_code)
print('3’5’ Frame 1: ',f3)


"3’5’ Frame 2"
def code2proten4(orf, genetic_code):
    protein = ''
    a=orf[::-1]
    a1 = a.translate(str.maketrans({'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}))

    for i in range(1, len(a1), 3):
        if len(a) >= i+3:
         codon = a1[i:i + 3]
         protein +=genetic_code[codon]

        else:
            break

    return protein
f4=code2proten4(l, genetic_code)
print('3’5’ Frame 2: ',f4)


"3’5’ Frame 3"
def code2proten5(orf, genetic_code):
    protein = ''
    a=orf[::-1]
    a1 = a.translate(str.maketrans({'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}))

    for i in range(2, len(a1), 3):
        if len(a) >= i+3:
         codon = a1[i:i + 3]
         protein +=genetic_code[codon]

        else:
            break

    return protein
f5=code2proten5(l, genetic_code)
print('3’5’ Frame 3: ',f5)



#Output
'''

DNA Sequence: ACTGTTGTTCGGTGATCATCAGTTGTACAACGTCCTAACAACATCACATGCAATGCTTATGATATTCTTC
5’3’ Frame 1:  T V V R * S S V V Q R P N N I T C N A Y D I L 
5’3’ Frame 2:  L L F G D H Q L Y N V L T T S H A M L M I F F 
5’3’ Frame 3:  C C S V I I S C T T S * Q H H M Q C L * Y S 
3’5’ Frame 1:  E E Y H K H C M * C C * D V V Q L M I T E Q Q 
3’5’ Frame 2:  K N I I S I A C D V V R T L Y N * * S P N N S 
3’5’ Frame 3:  R I S * A L H V M L L G R C T T D D H R T T 

'''