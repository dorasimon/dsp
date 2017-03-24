import csv

with open("emails.csv", "w") as file:
    fieldnames = ["email"]
    writer = csv.DictWriter(file, fieldnames = fieldnames)

    writer.writeheader()
    writer.writerow({"email": 'bellamys@mail.med.upenn.edu'})
    writer.writerow({"email": 'warren@upenn.edu'})
    writer.writerow({"email": 'bryanma@upenn.edu'})
    writer.writerow({"email": 'jinboche@upenn.edu'})
    writer.writerow({"email": 'sellenbe@upenn.edu'})
    writer.writerow({"email": 'jellenbe@mail.med.upenn.edu'})
    writer.writerow({"email": 'ruifeng@upenn.edu'})
    writer.writerow({"email": 'bcfrench@mail.med.upenn.edu'})
    writer.writerow({"email": 'pgimotty@upenn.edu'})
    writer.writerow({"email": 'wguo@mail.med.upenn.edu'})
    writer.writerow({"email": 'hsu9@mail.med.upenn.edu'})
    writer.writerow({"email": 'rhubb@mail.med.upenn.edu'})
    writer.writerow({"email": 'whwang@mail.med.upenn.edu'})
    writer.writerow({"email": 'mjoffe@mail.med.upenn.edu'})
    writer.writerow({"email": 'jrlandis@mail.med.upenn.edu'})
    writer.writerow({"email": 'liy3@email.chop.edu'})
    writer.writerow({"email": 'mingyao@mail.med.upenn.edu'})
    writer.writerow({"email": 'hongzhe@upenn.edu'})
    writer.writerow({"email": 'rlocalio@upenn.edu'})
    writer.writerow({"email": 'nanditam@mail.med.upenn.edu'})
    writer.writerow({"email": 'knashawn@mail.med.upenn.edu'})
    writer.writerow({"email": 'propert@mail.med.upenn.edu'})
    writer.writerow({"email": 'mputt@mail.med.upenn.edu'})
    writer.writerow({"email": 'sratclif@upenn.edu'})
    writer.writerow({"email": 'michross@upenn.edu'})
    writer.writerow({"email": 'jaroy@mail.med.upenn.edu'})
    writer.writerow({"email": 'msammel@cceb.med.upenn.edu'})
    writer.writerow({"email": 'shawp@upenn.edu'})
    writer.writerow({"email": 'rshi@mail.med.upenn.edu'})
    writer.writerow({"email": 'hshou@mail.med.upenn.edu'})
    writer.writerow({"email": 'jshults@mail.med.upenn.edu'})
    writer.writerow({"email": 'alisaste@mail.med.upenn.edu'})
    writer.writerow({"email": 'atroxel@mail.med.upenn.edu'})
    writer.writerow({"email": 'rxiao@mail.med.upenn.edu'})
    writer.writerow({"email": 'sxie@mail.med.upenn.edu'})
    writer.writerow({"email": 'dxie@upenn.edu'})
    writer.writerow({"email": 'weiyang@mail.med.upenn.edu'})