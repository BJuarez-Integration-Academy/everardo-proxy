import sys,json
#print ('argument list', sys.argv)
fileName = sys.argv[1]
with open(fileName) as user_file:
  parsed_json = json.load(user_file)
print(len(parsed_json["revision"]))