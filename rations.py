rasjon = open('food_rations.txt','r').read().split(',')

tall = list((int(x) for x in rasjon))

behov = 50
sultne_dager = 0
overført = 0
dag = 0

for mat in tall:
  dag += 1
  total_mat = mat + overført
  if behov > total_mat:
    sultne_dager += 1
    behov -= 1
    overført = 0
  else:
    sultne_dager = 0
    overført = total_mat - behov
    behov += 1
  if sultne_dager > 4:
    break

print(len(tall))
print(dag - 1)