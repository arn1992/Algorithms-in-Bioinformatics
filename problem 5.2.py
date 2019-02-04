

def main(a,b):
    distance1=0
    distance2=3
    s3=''
    s4=''
    op=''
    op1=''
    op2=''
    op3=''
    op4=''
    opx=''

    fo=''
    fd=0
    m=0
    l=0


    for i in range(len(a)):
        s1 = a[i]
        for j in range(len(b)):
            s2 = b[j]
            for s in range(len(s1)):

                if s1[s] != s2[s]:
                    distance1 += 1
            op = s1 + " & " + s2 + " ; "

            if j == 0:
                l=j
                d = distance1
                s3 = s1
                s4 = s2
                op1 = s3 + " & " + s4 + " ;"

            elif distance1 < distance2:
                opx=''

                distance2 = distance1
                opx = op

            elif distance1==distance2:
                opx = opx + " " + op


            distance1 = 0

        if distance2<d:

            op3=" "+opx+" "

            opx=''

        elif d<distance2:

            m=d
            op3=" "+op1+ " "



        elif d==distance2:

            op2=opx+" "+op1
            opx=''

            op3=" "+op2+" "



        if i == 0:
            if l==0:
                l=0

                fd = m
                op4=op3
            else:
                fd = distance2

                op4 = op3



        elif i > 0:

            if distance2 < fd:
                fd=distance2

                op4=''
                op4 = op3

            elif distance2 == fd:

                op4 = op4 + " " + op3

        op3=''
        distance2=3

    return op4






Isoleucine=['ATT','ATA','ATC']
Leucine=['CTT','CTC','CTA','CTG','TTA','TTG']
Valine=['GTT','GTC','GTA','GTG']
Phenylalanine=['TTT','TTC']
Methionine=['ATG']
Cysteine=['TGT','TGC']
Alanine=['GCT','GCC','GCA','GCG']
Glycine=['GGT','GGC','GGA','GGG']
Proline=['CCT','CCC','CCA','CCG']
Threonine=['ACT','ACC','ACA','ACG']
Serine=['TCT','TCC','TCA','TCG','AGT','AGC']
Tyrosine=['TAT','TAC']
Tryptophan=['TGG']
Glutamine=['CAA','CAG']
Asparagine=['AAT','AAC']
Histidine=['CAT','CAC']
Glutamic_acid=['GAA','GAG']
Aspartic_acid=['GAT','GAC']
Lysine=['AAA','AAG']
Arginine=['CGT','CGC','CGA','CGG','AGA','AGG']
Stop_codons=['TAA','TAG','TGA']

#Hamming Distance
#Isoleucine to others or Vice Versa
print('Hamming Distance from Isoleucine to others or Vice Versa: ')
n=main(Isoleucine,Leucine)
print('Minimum Hamming Distace between (Isoleucine & Leucine) or (Leucine & Isoleucine): ',n)

n=main(Isoleucine,Valine)
print('Minimum Hamming Distace between (Isoleucine & Valine) or (Valine & Isoleucine): ',n)

n=main(Isoleucine,Phenylalanine)
print('Minimum Hamming Distace between (Isoleucine & Phenylalanine) or (Phenylalanine & Isoleucine) : ',n)

n=main(Methionine, Isoleucine)
print('Minimum Hamming Distace between(Methionine & Isoleucine) or (Isoleucine & Methionine) : ',n)

n=main(Isoleucine,Cysteine)
print('Minimum Hamming Distace between (Isoleucine & Cysteine) or (Cysteine & Isoleucine): ',n)

n=main(Isoleucine,Alanine)
print('Minimum Hamming Distace between (Isoleucine & Alanine) or (Alanine & Isoleucine): ',n)

n=main(Isoleucine,Glycine)
print('Minimum Hamming Distace between (Isoleucine & Glycine) or (Glycine & Isoleucine): ',n)

n=main(Isoleucine,Proline)
print('Minimum Hamming Distace between (Isoleucine & Proline) or (Proline & Isoleucine): ',n)

n=main(Isoleucine,Threonine)
print('Minimum Hamming Distace between (Isoleucine & Threonine) or (Threonine & Isoleucine): ',n)

n=main(Isoleucine,Serine)
print('Minimum Hamming Distace between (Isoleucine & Serine) or (Serine & Isoleucine): ',n)

n=main(Isoleucine,Tyrosine)
print('Minimum Hamming Distace between (Isoleucine & Tyrosine) or (Tyrosine & Isoleucine): ',n)

n=main(Tryptophan,Isoleucine)
print('Minimum Hamming Distace between (Tryptophan & Isoleucine) or (Isoleucine & Tryptophan) : ',n)

n=main(Isoleucine,Glutamine)
print('Minimum Hamming Distace between (Isoleucine & Glutamine) or (Glutamine & Isoleucine): ',n)

