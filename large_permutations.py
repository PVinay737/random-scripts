#from itertools import permutations
#a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i','j','k','l']
#cc=('\n'.join(map(' '.join, permutations(a, len(a)))))
#print cc

cc=['a','b']

ss='ABCD'

def permutations(head, tail=''):
    if len(head) == 0: 
	with open('permsfile','a') as f1:
		print len(str(tail))
		f1.write(str(tail)+'\n')
    else:
        for i in range(len(head)):
            permutations(head[0:i] + head[i+1:], tail+head[i])


permutations(['a', 'b', 'c', 'd', 'e', 'f','g','h','i','j'])
