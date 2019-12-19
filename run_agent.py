from play import play_hanoi
import pandas as pd
import pickle
from argparse import ArgumentParser

'''
run 500 trials for each agent in each game setting
keep track of average
'''

if __name__ == "__main__":
	parser = ArgumentParser()
	parser.add_argument('-a', type=int)
	parser.add_argument('-c', type=int)
	args = parser.parse_args()

	results = {}

	for agent in [args.a]:
		print("#######################")
		print("AGENT", agent)
		print("#######################")
		results[agent] = {}
		for win_context in [args.c]:
			print("\n")
			print("CONTEXT", win_context)
			results[agent][win_context] ={}
			subsolutions = {}
			for h in range(15,1,-1):
				print("H", h)
				results[agent][win_context][h] = {}
				results[agent][win_context][h]['turn_count'] = 0
				results[agent][win_context][h]['solved'] = 0
				results[agent][win_context][h]['failed'] = 0
				for i in range(250):
					if i % 20 == 0:
						print(i)
					turn_count, subsolutions = play_hanoi(h=h, n_discs=4, agent=agent, \
												win_context=1, 
												subsolutions=subsolutions)
					if turn_count <= 1000:
						results[agent][win_context][h]['turn_count'] += turn_count
						results[agent][win_context][h]['solved'] += 1
					else:
						results[agent][win_context][h]['failed'] += 1
				if 	results[agent][win_context][h]['solved'] > 0:
					results[agent][win_context][h]['average_turn_count'] = \
						results[agent][win_context][h]['turn_count'] / \
						results[agent][win_context][h]['solved']
				else:
					results[agent][win_context][h]['average_turn_count'] = 1000
		print("\n")

	print(results)
	with open('result-a{}c{}.pkl'.format(args.a, args.c), 'wb') as f:
		pickle.dump(results, f)