rm(list = ls())
library(readxl)
library(ggplot2)
library(reshape2)
workbook <- "refined_top_10_proceedings.xlsx"
data_proceedings <- read_xlsx(workbook, 1)
data_proceedings
data <- melt(data_proceedings, id.vars='proceedings')
data
group <- as.factor(data$proceedings)
ggplot(data, aes(x = variable, y = value,  color = group)) + 
  geom_point(size = 3) + 
  geom_line(size = 1, aes(group = group, color = group)) + 
  labs(x = "Years", y = "Publications") +
  guides(color = guide_legend(title = "Proceedings")) +
  scale_y_continuous(expand = c(0.025,0), breaks = seq(0, 33, by = 3))+
  theme(panel.background = element_rect(fill = "white", colour="black", linewidth = 0.25),
        axis.line = element_line(colour = "black", linewidth = 0.25),
        axis.title = element_text(size = 24, color = "black"),
        axis.text = element_text(size = 10, color = "black"),
        legend.position = c(0.25,0.75))
