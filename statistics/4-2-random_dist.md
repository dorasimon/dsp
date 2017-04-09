[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> l = list(np.random.random(1000))  
d = {x: l.count(x) for x in l}  
pmf = thinkstats2.Pmf(d)  
thinkplot.Pmf(pmf)  
thinkplot.Config(xlabel = "Number", ylabel = "PMF")  
cdf = thinkstats2.Cdf(d, label = "number")  
thinkplot.Cdf(cdf)  
thinkplot.Config(xlabel = "Number", ylabel = "CDF")
