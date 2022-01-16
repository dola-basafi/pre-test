i = 1 
stat = 1 
while i > 1 or stat == 1 :   
  if i == 1: 
   print("HITUNG MAJU") 
  elif i == 21 : 
   print("HITUNG MUNDUR") 
   stat = -1 
  elif i%2==0 : 
   print(i) 
  i += stat
