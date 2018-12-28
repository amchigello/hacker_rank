import itertools

def all_possible_combo(word):
    result=[]
    n=word.count('?')
    all_combos=list(itertools.product('01', repeat=n))
    # print(all_combos)
    index=[x for (x,y) in enumerate(word) if y=='?']
    # print(index)
    for combo in all_combos:
        # print(list(combo))
        new_word=list(word)
        # print(list(zip(list(combo),index)))
        for i in list(zip(list(combo),index)):
            new_word[i[1]]=i[0]
        result.append(''.join(new_word))
    print(*result)  
            

word='10??'
all_possible_combo(word)
