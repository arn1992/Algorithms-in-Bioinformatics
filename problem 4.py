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




f = open('input1.txt', "r")

line = f.readline()

l=''
while line:

    print(line)
    l+="".join( line.splitlines())

    line = f.readline()
f.close()
#print(l)

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

#output

'''
ACTGTTGTTCGGTGATCATCAGTTGTACAACGTCCTAACAACATCACATGCAATGCTTATGATATTCTTC

TTCATCATGCCAGGCACGATGGCAGGACTAGGCAACTTACTAGTGCCATTCCAGATGAGTGTACCGGAGT

TAGTATTCCCAAAGATTAATAACATCGGTATATGATTTTTAGTATGTGGTCTACTTTTGATTACGGGTTC

ATCTTGGATGGAGGAAGGTTCAGGAACGGCCTGAACCGTCTATCCACCACTAGCGCTCACTGCAAGTCAT

AGCGGACTTGCTGTAGATACGTTCATTATCGCATTGCACATGGCCGGTGCAAGCTCCCTTACAGGAAGCA

TCAACCTTATATGTACAATCGCCTATGCCCGCCGTTCACTCATGGCGATGCTGCAGTCATCACTTTATCC

CTGATCCATTACAATCACTGCAGCGTTACTCATAGGAGTTGTGCCTGTGCTAGCAGGTGCTATCACGATG

CTACTCACTGATAGAAGTTGGAGTACCAGCTTCTATGACAGTTCGGCAGGCGGTGATCCTATGTTGTATC

AGCACTTATTCTGGGTGTTTGGGCATCCAGAAGTCTATATCATCATACTTCCAGTATTCGGTATAGTCAG
5’3’ Frame 1:  T V V R * S S V V Q R P N N I T C N A Y D I L L H H A R H D G R T R Q L T S A I P D E C T G V S I P K D * * H R Y M I F S M W S T F D Y G F I L D G G R F R N G L N R L S T T S A H C K S * R T C C R Y V H Y R I A H G R C K L P Y R K H Q P Y M Y N R L C P P F T H G D A A V I T L S L I H Y N H C S V T H R S C A C A S R C Y H D A T H * * K L E Y Q L L * Q F G R R * S Y V V S A L I L G V W A S R S L Y H H T S S I R Y S Q 
5’3’ Frame 2:  L L F G D H Q L Y N V L T T S H A M L M I F F F I M P G T M A G L G N L L V P F Q M S V P E L V F P K I N N I G I * F L V C G L L L I T G S S W M E E G S G T A * T V Y P P L A L T A S H S G L A V D T F I I A L H M A G A S S L T G S I N L I C T I A Y A R R S L M A M L Q S S L Y P * S I T I T A A L L I G V V P V L A G A I T M L L T D R S W S T S F Y D S S A G G D P M L Y Q H L F W V F G H P E V Y I I I L P V F G I V 
5’3’ Frame 3:  C C S V I I S C T T S * Q H H M Q C L * Y S S S S C Q A R W Q D * A T Y * C H S R * V Y R S * Y S Q R L I T S V Y D F * Y V V Y F * L R V H L G W R K V Q E R P E P S I H H * R S L Q V I A D L L * I R S L S H C T W P V Q A P L Q E A S T L Y V Q S P M P A V H S W R C C S H H F I P D P L Q S L Q R Y S * E L C L C * Q V L S R C Y S L I E V G V P A S M T V R Q A V I L C C I S T Y S G C L G I Q K S I S S Y F Q Y S V * S 
3’5’ Frame 1:  L T I P N T G S M M I * T S G C P N T Q N K C * Y N I G S P P A E L S * K L V L Q L L S V S S I V I A P A S T G T T P M S N A A V I V M D Q G * S D D C S I A M S E R R A * A I V H I R L M L P V R E L A P A M C N A I M N V S T A S P L * L A V S A S G G * T V Q A V P E P S S I Q D E P V I K S R P H T K N H I P M L L I F G N T N S G T L I W N G T S K L P S P A I V P G M M K K N I I S I A C D V V R T L Y N * * S P N N S 
3’5’ Frame 2:  * L Y R I L E V * * Y R L L D A Q T P R I S A D T T * D H R L P N C H R S W Y S N F Y Q * V A S * * H L L A Q A Q L L * V T L Q * L * W I R D K V M T A A S P * V N G G H R R L Y I * G * C F L * G S L H R P C A M R * * T Y L Q Q V R Y D L Q * A L V V D R R F R P F L N L P P S K M N P * S K V D H I L K I I Y R C Y * S L G I L T P V H S S G M A L V S C L V L P S C L A * * R R I S * A L H V M L L G R C T T D D H R T T 
3’5’ Frame 3:  D Y T E Y W K Y D D I D F W M P K H P E * V L I Q H R I T A C R T V I E A G T P T S I S E * H R D S T C * H R H N S Y E * R C S D C N G S G I K * * L Q H R H E * T A G I G D C T Y K V D A S C K G A C T G H V Q C D N E R I Y S K S A M T C S E R * W W I D G S G R S * T F L H P R * T R N Q K * T T Y * K S Y T D V I N L W E Y * L R Y T H L E W H * * V A * S C H R A W H D E E E Y H K H C M * C C * D V V Q L M I T E Q Q 

'''