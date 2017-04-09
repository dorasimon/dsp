[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> resp = nsfg.ReadFemResp()  
d = dict(resp.numkdhh.value_counts())  
pmf = thinkstats2.Pmf(d, label = "actual")  
biased_pmf = BiasPmf(pmf, label = "biased")  
thinkplot.PrePlot(2)  
thinkplot.Pmfs([pmf, biased_pmf])  
thinkplot.Config(xlabel = "Number of children", ylabel = "PMF")  
print("Actual mean", pmf.Mean())  
print("Observed mean", biased_pmf.Mean())  
Actual mean 1.02420515504  
Observed mean 2.40367910066
