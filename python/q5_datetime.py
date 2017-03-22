# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
from datetime import datetime  
def delta(date1, date2):  
    date1 = datetime.strptime(date1, "%m-%d-%Y")  
    date2 = datetime.strptime(date2, "%m-%d-%Y")  
    return (date2 - date1).days  

delta(date_start, date_stop)

####b)  
date_start = '12312013'  
date_stop = '05282015'  
from datetime import datetime  
def delta(date1, date2):  
    date1 = datetime.strptime(date1, "%m%d%Y")  
    date2 = datetime.strptime(date2, "%m%d%Y")  
    return (date2 - date1).days  

delta(date_start, date_stop)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
from datetime import datetime  
def delta(date1, date2):  
    date1 = datetime.strptime(date1, "%d-%b-%Y")  
    date2 = datetime.strptime(date2, "%d-%b-%Y")  
    return (date2 - date1).days  

delta(date_start, date_stop)
