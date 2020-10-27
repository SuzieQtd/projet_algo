# from matplotlib import pyplot as plt
#
#
# humidex = T + h
# h = #humidité relative en pourcentage
#
# plt.plot()
# plt.show()

# import xlrd
#import panda as pd

# document = xlrd.open_workbook(r'''C:\\Users\\aachi\\Desktop\\projet_algo\\EIVP_KM.csv''')
#
# print("Nombre de feuilles: "+str(document.nsheets))
# print("Noms des feuilles: "+str(document.sheet_names()))

path="C:\\Users\\aachi\\Desktop\\projet_algo\\EIVP_KM.csv"
import csv
objetFichier=open(path,'rb')
objetcsv=csv.writer(objetFichier,delimiter=';')
print (objetcsv)

# lst=[]
# for row in objetcsv:
#     lst.append(row)
# lst = list(objetcsv)

"""id=[]
noise=[]
temp=[]
hum=[]
lum=[]
co2=[]
tps=[] 


for i in range(1, len(doc[0])):
    id.append(doc[0][i])
    noise.append(doc[1][i])
    temp.append(doc[2][i])
    hum.append(doc[3][i])
    lum.append(doc[4][i])
    co2.append(doc[5][i])
    tps.append(doc[6][i])
  
def sepdate():
    date1=''
    date=[]
    for j in range(0,10):
        date1.join(tps[j-1])
    for i in range(len(date1)):
        date.append(date1[i])
    return date
 
print(sepdate())


tps1=[]
tps2=[]
tps3=[]
tps4=[]
tps5=[]
tps6=[]
for i in range(len(tps)):
    if id[i]=='1':
        tps1.append(tps[i])
    elif id[i]=='2':
        tps2.append(tps[i])
    elif id[i]=='3':
        tps3.append(tps[i])
    elif id[i]=='4':
        tps4.append(tps[i])
    elif id[i]=='5':
        tps5.append(tps[i])
    else:
        tps6.append(tps[i])
print(tps1) """
