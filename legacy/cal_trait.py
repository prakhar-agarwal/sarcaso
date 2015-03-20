import polarity

def calculate_trait(fpath):
    polarity_scores = polarity.get_scores()
    f = open('user_data/opinions/opinion_'+fpath)
    o = f.read()
    op = eval(o)
    trait_dict = {}
    for k in op.keys():
        p_val = 0.0
        adj_phrase_list = op[k]
        for adj in adj_phrase_list:
            if adj[0] == '':
                try:
                    p_val += polarity_scores[adj[1]]
                except:
                    pass
            else:
                try:
                    p_val += polarity_scores[adj[0] + ' ' + adj[1]]
                except:
                    pass
        avg_val = 0.0
        if len(adj_phrase_list) != 0:
            avg_val = p_val/len(adj_phrase_list)
        
        trait_dict[k] = avg_val
    
    f2=open('user_data/traits/traits_'+fpath, 'w')
    f2.write(str(trait_dict))
