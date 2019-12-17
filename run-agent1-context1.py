from play import play_hanoi
import pandas as pd
import pickle

'''
run 500 trials for each agent in each game setting
keep track of average
'''

results = {}

for agent in [1]:
	print("#######################")
	print("AGENT", agent)
	print("#######################")
	results[agent] = {}
	for win_context in [1]:
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
											win_context=0, 
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
with open('result-a1c1.pkl', 'wb') as f:
	pickle.dump(results, f)