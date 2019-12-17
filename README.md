# MP-Hanoi

# Task 2 - Productivity Scores

For this task, I was provided with the results of a randomized controlled trial, where different goal setting apps were provided to participants and productivity scores were subsequently obtained.

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

From the results, we see that the X95 condition stands out. It's average p-value is lowest, and with respect to the X81, X125, X84 and X74 columns, the difference is significant. No other significant differences were found between any other column pairs.

It can be noted that the mean productivity score of the X95 condition is the highest (102.05), and the standard deviation is the second lowest (26.79). On average, the mean of X95 is 12.84 points higher than the means of the four columns mentioned above. 

If X95 is the control condition, this is disappointing news for the researchers. In four experiments, the app would have negatively affected productivity and in the remaining eight no significant difference would have been observed.

If X95 corresponds to one of the app experiments, then the results may be quite promising. It results in significantly better outcomes than at least three other apps. However, it remains unclear whether the results differ from those of the control condition.
