amino_acid={"Isoleucine": {'ATT','ATC','ATA'},
            "Leucine":{'CTT','CTC','CTA','CTG','TTA','TTG'},
            "Valine":{'GTT','GTC','GTA','GTG'},
            "Phenylalanine":{'TTT','TTC'},
            "Methionine":{'ATG'},
            "Cysteine":{'TGT','TGC'},
            "Alanine": {'GCT','GCC','GCA','GCG'},
            "Glycine":{'GGT','GGC','GGA','GGG'},
            "Proline":{'CCT','CCC','CCA','CCG'},
            "Threonine":{'ACT','ACC','ACA','ACG'},
            "Serine":{'TCT','TCC','TCA','TCG','AGT','AGC'},
            "Tyrosine":{'TAT','TAC'},
            "Tryptophan":{'TGG'},
            "Glutamine":{'CAA','CAG'},
            "Asparagine":{'AAT','AAC'},
            "Histidine":{'CAT','CAC'},
            "Glutamic_acid":{'GAA','GAG'},
            "Aspartic_acid":{'GAT','GAC'},
            "Lysine":{'AAA','AAG'},
            "Arginine":{'CGT','CGC','CGA','CGG','AGA','AGG'},
            "Stop_codons":{'TAA','TAG','TGA'}
}

print("Amino Acids and Associated Codons:")
for key in amino_acid:
    print(key," : ",amino_acid[key])



#output

'''
Amino Acids and Associated Codons:
Methionine  :  {'ATG'}
Threonine  :  {'ACC', 'ACG', 'ACA', 'ACT'}
Serine  :  {'TCA', 'TCG', 'TCC', 'AGC', 'TCT', 'AGT'}
Arginine  :  {'CGC', 'CGT', 'AGG', 'CGG', 'CGA', 'AGA'}
Isoleucine  :  {'ATA', 'ATC', 'ATT'}
Tyrosine  :  {'TAT', 'TAC'}
Aspartic_acid  :  {'GAC', 'GAT'}
Proline  :  {'CCT', 'CCA', 'CCC', 'CCG'}
Histidine  :  {'CAT', 'CAC'}
Glutamic_acid  :  {'GAA', 'GAG'}
Tryptophan  :  {'TGG'}
Leucine  :  {'CTA', 'CTG', 'CTT', 'CTC', 'TTG', 'TTA'}
Alanine  :  {'GCG', 'GCA', 'GCT', 'GCC'}
Asparagine  :  {'AAT', 'AAC'}
Valine  :  {'GTA', 'GTT', 'GTC', 'GTG'}
Phenylalanine  :  {'TTC', 'TTT'}
Stop_codons  :  {'TAA', 'TGA', 'TAG'}
Glutamine  :  {'CAG', 'CAA'}
Glycine  :  {'GGC', 'GGA', 'GGT', 'GGG'}
Cysteine  :  {'TGT', 'TGC'}
Lysine  :  {'AAA', 'AAG'}
'''

