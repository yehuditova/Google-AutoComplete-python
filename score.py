def get_score(fix_name, index):
    score={
        'char_change':
            {1:5,
             2:4,
             3:3,
             4:2,
             'else':1},
        'char_remove':
            {1: 10,
             2: 8,
             3: 6,
             4: 4,
             'else': 2},
        'char_add':
            {1: 10,
             2: 8,
             3: 6,
             4: 4,
             'else': 2},
    }
    if index<5:
        return score[fix_name][index]
    else:
        return score[fix_name]['else']