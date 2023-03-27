id = open('duplicates.txt','r').read().split()
tall = list((int(x) for x in id))

total = 0

unik = []
for i in tall:
  if i not in unik:
    unik.append(i)
  else:
    total += 1

print(f"{total} mail kan slettes.")