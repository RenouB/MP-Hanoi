import pickle
import pandas as pd

with open("result-a0c0.pkl", 'rb') as f:
	a0c0 = pickle.load(f)

with open("result-a0c1.pkl", 'rb') as f:
	a0c1 = pickle.load(f)

with open("result-a1c0.pkl", 'rb') as f:
	a1c0 = pickle.load(f)

with open("result-a1c1.pkl", 'rb') as f:
	a1c1 = pickle.load(f)

with open("result-a2c0.pkl", 'rb') as f:
	a2c0 = pickle.load(f)

with open("result-a2c1.pkl", 'rb') as f:
	a2c1 = pickle.load(f)

all = [a0c0, a0c1, a1c0, a1c1, a2c0, a2c1]


agents = []
hs = []
context =[]
av_turns =[]
failed = []
for results in all:
	print(results)
	for agent, contexts in results.items():
		for win_context, all_h in contexts.items():

			for h, counts in all_h.items():
				print(counts)
				agents.append(agent)
				hs.append(h)
				context.append(win_context)
				av_turns.append(counts["average_turn_count"])
				failed.append(counts["failed"])

dct = {"agent":agents, "h":hs, "win-context": context, "av-turns":av_turns, "failed":failed}
df = pd.DataFrame(dct)
df.to_csv("results.csv")