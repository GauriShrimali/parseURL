import re
text = open("text.txt","r")
txt = text.read()

url = 'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
for line in txt:
    occ = re.findall(url,txt)

if len(occ) == 0:
    print("No URL present")
else:
    print("\nTotal URLs: ",len(occ))
    print("\nFirst URL: ",occ[0])
    print("\nAll URLs: ")
    for i in occ:
        print(i)