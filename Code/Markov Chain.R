zones <- c("North", "West", "East")
transition <- matrix(c(0.1, 0.5, 0.4, 0.2, 0.3, 0.5, 0.1, 0.8, 0.1), nrow=3, byrow=T, dimnames=list(zones, zones))
transition

#install.packages("markovchain")
library(markovchain)

McZone <- new("markovchain", states=zones, byrow=T, transitionMatrix=transition, name="Transitions")
McZone 

#install.packages("diagram")
library(diagram)

plotmat(transition, pos=c(1,2), lwd=1, box.lwd = 1, cex.txt = 0.5, box.size = 0.1, box.type = "circle", box.prop = 0.5, box.col = "purple", arr.length = 0.1, arr.width = 0.1, self.cex = 0.4, self.shifty = -0.01, self.shiftx = 0.13, main = "Transition Diagram")

steadyStates(McZone)

McZone^25