n=main(Isoleucine,Asparagine)
print('Minimum Hamming Distace between (Isoleucine & Asparagine) or (Asparagine & Isoleucine) : ',n)

n=main(Isoleucine,Histidine)
print('Minimum Hamming Distace between (Isoleucine & Histidine) or (Histidine & Isoleucine): ',n)

n=main(Glutamic_acid,Isoleucine)
print('Minimum Hamming Distace between (Glutamic Acid & Isoleucine) or (Isoleucine & Glutamic Acid): ',n)

n=main(Isoleucine,Aspartic_acid)
print('Minimum Hamming Distace between (Isoleucine & Aspartic Acid) or (Aspartic Acid & Isoleucine): ',n)

n=main(Lysine,Isoleucine)
print('Minimum Hamming Distace between (Lysine & Isoleucine) or (Isoleucine & Lysine): ',n)

n=main(Isoleucine,Arginine)
print('Minimum Hamming Distace between (Isoleucine & Arginine) or (Arginine & Isoleucine): ',n)

n=main(Stop_codons,Isoleucine)
print('Minimum Hamming Distace between (Isoleucine & Stop Codons) or (Stop Codons & Isoleucine): ',n)

################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Leucine to others or Vice Versa: ')

n=main(Leucine,Valine)
print('Minimum Hamming Distace between (Leucine & Valine) or (Valine & Leucine): ',n)

n=main(Leucine,Phenylalanine)
print('Minimum Hamming Distace between (Leucine & Phenylalanine) or (Phenylalanine & Leucine) : ',n)

n=main(Methionine, Leucine)
print('Minimum Hamming Distace between (Leucine & Methionine) or (Methionine & Leucine): ',n)

n=main(Leucine,Cysteine)
print('Minimum Hamming Distace between (Leucine & Cysteine) or (Cysteine & Leucine): ',n)

n=main(Leucine,Alanine)
print('Minimum Hamming Distace between (Leucine & Alanine) or (Alanine & Leucine): ',n)

n=main(Leucine,Glycine)
print('Minimum Hamming Distace between (Leucine & Glycine) or (Glycine & Leucine): ',n)

n=main(Leucine,Proline)
print('Minimum Hamming Distace between (Leucine & Proline) or (Proline & Leucine): ',n)

n=main(Leucine,Threonine)
print('Minimum Hamming Distace between (Leucine & Threonine) or (Threonine & Leucine): ',n)

n=main(Leucine,Serine)
print('Minimum Hamming Distace between (Leucine & Serine) or (Serine & Leucine): ',n)

n=main(Leucine,Tyrosine)
print('Minimum Hamming Distace between (Leucine & Tyrosine) or (Tyrosine & Leucine): ',n)

n=main(Tryptophan,Leucine)
print('Minimum Hamming Distace between (Leucine & Tryptophan) or (Tryptophan & Leucine): ',n)

n=main(Glutamine,Leucine)
print('Minimum Hamming Distace between (Glutamine & Leucine) or (Leucine & Glutamine) or: ',n)

n=main(Leucine,Asparagine)
print('Minimum Hamming Distace between (Leucine & Asparagine) or (Asparagine & Leucine) : ',n)

n=main(Leucine,Histidine)
print('Minimum Hamming Distace between (Leucine & Histidine) or (Histidine & Leucine): ',n)

n=main(Glutamic_acid,Leucine)
print('Minimum Hamming Distace between (Glutamic Acid & Leucine) or (Leucine & Glutamic Acid): ',n)

n=main(Leucine,Aspartic_acid)
print('Minimum Hamming Distace between (Leucine & Aspartic Acid) or (Aspartic Acid & Leucine): ',n)

n=main(Lysine,Leucine)
print('Minimum Hamming Distace between (Lysine & Leucine)or (Leucine & Lysine) : ',n)

n=main(Leucine,Arginine)
print('Minimum Hamming Distace between (Leucine & Arginine) or (Arginine & Leucine): ',n)

n=main(Stop_codons,Leucine)
print('Minimum Hamming Distace between (Leucine & Stop Codons) or (Stop Codons & Leucine): ',n)


################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Valine to others or Vice Versa: ')


n=main(Valine,Phenylalanine)
print('Minimum Hamming Distace between (Valine & Phenylalanine) or (Phenylalanine & Valine) : ',n)

n=main(Methionine, Valine)
print('Minimum Hamming Distace between (Valine & Methionine) or (Methionine & Valine): ',n)

n=main(Valine,Cysteine)
print('Minimum Hamming Distace between (Valine & Cysteine) or (Cysteine & Valine): ',n)

n=main(Valine,Alanine)
print('Minimum Hamming Distace between (Valine & Alanine) or (Alanine & Valine): ',n)

n=main(Valine,Glycine)
print('Minimum Hamming Distace between (Valine & Glycine) or (Glycine & Valine): ',n)

