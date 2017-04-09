[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> def centimeters(foot, inch):  
    return (foot * 12 + inch) * 2.54  
dist.cdf(centimeters(6, 1)) - dist.cdf(centimeters(5, 10))  
0.34274683763147457  
About 34% of the people are between 5'10" and 6'1".
