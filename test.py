# Python dictionary to convert letters into numbers
l_to_n = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 
    'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 
    'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 
    'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 
    'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 
    'Z': 25, 'AA': 26, 'AB': 27, 'AC': 28, 'AD': 29
}

n_to_l = {v: k for k, v in l_to_n.items()}

def formula_from_week(week):
    return f'=INDEX(AC:AC, MATCH(GetOpponent(INDIRECT("AB"&ROW()), TEXTJOIN(",", true, {n_to_l[(week)-1]}$3:{n_to_l[week]}$14)), AB:AB, 0)) / (INDEX(AC:AC, MATCH(GetOpponent(INDIRECT("AB"&ROW()), TEXTJOIN(",", true, {n_to_l[(week)-1]}$3:{n_to_l[week]}$14)), AB:AB, 0)) + INDEX(AD:AD, MATCH(GetOpponent(INDIRECT("AB"&ROW()), TEXTJOIN(",", true, {n_to_l[(week)-1]}$3:{n_to_l[week]}$14)), AB:AB, 0)))'

for i in range(1,50,2):
    print((i // 2)+1, formula_from_week(i), end='\n\n')