n=main(Valine,Proline)
print('Minimum Hamming Distace between (Valine & Proline) or (Proline & Valine): ',n)

n=main(Valine,Threonine)
print('Minimum Hamming Distace between (Valine & Threonine) or (Threonine & Valine): ',n)

n=main(Valine,Serine)
print('Minimum Hamming Distace between (Valine & Serine) or (Serine & Valine): ',n)

n=main(Valine,Tyrosine)
print('Minimum Hamming Distace between (Valine & Tyrosine) or (Tyrosine & Valine): ',n)

n=main(Tryptophan,Valine)
print('Minimum Hamming Distace between (Valine & Tryptophan) or (Tryptophan & Valine): ',n)

n=main(Glutamine,Valine)
print('Minimum Hamming Distace between (Glutamine & Valine) or (Valine & Glutamine): ',n)

n=main(Valine,Asparagine)
print('Minimum Hamming Distace between (Valine & Asparagine) or (Asparagine & Valine) : ',n)

n=main(Valine,Histidine)
print('Minimum Hamming Distace between (Valine & Histidine) or (Histidine & Valine): ',n)

n=main(Glutamic_acid,Valine)
print('Minimum Hamming Distace between (Glutamic Acid & Valine) or (Valine & Glutamic Acid): ',n)

n=main(Valine,Aspartic_acid)
print('Minimum Hamming Distace between (Valine & Aspartic Acid) or (Aspartic Acid & Valine): ',n)

n=main(Lysine,Valine)
print('Minimum Hamming Distace between (Lysine & Valine)or (Valine & Lysine) : ',n)

n=main(Valine,Arginine)
print('Minimum Hamming Distace between (Valine & Arginine) or (Arginine & Valine): ',n)

n=main(Stop_codons,Valine)
print('Minimum Hamming Distace between (Valine & Stop Codons) or (Stop Codons & Valine): ',n)


################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Phenylalanine to others or Vice Versa: ')




n=main(Methionine, Phenylalanine)
print('Minimum Hamming Distace between (Phenylalanine & Methionine) or (Methionine & Phenylalanine): ',n)

n=main(Phenylalanine,Cysteine)
print('Minimum Hamming Distace between (Phenylalanine & Cysteine) or (Cysteine & Phenylalanine): ',n)

n=main(Phenylalanine,Alanine)
print('Minimum Hamming Distace between (Phenylalanine & Alanine) or (Alanine & Phenylalanine): ',n)

n=main(Phenylalanine,Glycine)
print('Minimum Hamming Distace between (Phenylalanine & Glycine) or (Glycine & Phenylalanine): ',n)

n=main(Phenylalanine,Proline)
print('Minimum Hamming Distace between (Phenylalanine & Proline) or (Proline & Phenylalanine): ',n)

n=main(Phenylalanine,Threonine)
print('Minimum Hamming Distace between (Phenylalanine & Threonine) or (Threonine & Phenylalanine): ',n)

n=main(Phenylalanine,Serine)
print('Minimum Hamming Distace between (Phenylalanine & Serine) or (Serine & Phenylalanine): ',n)

n=main(Phenylalanine,Tyrosine)
print('Minimum Hamming Distace between (Phenylalanine & Tyrosine) or (Tyrosine & Phenylalanine): ',n)

n=main(Tryptophan,Phenylalanine)
print('Minimum Hamming Distace between (Phenylalanine & Tryptophan) or (Tryptophan & Phenylalanine): ',n)

n=main(Glutamine,Phenylalanine)
print('Minimum Hamming Distace between (Glutamine & Phenylalanine) or (Phenylalanine & Glutamine): ',n)

n=main(Phenylalanine,Asparagine)
print('Minimum Hamming Distace between (Phenylalanine & Asparagine) or (Asparagine & Phenylalanine) : ',n)

n=main(Phenylalanine,Histidine)
print('Minimum Hamming Distace between (Phenylalanine & Histidine) or (Histidine & Phenylalanine): ',n)

n=main(Glutamic_acid,Phenylalanine)
print('Minimum Hamming Distace between (Glutamic Acid & Phenylalanine) or (Phenylalanine & Glutamic Acid): ',n)

n=main(Phenylalanine,Aspartic_acid)
print('Minimum Hamming Distace between (Phenylalanine & Aspartic Acid) or (Aspartic Acid & Phenylalanine): ',n)

n=main(Lysine,Phenylalanine)
print('Minimum Hamming Distace between (Lysine & Phenylalanine)or (Lysine & Phenylalanine) : ',n)

n=main(Phenylalanine,Arginine)
print('Minimum Hamming Distace between (Phenylalanine & Arginine) or (Arginine & Phenylalanine): ',n)

