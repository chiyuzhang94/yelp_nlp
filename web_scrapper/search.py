#use Yelp API to seach business and return search results
'''
API in https://www.yelp.com/developers/documentation/v3/business_search
input: term, location
output: json file
'''
import json
import requests
import datetime
def askapi(LOCATION, TERM, OFFEST):
	CLIENT_ID = 'P_S1kyi0U1AnItJwJG6mCw'
	CLIENT_SECRET = '3gtLp1DZ7jgiVvYKcXHHRoxlDiShlD0BI6w04L1XaMLZn1eDevZCrQbWiKlJDXls'
	OFFSET_NUM = OFFEST
	SEARCH_LIMIT = 50
	lim = 1000-OFFSET_NUM
	if lim < 50:
		SEARCH_LIMIT = lim
	data = {'grant_type': 'client_credentials',											
	        'client_id': CLIENT_ID,														
	        'client_secret': CLIENT_SECRET}												
	token = requests.post('https://api.yelp.com/oauth2/token', data=data)				
	access_token = token.json()['access_token']											
	url = 'https://api.yelp.com/v3/businesses/search'									
	headers = {'Authorization': 'bearer %s' % access_token}								
	# Yelp v3 API: https://nz.yelp.com/developers/documentation/v3                      
	params = {														
			  'location': LOCATION,												
			  'term': TERM,												
			  'limit': SEARCH_LIMIT,
			  'offset': OFFSET_NUM}	

	response = requests.get(url=url, params=params, headers=headers)					

	results = response.json()['businesses']
	return results
def outpt(now, term, location,search):
    filename = str(now.month).zfill(2) + str(now.day).zfill(2) + '_' + term + '_' + location.replace(" ", "").replace(",","")
    with open(''+filename+'.txt', 'w') as f:
        json.dump(search, f, ensure_ascii=True)

count = 0
resultslist = []
now = datetime.datetime.now()
term = 'restaurants'
location = 'New York, NY'

for i in range(20):
	
	offset_num = i*50+1
	answer = askapi(location,term,offset_num)
	for item in answer:
		resultslist.append(item)
	count += len(answer)
	print 'Get ' + str(count) + ' results'

outpt(now,term,location,resultslist)

print "Total number of results:" + str(count)

