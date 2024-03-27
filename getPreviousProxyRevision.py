import sys,json
#print ('argument list', sys.argv)
fileName = sys.argv[1]
with open(fileName) as user_file:
  parsed_json = json.load(user_file)
revisionsInt = []
for rev in parsed_json["revision"]:
    revisionsInt.append(int(rev))
revisionsInt.sort(reverse = True)
if len(revisionsInt) > 1:
  print(revisionsInt[1])
else:
  print(1)