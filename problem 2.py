
f = open('input.txt', "r")

line = f.readline()

l=''
while line:

    #print(line)
    l+="".join( line.splitlines())

    line = f.readline()
f.close()
print('length of seq.: ',len(l))
print('main DNA seq.: ',l)



a= l.translate(str.maketrans({'A': 'T', 'T': 'A','G':'C','C':'G'}))

print('translated one: ',a)
print('Reverse complement:')
print ('main output (reversed complement sequence): ',a[::-1])


#output

'''
length of seq.:  70
main DNA seq.:  ACTGTTGTTCGGTGATCATCAGTTGTACAACGTCCTAACAACATCACATGCAATGCTTATGATATTCTTC
translated one:  TGACAACAAGCCACTAGTAGTCAACATGTTGCAGGATTGTTGTAGTGTACGTTACGAATACTATAAGAAG
main output (reversed complement sequence):  GAAGAATATCATAAGCATTGCATGTGATGTTGTTAGGACGTTGTACAACTGATGATCACCGAACAACAGT

'''