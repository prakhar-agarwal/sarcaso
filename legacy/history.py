def create_history(fpath):

    f = open('user_data/history/history_'+fpath,'r')

    data = []

    for line in f:
        data.append(str(line))

    f.close()

    return data

