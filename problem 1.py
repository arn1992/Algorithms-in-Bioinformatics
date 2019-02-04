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
a=l.replace('T','U')
print('Transcription:')
print('main output (converted one from T to U): ',a)


#output

'''
length of seq.:  70
main DNA seq.:  ACTGTTGTTCGGTGATCATCAGTTGTACAACGTCCTAACAACATCACATGCAATGCTTATGATATTCTTC
main output (converted one from T to U):  ACUGUUGUUCGGUGAUCAUCAGUUGUACAACGUCCUAACAACAUCACAUGCAAUGCUUAUGAUAUUCUUC

'''

