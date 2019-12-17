library(tidyverse)
library(dplyr)
library(reshape2)
results <- read.csv("fake_results.csv")

agent_zero <- results %>% filter(agent == 0)
melted <- agent_zero %>% select("win.context","av.turns","h","failed") %>% 
  melt(id.vars=c("h", "win.context"), measure.vars=c("av.turns", "failed"))

library(ggplot2)
number_ticks <- function(n) {function(limits) pretty(limits, n)}

g <- ggplot(melted, aes(x=h, y=value, fill=factor(win.context))) + 
  geom_bar(stat="identity", position="dodge") +
  geom_text(aes(label=value), vjust=0) +
  opts(axis.text.x=theme_blank(),
       axis.ticks=theme_blank(),
       axis.title.x=theme_blank(),
       legend.title=theme_blank(),
       axis.title.y=theme_blank()
  ) +
  scale_fill_discrete(name="Win scenario",
                    # breaks=c(1, 2),
                    labels=c("Random pole", "Random state"))+
  xlab("h")+ylab("Average score") +ylim(0,15) +   scale_x_continuous(breaks=number_ticks(16))





g





df = melt(data.frame(agent=agent_one$h,, turns=agent_one$av.turns, 
                     context=agent_one$win.context))
