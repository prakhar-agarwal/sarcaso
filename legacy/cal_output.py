#Function to compute the sarcasm value of the input tweet
def calculate_output(sample, fpath):

    f_trait = open('user_data/traits/traits_'+fpath,'r')

    res = f_trait.read()
    trait_dict = eval(res)

    f_trait.close()

    sarcasm_value = 0.0

    for k in sample.keys():
        if k in trait_dict.keys():
            #negative tweet about positive trait
            if float(sample[k])<0 and float(trait_dict[k])>0:
                sarcasm_value += 1.2 * ( abs(float(trait_dict[k])) + abs(float(sample[k])))
            
            #positive tweet about negative trait
            elif float(sample[k])>0 and float(trait_dict[k])<0:
                sarcasm_value += 1.6 * ( abs(float(sample[k])) + abs(float(trait_dict[k])))
            
            else:
                sarcasm_value += 0.2 * (abs( float(trait_dict[k]) - float(sample[k])))
    #Normalize value computed
    sarcasm_value = sarcasm_value/3.2

    return sarcasm_value

