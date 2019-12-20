# MP-Hanoi

# Task 1 - Simulation of different play strategies for the Tower of Hanoi Game

For this task three strategies were simulated.
- **Agent 0**: Plans h moves ahead and chooses the set of moves that results in the highest score, where the score is measured as the number of discs in the correct location after h moves. When multiple possibilities shared the same score, the agent randomly selects from these.
- **Agent 1**: Given an initial state, this agent identifies the largest misplaced disk. It subsequently plans h moves ahead to try and place this disc in its correct location. If multiple possibilities satisfy this criteria, it chooses from them based on score, analogously to Agent 0. If no possibilities satisfy this criteria, it employs the exact same strategy as Agent 0.
- **Agent 2**: This agent is identical to Agent 1, except that it attempts to place a randomly chosen disc.

In these simulations, the start states are randomly initialized.  Experiments are also performed with respect to different winning states. In Win Context 0, all discs must be placed on a randomly chosen pole. In Win Context 1, the winning state is randomly chosen. We make no changes to the rules governing disc movements and valable configurations. All simulations involve four discs.

For each agent and win context, we simulate planning horizons in the range of 1 to 15. Each of these individual simulations is performed 250 times and the resulting scores are averaged, where score is the number of turns taken to complete the game.

The results are now presented and discussed.

## Results

<img src="c0.png" width="500">
<img src="c1.png" width="500">

The results will be interpreted by means of the two figures above.

A very similar overall trend can be observed in both figures.  At low h, the three agenst perform very similarly. As h increases, the differences become more pronounced. Starting at h = 3, Agent 0 becomes the worst player and clearly maintains this status until h == 11, where it then converges with the others. Noticable differences between Agents 1 and 2 can observed from h = 4 to h = 6. In this range, Agent 1 significantly outperforms Agent 2 in both win scenarios. From h = 7 onward their performance is essentially the same. 

At higher h, all three Agents achieve equal performance. This is explained by the fact that the solution for the game can often be found within such a planning horizon. The game is won before any choice can be made.

The trends of the graph show that there is little difference in difficulty between the two win contexts. The differences observed in turn counts could be attributed to the randomness inherent to the game. The results suggest that the two tasks could be mathematicaly equivalent.

## Discussion

Agent zero very clearly performs the worst. In my opinion, this is because this strategy is the most susceptible to falling into loops. Because of the score based criteria, it often ends up vacillating between the two same choices for many rounds.

Agent 1 appears to outperform Agent 2 for mid-range horizon ranges. I find that this makes intuitive sense, because this is a more directed and purposeful goal strategy. Perhaps by moving the largest misplaced disc, Agent 2 has less likelihood that the correct placement of a given disc be impeded by the presence of a smaller disc on the target pole.

If any of these strategies were to be taught to human players, Agent 1 would be the best candidate. Not only does it more quickly outperform the others, but it's goal setting strategy makes more intuitive sense than Agent 2's. However, it Agent 1 still requires a very large event horizon before it can complete the game in a reasonable time. It would be very difficult for human players to plan six moves ahead. 

Before proceeding to task 2, I would like to note some issues regarding the implementation. In its current state, the simulation is not scalable. Future efforts should focus on more efficient dynamic programming algorithms.

Additionally, it is surprising that all Agents completed each game within the maximum number of turns. This is especially peculiar given that Agent 1 is so susceptible to loops. This may be due to a faulty implementation, and must be further investigated.

# Task 2 - Productivity Scores

For this task, the results of a randomized controlled trial were provided, in which participants were trained using goal-setting apps, and productivity scores were subsequently collected.

Twelve of the columns represent different experiment conditions, and a thirteenth represents the control condition. It is not indicated which column represents the control condition, so it cannot be measured if a given condition produces a significant change with respect to the control.

Given this situation, I have decided to perform a t-test between each column pair. Using the resulting values, I computed an average p-value for a given column with respect to all others. While doing so, I also counted the number of times that the calculated p-value was <= 0.05. The following table contains this information in addition to some other useful metrics.

|condition|   mean|     sd|  av_p|sig_count|
|---------|-------|-------|------|---------|
|X81      | 91.59 | 28.60 | 0.56 |       1 |
|X40      | 92.66 | 27.14 | 0.62 |       0 |
|X99      | 96.20 | 32.97 | 0.57 |       0 |
|X114     | 94.96 | 31.49 | 0.65 |       0 |
|X94      | 94.27 | 29.67 | 0.67 |       0 |
|X116     | 93.62 | 25.01 | 0.65 |       0 |
|X69      | 95.37 | 29.55 | 0.62 |       0 |
|X125     | 90.50 | 28.91 | 0.50 |       1 |
|X84      | 87.00 | 32.72 | 0.34 |       1 |
|X95      |102.05 | 26.79 | 0.18 |       4 |
|X90      | 93.45 | 29.07 | 0.67 |       0 |
|X66      | 94.15 | 32.59 | 0.68 |       0 |
|X74      | 87.76 | 33.70 | 0.39 |       1 |

From the results, we see that the X95 condition stands out. It's average p-value is lowest, and with respect to the X81, X125, X84 and X74 conditions, the difference is significant. No significant differences were found between any other condition pairs.

It can be noted that the mean productivity score of the X95 condition is the highest (102.05), and the standard deviation is the second lowest (26.79). On average, the mean of X95 is 12.84 points higher than the means of the four other columns mentioned above. 

If X95 is the control condition, this is disappointing news for the researchers. In four experiments, the app would have negatively affected productivity, and in the remaining eight no significant difference would have been observed.

If X95 corresponds to one of the app conditions, then the results may promising. The outcomes are significantly better than at least three other app conditions. However, it remains unclear whether the results differ from those of the control condition.
