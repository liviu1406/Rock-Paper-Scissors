dictionary = ['all', 'an', 'and', 'as', 'closely', 'correct', 'equivocal',
              'examine', 'indication', 'is', 'means', 'minutely', 'or', 'scrutinize',
              'sign', 'the', 'to', 'uncertain']


words = [cuv for cuv in input().split() if cuv not in dictionary]
print('\n'.join(words) or 'OK')
