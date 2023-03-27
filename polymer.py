polymer = open('polymer.txt','r').read()

units = list((x for x in polymer))

react = True
while react:
  react = False
  for i in range(len(units) - 1):
    if abs((ord(units[i]) - ord(units[i + 1]))) == 32:
      del units[i + 1]
      del units[i]
      react = True
      break

print(len(units))