n=main(Stop_codons,Phenylalanine)
print('Minimum Hamming Distace between (Phenylalanine & Stop Codons) or (Stop Codons & Phenylalanine): ',n)


################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Methionine to others or Vice Versa: ')



n=main(Methionine,Cysteine)
print('Minimum Hamming Distace between (Methionine & Cysteine) or (Cysteine & Methionine): ',n)

n=main(Methionine,Alanine)
print('Minimum Hamming Distace between (Methionine & Alanine) or (Alanine & Methionine): ',n)

n=main(Methionine,Glycine)
print('Minimum Hamming Distace between (Methionine & Glycine) or (Glycine & Methionine): ',n)

n=main(Methionine,Proline)
print('Minimum Hamming Distace between (Methionine & Proline) or (Proline & Methionine): ',n)

n=main(Methionine,Threonine)
print('Minimum Hamming Distace between (Methionine & Threonine) or (Threonine & Methionine): ',n)

n=main(Methionine,Serine)
print('Minimum Hamming Distace between (Methionine & Serine) or (Serine & Methionine): ',n)

n=main(Methionine,Tyrosine)
print('Minimum Hamming Distace between (Methionine & Tyrosine) or (Tyrosine & Methionine): ',n)

n=main(Tryptophan,Methionine)
print('Minimum Hamming Distace between (Methionine & Tryptophan) or (Tryptophan & Methionine): ',n)

n=main(Glutamine,Methionine)
print('Minimum Hamming Distace between (Glutamine & Methionine) or (Methionine & Glutamine): ',n)

n=main(Methionine,Asparagine)
print('Minimum Hamming Distace between (Methionine & Asparagine) or (Asparagine & Methionine) : ',n)

n=main(Methionine,Histidine)
print('Minimum Hamming Distace between (Methionine & Histidine) or (Histidine & Methionine): ',n)

n=main(Glutamic_acid,Methionine)
print('Minimum Hamming Distace between (Glutamic Acid & Methionine) or (Methionine & Glutamic Acid): ',n)

n=main(Methionine,Aspartic_acid)
print('Minimum Hamming Distace between (Methionine & Aspartic Acid) or (Aspartic Acid & Methionine): ',n)

n=main(Lysine,Methionine)
print('Minimum Hamming Distace between (Lysine & Methionine)or (Lysine & Methionine) : ',n)

n=main(Methionine,Arginine)
print('Minimum Hamming Distace between (Methionine & Arginine) or (Arginine & Methionine): ',n)

n=main(Stop_codons,Methionine)
print('Minimum Hamming Distace between (Methionine & Stop Codons) or (Stop Codons & Methionine): ',n)



################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Cysteine to others or Vice Versa: ')


n=main(Cysteine,Alanine)
print('Minimum Hamming Distace between (Cysteine & Alanine) or (Alanine & Cysteine): ',n)

n=main(Cysteine,Glycine)
print('Minimum Hamming Distace between (Cysteine & Glycine) or (Glycine & Cysteine): ',n)

n=main(Cysteine,Proline)
print('Minimum Hamming Distace between (Cysteine & Proline) or (Proline & Cysteine): ',n)

n=main(Cysteine,Threonine)
print('Minimum Hamming Distace between (Cysteine & Threonine) or (Threonine & Cysteine): ',n)

n=main(Cysteine,Serine)
print('Minimum Hamming Distace between (Cysteine & Serine) or (Serine & Cysteine): ',n)

n=main(Cysteine,Tyrosine)
print('Minimum Hamming Distace between (Cysteine & Tyrosine) or (Tyrosine & Cysteine): ',n)

n=main(Tryptophan,Cysteine)
print('Minimum Hamming Distace between (Cysteine & Tryptophan) or (Tryptophan & Cysteine): ',n)

n=main(Glutamine,Cysteine)
print('Minimum Hamming Distace between (Glutamine & Cysteine) or (Cysteine & Glutamine): ',n)

n=main(Cysteine,Asparagine)
print('Minimum Hamming Distace between (Cysteine & Asparagine) or (Asparagine & Cysteine) : ',n)

n=main(Cysteine,Histidine)
print('Minimum Hamming Distace between (Cysteine & Histidine) or (Histidine & Cysteine): ',n)

n=main(Glutamic_acid,Cysteine)
print('Minimum Hamming Distace between (Glutamic Acid & Cysteine) or (Cysteine & Glutamic Acid): ',n)

n=main(Cysteine,Aspartic_acid)
print('Minimum Hamming Distace between (Cysteine & Aspartic Acid) or (Aspartic Acid & Cysteine): ',n)

n=main(Lysine,Cysteine)
print('Minimum Hamming Distace between (Lysine & Cysteine)or (Lysine & Cysteine) : ',n)

n=main(Cysteine,Arginine)
print('Minimum Hamming Distace between (Cysteine & Arginine) or (Arginine & Cysteine): ',n)

