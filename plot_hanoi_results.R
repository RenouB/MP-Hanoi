library(tidyverse)
library(dplyr)
library(reshape2)
results <- read.csv("results.csv")

agent_zero <- results %>% filter(agent == 0)
zero_colors <- c("#AD2C23", "#FF7066")
agent_one <- results %>% filter(agent == 1)
one_colors <- c("#B39340","#FFE08F")
agent_two <- results %>% filter(agent == 2)
two_colors = c("#526AB3", "#90ABFF")
three_together_colors <- c("#FF7066","#FFE08F", "#90ABFF")

context_zero <- results %>% filter(win.context == 0)
context_one <- results %>%filter(win.context == 1)

number_ticks <- function(n) {function(limits) pretty(limits, n)}

# begin plotting agent 0
melted1 <- agent_zero %>% select("win.context","av.turns","h","failed") %>% 
  melt(id.vars=c("h", "win.context"), measure.vars=c("av.turns"))
melted2 <- agent_zero %>% select("win.context","av.turns","h","failed") %>% 
  melt(id.vars=c("h", "win.context"), measure.vars=c("failed"))
long <- cbind(melted1, melted2)
long <- long[,-c(5,6)]

g <- ggplot(long, aes(x=h, y=value, fill=factor(win.context))) + 
  geom_bar(stat="identity", position="dodge") +
  geom_text(aes(label=round(value)), position=position_dodge(width=0.9), vjust=-0.25)+
  scale_fill_manual(values = zero_colors, name= "Win scenario", labels=(c("random pole", "random state")))+
  xlab("h")+ylab("Average score") + scale_x_continuous(breaks=number_ticks(16)) +
  ggtitle("Agent zero's scores in both win scenarios")

g


# begin plotting agent 1
melted1 <- agent_one %>% select("win.context","av.turns","h","failed") %>% 
  melt(id.vars=c("h", "win.context"), measure.vars=c("av.turns"))
melted2 <- agent_one %>% select("win.context","av.turns","h","failed") %>% 
  melt(id.vars=c("h", "win.context"), measure.vars=c("failed"))
long <- cbind(melted1, melted2)
long <- long[,-c(5,6)]

g <- ggplot(long, aes(x=h, y=value, fill=factor(win.context))) + 
  geom_bar(stat="identity", position="dodge") +
  geom_text(aes(label=round(value)), position=position_dodge(width=0.9), vjust=-0.25)+
  scale_fill_manual(values = one_colors,name= "Win scenario", labels=(c("random pole", "random state")))+
  xlab("h")+ylab("Average score") + scale_x_continuous(breaks=number_ticks(16)) +
  ggtitle("Agent one's scores in both win scenarios")

g

# begin plotting agent 2
melted1 <- agent_two %>% select("win.context","av.turns","h","failed") %>% 
  melt(id.vars=c("h", "win.context"), measure.vars=c("av.turns"))
melted2 <- agent_two %>% select("win.context","av.turns","h","failed") %>% 
  melt(id.vars=c("h", "win.context"), measure.vars=c("failed"))
long <- cbind(melted1, melted2)
long <- long[,-c(5,6)]

g <- ggplot(long, aes(x=h, y=value, fill=factor(win.context))) + 
  geom_bar(stat="identity", position="dodge") +
  geom_text(aes(label=round(value)), position=position_dodge(width=0.9), vjust=-0.25)+
  scale_fill_manual(values = two_colors,name= "Win scenario", labels=(c("random pole", "random state")))+
  xlab("h")+ylab("Average score") + scale_x_continuous(breaks=number_ticks(16)) +
  ggtitle("Agent two's scores in both win scenarios")
g

# begin plotting context 0
melted1 <- context_zero %>% select("agent","av.turns","h","failed") %>% 
  melt(id.vars=c("h", "agent"), measure.vars=c("av.turns"))
melted2 <- context_zero %>% select("agent","av.turns","h","failed") %>% 
  melt(id.vars=c("h", "agent"), measure.vars=c("failed"))
long <- cbind(melted1, melted2)
long <- long[,-c(5,6)]

g <- ggplot(long, aes(x=h, y=value, fill=factor(agent))) + 
  geom_bar(stat="identity", width=0.7, position=position_dodge(width=0.7)) +
  geom_text(aes(label=round(value)), position=position_dodge(width=0.7), vjust=-0.25)+
  scale_fill_manual(values = three_together_colors, name= "Agent", labels=(c("0", "1", "2"))) +
  xlab("h")+ylab("Average score") + scale_x_continuous(breaks=number_ticks(16)) +
  ggtitle("Scores for each agent in win scenario zero")
g

# begin plotting context 1
melted1 <- context_one %>% select("agent","av.turns","h","failed") %>% 
  melt(id.vars=c("h", "agent"), measure.vars=c("av.turns"))
melted2 <- context_one %>% select("agent","av.turns","h","failed") %>% 
  melt(id.vars=c("h", "agent"), measure.vars=c("failed"))
long <- cbind(melted1, melted2)
long <- long[,-c(5,6)]

  g <- ggplot(long, aes(x=h, y=value, fill=factor(agent))) + 
  geom_bar(stat="identity", width=0.7, position=position_dodge(width=0.7)) +
  geom_text(aes(label=round(value)), position=position_dodge(width=0.7), vjust=-0.25)+
  scale_fill_manual(values = three_together_colors, name= "Agent", labels=(c("0", "1", "2"))) +
  xlab("h")+ylab("Average score") + scale_x_continuous(breaks=number_ticks(16)) +
  ggtitle("Scores for each agent in win scenario one")
g






