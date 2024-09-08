rm(list = ls())
library(readxl)
library(ggplot2)
library(reshape2)
workbook <- "refined_top_10_journals.xlsx"
data_journals <- read_xlsx(workbook, 1)
data_journals
data <- melt(data_journals, id.vars='journals')
data
group <- as.factor(data$journals)
ggplot(data, aes(x = variable, y = value,  color = group)) + 
  geom_point(size = 3) + 
  geom_line(size = 1, aes(group = group, color = group)) + 
  labs(x = "Years", y = "Publications") +
  guides(color = guide_legend(title = "Journals")) +
  scale_y_continuous(expand = c(0.05,0), breaks = c(0:13))+
  theme(panel.background = element_rect(fill = "white", colour="black", linewidth = 0.25),
        axis.line = element_line(colour = "black", linewidth = 0.25),
        axis.title = element_text(size = 24, color = "black"),
        axis.text = element_text(size = 10, color = "black"),
        legend.position = c(0.24,0.75))