n=main(Stop_codons,Cysteine)
print('Minimum Hamming Distace between (Cysteine & Stop Codons) or (Stop Codons & Cysteine): ',n)



################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Alanine to others or Vice Versa: ')



n=main(Alanine,Glycine)
print('Minimum Hamming Distace between (Alanine & Glycine) or (Glycine & Alanine): ',n)

n=main(Alanine,Proline)
print('Minimum Hamming Distace between (Alanine & Proline) or (Proline & Alanine): ',n)

n=main(Alanine,Threonine)
print('Minimum Hamming Distace between (Alanine & Threonine) or (Threonine & Alanine): ',n)

n=main(Alanine,Serine)
print('Minimum Hamming Distace between (Alanine & Serine) or (Serine & Alanine): ',n)

n=main(Alanine,Tyrosine)
print('Minimum Hamming Distace between (Alanine & Tyrosine) or (Tyrosine & Alanine): ',n)

n=main(Tryptophan,Alanine)
print('Minimum Hamming Distace between (Alanine & Tryptophan) or (Tryptophan & Alanine): ',n)

n=main(Glutamine,Alanine)
print('Minimum Hamming Distace between (Glutamine & Alanine) or (Alanine & Glutamine): ',n)

n=main(Alanine,Asparagine)
print('Minimum Hamming Distace between (Alanine & Asparagine) or (Asparagine & Alanine) : ',n)

n=main(Alanine,Histidine)
print('Minimum Hamming Distace between (Alanine & Histidine) or (Histidine & Alanine): ',n)

n=main(Glutamic_acid,Alanine)
print('Minimum Hamming Distace between (Glutamic Acid & Alanine) or (Alanine & Glutamic Acid): ',n)

n=main(Alanine,Aspartic_acid)
print('Minimum Hamming Distace between (Alanine & Aspartic Acid) or (Aspartic Acid & Alanine): ',n)

n=main(Lysine,Alanine)
print('Minimum Hamming Distace between (Lysine & Alanine)or (Lysine & Alanine) : ',n)

n=main(Alanine,Arginine)
print('Minimum Hamming Distace between (Alanine & Arginine) or (Arginine & Alanine): ',n)

n=main(Stop_codons,Alanine)
print('Minimum Hamming Distace between (Alanine & Stop Codons) or (Stop Codons & Alanine): ',n)


################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Glycine to others or Vice Versa: ')


n=main(Glycine,Proline)
print('Minimum Hamming Distace between (Glycine & Proline) or (Proline & Glycine): ',n)

n=main(Glycine,Threonine)
print('Minimum Hamming Distace between (Glycine & Threonine) or (Threonine & Glycine): ',n)

n=main(Glycine,Serine)
print('Minimum Hamming Distace between (Glycine & Serine) or (Serine & Glycine): ',n)

n=main(Glycine,Tyrosine)
print('Minimum Hamming Distace between (Glycine & Tyrosine) or (Tyrosine & Glycine): ',n)

n=main(Tryptophan,Glycine)
print('Minimum Hamming Distace between (Glycine & Tryptophan) or (Tryptophan & Glycine): ',n)

n=main(Glutamine,Glycine)
print('Minimum Hamming Distace between (Glutamine & Glycine) or (Glycine & Glutamine): ',n)

n=main(Glycine,Asparagine)
print('Minimum Hamming Distace between (Glycine & Asparagine) or (Asparagine & Glycine) : ',n)

n=main(Glycine,Histidine)
print('Minimum Hamming Distace between (Glycine & Histidine) or (Histidine & Glycine): ',n)

n=main(Glutamic_acid,Glycine)
print('Minimum Hamming Distace between (Glutamic Acid & Glycine) or (Glycine & Glutamic Acid): ',n)

n=main(Glycine,Aspartic_acid)
print('Minimum Hamming Distace between (Glycine & Aspartic Acid) or (Aspartic Acid & Glycine): ',n)

n=main(Lysine,Glycine)
print('Minimum Hamming Distace between (Lysine & Glycine)or (Lysine & Glycine) : ',n)

n=main(Glycine,Arginine)
print('Minimum Hamming Distace between (Glycine & Arginine) or (Arginine & Glycine): ',n)

n=main(Stop_codons,Glycine)
print('Minimum Hamming Distace between (Glycine & Stop Codons) or (Stop Codons & Glycine): ',n)



################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Proline to others or Vice Versa: ')


n=main(Proline,Threonine)
print('Minimum Hamming Distace between (Proline & Threonine) or (Threonine & Proline): ',n)

n=main(Proline,Serine)
print('Minimum Hamming Distace between (Proline & Serine) or (Serine & Proline): ',n)

n=main(Proline,Tyrosine)
print('Minimum Hamming Distace between (Proline & Tyrosine) or (Tyrosine & Proline): ',n)

