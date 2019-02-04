
print("Name: Md. Aminur Rab Ratul; ID: 300086571")

final_score= list()

def zeros(shape):
    retval = []
    for x in range(shape[0]):
        retval.append([])
        for y in range(shape[1]):
            retval[-1].append(0)
    return retval

match_award = 1
mismatch_penalty1 = -5
mismatch_penalty2 = -1
gap_penalty = -3  # Indel

def match_score(alpha, beta):

    if (alpha == '-' and beta == '-'):
        return gap_penalty


    elif alpha == beta:

        return match_award
    elif (alpha == '-' or beta == '-'):
        return gap_penalty

    #transition/transversion substitution matrix implementation

    elif ((alpha=='A' and beta=='C')or(alpha=='A' and beta=='T') or (alpha=='C' and beta=='A')or (alpha=='C' and beta=='G') or (alpha=='G' and beta=='C') or (alpha=='G' and beta=='T') or (alpha=='T' and beta=='A')or (alpha=='T' and beta=='G')):

        return mismatch_penalty1
    elif ((alpha=='A' and beta=='G')or (alpha=='C' and beta=='T')or  (alpha=='G' and beta=='A') or  (alpha=='T' and beta=='C')):

        return mismatch_penalty2
    else:
        return gap_penalty


def finalize(align1, align2):
    align1 = align1[::-1]  # reverse sequence 1
    align2 = align2[::-1]  # reverse sequence 2

    i, j = 0, 0

    # calcuate identity, score and aligned sequeces
    symbol = ''
    found = 0
    score = 0
    identity = 0
    for i in range(0, len(align1)):
        # if two AAs are the same, then output the letter
        if align1[i] == align2[i]:
            symbol = symbol + align1[i]
            identity = identity + 1
            score += match_score(align1[i], align2[i])

        # if they are not identical and none of them is gap
        elif align1[i] != align2[i] and align1[i] != '-' and align2[i] != '-':
            score += match_score(align1[i], align2[i])
            symbol += ' '
            found = 0

        # if one of them is a gap, output a space
        elif align1[i] == '-' or align2[i] == '-':
            symbol += ' '
            score += gap_penalty

    identity = float(identity) / len(align1) * 100

    #print( 'Identity =', "%3.3f" % identity, 'percent')

    print ('Score =', score)
    final_score.append(int(score))

    #print(final_score)

    print( align1)

    #print ( symbol)
    print ( align2)





def water(seq1, seq2):
    m= len(seq1)
    #print('length sequnce1: ',m)
    n=len(seq2)  # length of two sequences
    #print('length sequnce2: ', n)

    # Generate DP table and traceback path pointer matrix
    score = zeros((m + 1, n + 1))  # the DP table
    pointer = zeros((m + 1, n + 1))  # to store the traceback path

    max_score = 0  # initial maximum score in DP table
    # Calculate DP table and mark pointers
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            #print(score,' ki')
            score_diagonal = score[i - 1][j - 1] + match_score(seq1[i - 1], seq2[j - 1])

            ##print(score, ' ki1')
            score_up = score[i][j - 1] + gap_penalty

            score_left = score[i - 1][j] + gap_penalty

            score[i][j] = max(0, score_left, score_up, score_diagonal)
            if score[i][j] == 0:
                pointer[i][j] = 0  # 0 means end of the path
            if score[i][j] == score_left:
                pointer[i][j] = 1  # 1 means trace up
            if score[i][j] == score_up:
                pointer[i][j] = 2  # 2 means trace left
            if score[i][j] == score_diagonal:
                pointer[i][j] = 3  # 3 means trace diagonal
            if score[i][j] >= max_score:
                max_i = i
                max_j = j
                max_score = score[i][j];

    align1, align2 = '', ''  # initial sequences

    i, j = max_i, max_j  # indices of path starting point

    # traceback, follow pointers
    while pointer[i][j] != 0:
        if pointer[i][j] == 3:
            align1 += seq1[i - 1]
            align2 += seq2[j - 1]
            i -= 1
            j -= 1
        elif pointer[i][j] == 2:
            align1 += '_'
            align2 += seq2[j - 1]
            j -= 1
        elif pointer[i][j] == 1:
            align1 += seq1[i - 1]
            align2 += '-'
            i -= 1


    finalize(align1, align2)
    #print(pointer)



#randomly generate 1000 pairs of DNA Sequence

print('randomly Generate 1000 pairs with 280 and 240 length: ')
import random

for i in range(0,1000):


    #print("take sequence1 with equal probability (PA=PC=PG=PT=.25; 70 each and total 280: )")
    dna_list = [x for x in ''.join(['ACGT' for i in range(70)])]
    random.shuffle(dna_list)
    sequnce1 = ''.join(dna_list)
    #print(sequnce1)
    #print("take sequence2 with equal probability (PA=PC=PG=PT=.25; 60 each and total 240: )")
    dna_list2 = [x for x in ''.join(['ACGT' for i in range(60)])]
    random.shuffle(dna_list2)
    sequnce2 = ''.join(dna_list2)
    #print(sequnce2)

    # convert lower case to upper case letter and check two sequnces:
    water(sequnce1.upper(), sequnce2.upper())

#generate plot
print('generate plot: ')

import matplotlib.pyplot as plt
import numpy as np
# x axis values
x=list()
x =list(np.arange(0,1000,1))
# corresponding y axis values
y = final_score

# plotting the points
plt.plot(x, y)


# naming the x axis
plt.xlabel('value from 0 to 1000')
# naming the y axis
plt.ylabel('plot the scores value')

# giving a title to my graph
plt.title('Alignment of random sequences of 1000 pairs')

# function to show the plot
plt.show()


'''
#scatter plot part
import matplotlib.pyplot as plt
import numpy as np
# x axis values
x=list()
x =list(np.arange(0,1000,1))
# corresponding y axis values
y = final_score

# plotting the points
plt.scatter(x, y)


# naming the x axis
plt.xlabel('value from 0 to 1000')
# naming the y axis
plt.ylabel('plot the scores value')

# giving a title to my graph
plt.title('Alignment of random sequences of 1000 pairs')

# function to show the plot
plt.show()
'''

'''
#histogram part
import numpy as np
import matplotlib.pyplot as plt
x=list()
x =list(np.arange(0,1000,1))
# corresponding y axis values
y = final_score

data = y
plt.hist(data, histtype='stepfilled', bins=5)
plt.xlabel('plot the scores value')
# naming the y axis
plt.ylabel('number of pairs in each bins')

# giving a title to my graph
plt.title('Alignment of random sequences of 1000 pairs')
# function to show the plot
plt.show()
'''