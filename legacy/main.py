from user import user

import relations
import polarity
import cal_trait
import cal_output
import history
import hashtag

#Set user IDs
user1 = user()
user2 = user()
user3 = user()
user4 = user()

#initialized score database
polarity_scores = polarity.get_scores()


#initialize user history
data = history.create_history('user_1')


#input test data
print "-------ENTER TWEET TO ANALYZE-------"
tweet = raw_input()
print "------------------------------------"


#analyse test data

#lexical analysis

hash_value = hashtag.search_hashtag(tweet)


#like/dislike analysis

f = open('user_data/opinions/opinion_user_1','w')
f.write( str( user1.create_subject_list(data)))
f.close()

cal_trait.calculate_trait('user_1')

#output answer
sample_relations = relations.get_dict_relations(tweet)
sample_trait = {}

for k in sample_relations.keys():
     p_val = 0.0
     adj_phrase_list = sample_relations[k]
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
           
         sample_trait[k] = avg_val

final_output = 0.0

if hash_value == 1:
    final_output = (2.0 * cal_output.calculate_output(sample_trait,'user_1') + 1)/3

print '\n'
print "----------------------------------------------------------"
print "Sarcasm Value Calculated: ", final_output
print "----------------------------------------------------------"