n=main(Tryptophan,Proline)
print('Minimum Hamming Distace between (Proline & Tryptophan) or (Tryptophan & Proline): ',n)

n=main(Glutamine,Proline)
print('Minimum Hamming Distace between (Glutamine & Proline) or (Proline & Glutamine): ',n)

n=main(Proline,Asparagine)
print('Minimum Hamming Distace between (Proline & Asparagine) or (Asparagine & Proline) : ',n)

n=main(Proline,Histidine)
print('Minimum Hamming Distace between (Proline & Histidine) or (Histidine & Proline): ',n)

n=main(Glutamic_acid,Proline)
print('Minimum Hamming Distace between (Glutamic Acid & Proline) or (Proline & Glutamic Acid): ',n)

n=main(Proline,Aspartic_acid)
print('Minimum Hamming Distace between (Proline & Aspartic Acid) or (Aspartic Acid & Proline): ',n)

n=main(Lysine,Proline)
print('Minimum Hamming Distace between (Lysine & Proline)or (Lysine & Proline) : ',n)

n=main(Proline,Arginine)
print('Minimum Hamming Distace between (Proline & Arginine) or (Arginine & Proline): ',n)

n=main(Stop_codons,Proline)
print('Minimum Hamming Distace between (Proline & Stop Codons) or (Stop Codons & Proline): ',n)


################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Threonine to others or Vice Versa: ')


n=main(Threonine,Serine)
print('Minimum Hamming Distace between (Threonine & Serine) or (Serine & Threonine): ',n)

n=main(Threonine,Tyrosine)
print('Minimum Hamming Distace between (Threonine & Tyrosine) or (Tyrosine & Threonine): ',n)

n=main(Tryptophan,Threonine)
print('Minimum Hamming Distace between (Threonine & Tryptophan) or (Tryptophan & Threonine): ',n)

n=main(Glutamine,Threonine)
print('Minimum Hamming Distace between (Glutamine & Threonine) or (Threonine & Glutamine): ',n)

n=main(Threonine,Asparagine)
print('Minimum Hamming Distace between (Threonine & Asparagine) or (Asparagine & Threonine) : ',n)

n=main(Threonine,Histidine)
print('Minimum Hamming Distace between (Threonine & Histidine) or (Histidine & Threonine): ',n)

n=main(Glutamic_acid,Threonine)
print('Minimum Hamming Distace between (Glutamic Acid & Threonine) or (Threonine & Glutamic Acid): ',n)

n=main(Threonine,Aspartic_acid)
print('Minimum Hamming Distace between (Threonine & Aspartic Acid) or (Aspartic Acid & Threonine): ',n)

n=main(Lysine,Threonine)
print('Minimum Hamming Distace between (Lysine & Threonine)or (Lysine & Threonine) : ',n)

n=main(Threonine,Arginine)
print('Minimum Hamming Distace between (Threonine & Arginine) or (Arginine & Threonine): ',n)

n=main(Stop_codons,Threonine)
print('Minimum Hamming Distace between (Threonine & Stop Codons) or (Stop Codons & Threonine): ',n)


################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Serine to others or Vice Versa: ')


n=main(Serine,Tyrosine)
print('Minimum Hamming Distace between (Serine & Tyrosine) or (Tyrosine & Serine): ',n)

n=main(Tryptophan,Serine)
print('Minimum Hamming Distace between (Serine & Tryptophan) or (Tryptophan & Serine): ',n)

n=main(Glutamine,Serine)
print('Minimum Hamming Distace between (Glutamine & Serine) or (Serine & Glutamine): ',n)

n=main(Serine,Asparagine)
print('Minimum Hamming Distace between (Serine & Asparagine) or (Asparagine & Serine) : ',n)

n=main(Serine,Histidine)
print('Minimum Hamming Distace between (Serine & Histidine) or (Histidine & Serine): ',n)

n=main(Glutamic_acid,Serine)
print('Minimum Hamming Distace between (Glutamic Acid & Serine) or (Serine & Glutamic Acid): ',n)

n=main(Serine,Aspartic_acid)
print('Minimum Hamming Distace between (Serine & Aspartic Acid) or (Aspartic Acid & Serine): ',n)

n=main(Lysine,Serine)
print('Minimum Hamming Distace between (Lysine & Serine)or (Lysine & Serine) : ',n)

n=main(Serine,Arginine)
print('Minimum Hamming Distace between (Serine & Arginine) or (Arginine & Serine): ',n)

n=main(Stop_codons,Serine)
print('Minimum Hamming Distace between (Serine & Stop Codons) or (Stop Codons & Serine): ',n)


################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Tyrosine to others or Vice Versa: ')


n=main(Tryptophan,Tyrosine)
print('Minimum Hamming Distace between (Tyrosine & Tryptophan) or (Tryptophan & Tyrosine): ',n)

