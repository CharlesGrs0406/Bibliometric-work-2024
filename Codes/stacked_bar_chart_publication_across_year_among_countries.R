rm(list = ls())
library(paletteer)
library(readxl)
library(reshape2)
library(ggplot2)
library(RColorBrewer)
workbook <- "country_publish_count_refined_top_10.xlsx"
mydataframe <- read_xlsx(workbook, 1)
mydataframe
data<-melt(mydataframe, id.vars = 'country')
data
paletteer_d("RColorBrewer::Paired")
ggplot(data = data,
       mapping = aes(x = variable, y = value, fill = country))+
  geom_bar(stat = "identity", position = "stack", color = "black", width = 0.7, linewidth = 0.25)+
  scale_fill_manual(values = c("#FB9A99FF", "#E31A1CFF", "#FF7F00FF", "#FDBF6FFF", "#B2DF8AFF", "#33A02CFF", "#A6CEE3FF","#1F78B4FF", "#CAB2D6FF", "#6A3D9AFF"))+
  labs(x = "Years", y = "Publications")+
  scale_y_continuous(expand = c(0,0), breaks = c(0, 100, 200, 300, 400, 500, 600))+
  theme_classic(base_size = 15)+
  theme(panel.background = element_rect(fill = "white", colour="black", linewidth = 0.25),
        axis.line = element_line(colour = "black", linewidth = 0.25),
        axis.title = element_text(size = 20, color = "black"),
        axis.text = element_text(size = 10, color = "black"),
        legend.position = c(0.15, 0.72)
  )
