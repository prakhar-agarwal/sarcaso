def search_hashtag(t):

    position = t.find('#sarcasm')

    #search if hashtag is present in tweet
    if position >= 0:
        
        #check if hashtag prepends tweet
        if position==0 and (t[8]=='\n' or t[8]=='\0' or t[8]=='.'):
            return 1

        #check if hashtag appends tweet
        elif position!=0 and (t[position]=='\n' or (t[position-2]=='.' or t[position-1]==' ')):
            return 1

        #hashtag present but maybe part of sentence
        else:
            return 0

    
    #if hashtag not present
    else:
        return -1