n=main(Glutamine,Tyrosine)
print('Minimum Hamming Distace between (Glutamine & Tyrosine) or (Tyrosine & Glutamine): ',n)

n=main(Tyrosine,Asparagine)
print('Minimum Hamming Distace between (Tyrosine & Asparagine) or (Asparagine & Tyrosine) : ',n)

n=main(Tyrosine,Histidine)
print('Minimum Hamming Distace between (Tyrosine & Histidine) or (Histidine & Tyrosine): ',n)

n=main(Glutamic_acid,Tyrosine)
print('Minimum Hamming Distace between (Glutamic Acid & Tyrosine) or (Tyrosine & Glutamic Acid): ',n)

n=main(Tyrosine,Aspartic_acid)
print('Minimum Hamming Distace between (Tyrosine & Aspartic Acid) or (Aspartic Acid & Tyrosine): ',n)

n=main(Lysine,Tyrosine)
print('Minimum Hamming Distace between (Lysine & Tyrosine)or (Lysine & Tyrosine) : ',n)

n=main(Tyrosine,Arginine)
print('Minimum Hamming Distace between (Tyrosine & Arginine) or (Arginine & Tyrosine): ',n)

n=main(Stop_codons,Tyrosine)
print('Minimum Hamming Distace between (Tyrosine & Stop Codons) or (Stop Codons & Tyrosine): ',n)


################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Tryptophan to others or Vice Versa: ')


n=main(Glutamine,Tryptophan)
print('Minimum Hamming Distace between (Glutamine & Tryptophan) or (Tryptophan & Glutamine): ',n)

n=main(Tryptophan,Asparagine)
print('Minimum Hamming Distace between (Tryptophan & Asparagine) or (Asparagine & Tryptophan) : ',n)

n=main(Tryptophan,Histidine)
print('Minimum Hamming Distace between (Tryptophan & Histidine) or (Histidine & Tryptophan): ',n)

n=main(Glutamic_acid,Tryptophan)
print('Minimum Hamming Distace between (Glutamic Acid & Tryptophan) or (Tryptophan & Glutamic Acid): ',n)

n=main(Tryptophan,Aspartic_acid)
print('Minimum Hamming Distace between (Tryptophan & Aspartic Acid) or (Aspartic Acid & Tryptophan): ',n)

n=main(Lysine,Tryptophan)
print('Minimum Hamming Distace between (Lysine & Tryptophan)or (Lysine & Tryptophan) : ',n)

n=main(Tryptophan,Arginine)
print('Minimum Hamming Distace between (Tryptophan & Arginine) or (Arginine & Tryptophan): ',n)

n=main(Stop_codons,Tryptophan)
print('Minimum Hamming Distace between (Tryptophan & Stop Codons) or (Stop Codons & Tryptophan): ',n)


################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Glutamine to others or Vice Versa: ')


n=main(Glutamine,Asparagine)
print('Minimum Hamming Distace between (Glutamine & Asparagine) or (Asparagine & Glutamine) : ',n)

n=main(Glutamine,Histidine)
print('Minimum Hamming Distace between (Glutamine & Histidine) or (Histidine & Glutamine): ',n)

n=main(Glutamic_acid,Glutamine)
print('Minimum Hamming Distace between (Glutamic Acid & Glutamine) or (Glutamine & Glutamic Acid): ',n)

n=main(Glutamine,Aspartic_acid)
print('Minimum Hamming Distace between (Glutamine & Aspartic Acid) or (Aspartic Acid & Glutamine): ',n)

n=main(Lysine,Glutamine)
print('Minimum Hamming Distace between (Lysine & Glutamine)or (Lysine & Glutamine) : ',n)

n=main(Glutamine,Arginine)
print('Minimum Hamming Distace between (Glutamine & Arginine) or (Arginine & Glutamine): ',n)

n=main(Stop_codons,Glutamine)
print('Minimum Hamming Distace between (Glutamine & Stop Codons) or (Stop Codons & Glutamine): ',n)


################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Asparagine to others or Vice Versa: ')


n=main(Asparagine,Histidine)
print('Minimum Hamming Distace between (Asparagine & Histidine) or (Histidine & Asparagine): ',n)

n=main(Glutamic_acid,Asparagine)
print('Minimum Hamming Distace between (Glutamic Acid & Asparagine) or (Asparagine & Glutamic Acid): ',n)

n=main(Asparagine,Aspartic_acid)
print('Minimum Hamming Distace between (Asparagine & Aspartic Acid) or (Aspartic Acid & Asparagine): ',n)

n=main(Lysine,Asparagine)
print('Minimum Hamming Distace between (Lysine & Asparagine)or (Lysine & Asparagine) : ',n)

n=main(Asparagine,Arginine)
print('Minimum Hamming Distace between (Asparagine & Arginine) or (Arginine & Asparagine): ',n)

