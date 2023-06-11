import csv
import pandas as pd
rows=[]
with open ('Data3.csv','r') as f:
  csv_reader = csv.reader(f)
  for row in csv_reader:
    rows.append(row)
Data = rows[1:]    
new_planet_data = []
for a in Data:
  
  if a == []:
    continue
  else:
    if a[8]== 'Unknown':
     continue
    if a[7]=='Unknown':
     continue
  
  new_planet_data.append(a)
  
print(len(new_planet_data))    



star_mass = []
star_radius = []
star_name=[]

for j in new_planet_data:
  
  if j == []:
    continue
  else:
    if j[8]== 'Unknown':
     continue
    elif j[8]=='':
      continue
    else:
      radius_value = j[8]
      star_radius.append(radius_value)
    if j[7]=='Unknown':
     continue
    elif j[7]=='':
      continue
    else:
      mass_value = j[7]
      star_mass.append(mass_value)
    if j[0]=='':
      continue
    else:
      star = j[0]
      star_name.append(star)

  
  
  #if a == []: 
   # continue



    

star_gravity = []
for index, name in enumerate(star_name):
    gravity = float(star_mass[index])*6.957e+8/((float(star_radius[index]))*1.989e+30)**2
    star_gravity.append(gravity)
print(star_gravity)

