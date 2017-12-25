import json
from pprint import pprint

filename = 'yourfilename'
f = open(filename, 'r')
for line in f:
    data = json.loads(line)
    #pprint(data['imp'][0]['native']['request'])
    #print(type(data['imp'][0]['native']))
    
    if data.has_key('imp') and data['imp'][0].has_key('native'):    
        try:
            request = data['imp'][0]['native']['request']
            if isinstance(request, dict) == False:
	        print(line.encode('utf8'))
	        print('is not dict')
                break
	except Exception as e:
	    print(e)
	    #print(str(data['imp'][0]['native']['request']).encode('utf8'))
	    #print(line.encode('utf8'))
	    break
print('******************* end ***********************')