n=main(Stop_codons,Asparagine)
print('Minimum Hamming Distace between (Asparagine & Stop Codons) or (Stop Codons & Asparagine): ',n)



################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Histidine to others or Vice Versa: ')


n=main(Glutamic_acid,Histidine)
print('Minimum Hamming Distace between (Glutamic Acid & Histidine) or (Histidine & Glutamic Acid): ',n)

n=main(Histidine,Aspartic_acid)
print('Minimum Hamming Distace between (Histidine & Aspartic Acid) or (Aspartic Acid & Histidine): ',n)

n=main(Lysine,Histidine)
print('Minimum Hamming Distace between (Lysine & Histidine)or (Lysine & Histidine) : ',n)

n=main(Histidine,Arginine)
print('Minimum Hamming Distace between (Histidine & Arginine) or (Arginine & Histidine): ',n)

n=main(Stop_codons,Histidine)
print('Minimum Hamming Distace between (Histidine & Stop Codons) or (Stop Codons & Histidine): ',n)


################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Glutamic_acid to others or Vice Versa: ')


n=main(Glutamic_acid,Aspartic_acid)
print('Minimum Hamming Distace between (Glutamic_acid & Aspartic Acid) or (Aspartic Acid & Glutamic_acid): ',n)

n=main(Lysine,Glutamic_acid)
print('Minimum Hamming Distace between (Lysine & Glutamic_acid)or (Lysine & Glutamic_acid) : ',n)

n=main(Glutamic_acid,Arginine)
print('Minimum Hamming Distace between (Glutamic_acid & Arginine) or (Arginine & Glutamic_acid): ',n)

n=main(Stop_codons,Glutamic_acid)
print('Minimum Hamming Distace between (Glutamic_acid & Stop Codons) or (Stop Codons & Glutamic_acid): ',n)


################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Aspartic_acid to others or Vice Versa: ')



n=main(Lysine,Aspartic_acid)
print('Minimum Hamming Distace between (Lysine & Aspartic_acid)or (Lysine & Aspartic_acid) : ',n)

n=main(Aspartic_acid,Arginine)
print('Minimum Hamming Distace between (Aspartic_acid & Arginine) or (Arginine & Aspartic_acid): ',n)

n=main(Stop_codons,Aspartic_acid)
print('Minimum Hamming Distace between (Aspartic_acid & Stop Codons) or (Stop Codons & Aspartic_acid): ',n)


################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Lysine to others or Vice Versa: ')


n=main(Lysine,Arginine)
print('Minimum Hamming Distace between (Lysine & Arginine) or (Arginine & Lysine): ',n)

n=main(Stop_codons,Lysine)
print('Minimum Hamming Distace between (Lysine & Stop Codons) or (Stop Codons & Lysine): ',n)


################################################################################################################
print('################################################################################################################')


#Hamming Distance
#Leucine to others or Vice Versa
print('Hamming Distance from Arginine to others or Vice Versa: ')


n=main(Stop_codons,Arginine)
print('Minimum Hamming Distace between (Arginine & Stop Codons) or (Stop Codons & Arginine): ',n)


#some of the output:

'''
Hamming Distance from Isoleucine to others or Vice Versa: 
Minimum Hamming Distace between (Isoleucine & Leucine) or (Leucine & Isoleucine):   ATT & CTT ;   ATA & CTA ;  ATA & TTA ;    ATC & CTC ;  
Minimum Hamming Distace between (Isoleucine & Valine) or (Valine & Isoleucine):   ATT & GTT ;   ATA & GTA ;    ATC & GTC ;  
Minimum Hamming Distace between (Isoleucine & Phenylalanine) or (Phenylalanine & Isoleucine) :   ATT & TTT ;   ATC & TTC ;  
Minimum Hamming Distace between(Methionine & Isoleucine) or (Isoleucine & Methionine) :   ATG & ATA ;  ATG & ATC ;  ATG & ATT ; 
Minimum Hamming Distace between (Isoleucine & Cysteine) or (Cysteine & Isoleucine):   ATT & TGT ;   ATC & TGC ;  
Minimum Hamming Distace between (Isoleucine & Alanine) or (Alanine & Isoleucine):   ATT & GCT ;   ATA & GCA ;    ATC & GCC ;  
Minimum Hamming Distace between (Isoleucine & Glycine) or (Glycine & Isoleucine):   ATT & GGT ;   ATA & GGA ;    ATC & GGC ;  
Minimum Hamming Distace between (Isoleucine & Proline) or (Proline & Isoleucine):   ATT & CCT ;   ATA & CCA ;    ATC & CCC ;  
Minimum Hamming Distace between (Isoleucine & Threonine) or (Threonine & Isoleucine):   ATT & ACT ;   ATA & ACA ;    ATC & ACC ;  

'''

