library(tidyverse)

# A randomized controlled trial compared 12 different variants 
# of a goal setting app to a control condition that did wasn’t 
# given the goal setting app. The researcher recruited 50 participants 
# per condition and used RescueTime to obtain a productivity score
# for each participant. The resulting data are contained 
# in the attached csv file. How would you interpret these results?

# I would assume researchers assigned either first or last column for control.
# X81: mean 91.59, std 28.6068 mean p: 0.5636
# X74: mean 87.76, std 33.7027 mean p: 0.3517
# Neither X81 nor X74 are statistically different with respect to any columns.
# I conclude that X74 is most probably the control.

# with respect to x81, x95 has lowest p value -> 0.0427
# with respect to x74, x95 has lowest p value -> 0.0122
# I looked into x95. It has mean p of 0.1086 wrt everything else.
# has significant p values wrt four other columns. 
# has highest mean at 102. second lowest std at 26.80.
# four confidence intervals that do not allow for 0.

df <- read.csv("productivity_scores.csv")

p_comparisons <- matrix(nrow=13,ncol=13)
colnames(p_comparisons) <- colnames(df)
rownames(p_comparisons) <- colnames(df)

summary <- matrix(nrow=13, ncol=4)
colnames(summary) <- c("mean","sd","av_p","sig_count")
rownames(summary)<- colnames(df)

boxplot(df)

# for each column, get its p values wrt all other cols
for(i in c(1:length(colnames(df)))){
  name <- colnames(df)[i]
  print(name)
  summary[name,"mean"] <- mean(df[[name]])
  summary[name,"sd"] <- sd(df[[name]])
  summary[name,"sig_count"] <- 0
  for(ii in c(1:length(colnames(df)))){
    print(ii)
    name2 <- colnames(df)[ii]
    cat(name,name2,"\n")
    test <- t.test(df[[name]], df[[name2]])
    p <- test$p.value
    if (p < 0.05){
      summary[name,"sig_count"] <- summary[name,"sig_count"] + 1
    }
    p_comparisons[name,name2] <- p
  }
  summary[name,"av_p"] <- sum(p_comparisons[name,-1]) / 12
}

