import csv

with open("emails.csv", "w", newline = "") as file:
    writer = csv.writer(file, delimiter = ",")
    data = [
    ["email"], 
    ['bellamys@mail.med.upenn.edu'], 
    ['warren@upenn.edu'], 
    ['bryanma@upenn.edu'], 
    ['jinboche@upenn.edu'], 
    ['sellenbe@upenn.edu'], 
    ['jellenbe@mail.med.upenn.edu'], 
    ['ruifeng@upenn.edu'], 
    ['bcfrench@mail.med.upenn.edu'], 
    ['pgimotty@upenn.edu'], 
    ['wguo@mail.med.upenn.edu'], 
    ['hsu9@mail.med.upenn.edu'], 
    ['rhubb@mail.med.upenn.edu'], 
    ['whwang@mail.med.upenn.edu'], 
    ['mjoffe@mail.med.upenn.edu'], 
    ['jrlandis@mail.med.upenn.edu'], 
    ['liy3@email.chop.edu'], 
    ['mingyao@mail.med.upenn.edu'], 
    ['hongzhe@upenn.edu'], 
    ['rlocalio@upenn.edu'], 
    ['nanditam@mail.med.upenn.edu'], 
    ['knashawn@mail.med.upenn.edu'], 
    ['propert@mail.med.upenn.edu'], 
    ['mputt@mail.med.upenn.edu'], 
    ['sratclif@upenn.edu'], 
    ['michross@upenn.edu'], 
    ['jaroy@mail.med.upenn.edu'], 
    ['msammel@cceb.med.upenn.edu'], 
    ['shawp@upenn.edu'], 
    ['rshi@mail.med.upenn.edu'], 
    ['hshou@mail.med.upenn.edu'], 
    ['jshults@mail.med.upenn.edu'], 
    ['alisaste@mail.med.upenn.edu'], 
    ['atroxel@mail.med.upenn.edu'], 
    ['rxiao@mail.med.upenn.edu'], 
    ['sxie@mail.med.upenn.edu'], 
    ['dxie@upenn.edu'], 
    ['weiyang@mail.med.upenn.edu']]
    writer.writerows(data)