#str->list of str
#generate all permutations of a given string
def perm_gen_lex(a): 
    '''For each character in the input string:
        Form a simpler string by removing the character from the input string
        Generate all permutations of the simpler string recursively (i.e. call the perm_gen_lex function with the simpler string)
        Add the removed character to the front of each permutation of the simpler string, and add the resulting permutation to the list '''
    if type(a) != str: raise ValueError
    if a == "": return []
    if len(a) == 1:
        return [a]
    list1 = []
    for i in a:
        x = i
        b = a.replace(i,'')
        reduced_result = perm_gen_lex(b)
        for j in reduced_result:
            list1.append(i + j)
    return list1



x = perm_gen_lex('abcdefghijk')
#print(x)
