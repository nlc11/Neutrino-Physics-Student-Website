x <- as.numeric(as.POSIXct(Sys.time()))

n <- 1000

nums <- c()




for(i in 0:n){
  x <- (65539*x) %% 2**31
  u <- x/(2**31)
  nums <- c(nums, u)
}

hist(nums)

gumbel <- c(-log(-log(nums)))

h <- hist(gumbel, 30, probability = TRUE)

xtheory <- seq(-2, 8, 0.01)

ytheory <- c(exp(-(xtheory+exp(-xtheory))))
lines(xtheory, ytheory, col='purple')

xbins <- h$mids
ybins <- h$density
yexpect <- c(exp(-(xbins+exp(-xbins))))
chi <- sum((ybins - yexpect)**2/yexpect)
print(chi)
chi0 = chi/(length(xbins)-1)
print(chi0)

