import requests
import logging

logging.basicConfig(filename='scriptlog.log', level=logging.INFO)
print '\n';
print '*********Welcome to the Nuage Test App**********';
print '*****Enter 1 to get the url of the App*****';
print '*****Enter 2 to post to the App*****';
print '*****Enter 3 to put the data to the App*****';
print '*****Enter 4 to delete the data from the App*****';
print '***********Enter 5 to quit****************';

url = 'http://localhost'
option = input('Enter an integer between 1 and 5 \t');
logging.info('Option entered \t' + str(option))

while (option != 5):

	if option == 1:
		response = requests.get(url)
		print '\n' + response.url
	else:
		nid = input('\nEnter the id \t');
		nname = input('Enter the name within quotes \t');
		body = {'pid': nid, 'name': nname}

	if option == 2:		
		requests.post(url, data=body)	
		logging.info('Posted: \t' + 'id ' + str(body['pid']) + 'Name is ' + body['name'])	
		
	if option == 3:		
		requests.put(url, data=body)

	if option == 4:		
		requests.delete(url, data=body)
		logging.info('Deleted: \t' + 'id ' + str(body['pid']) + 'Name is ' + body['name'])	


	print '\n';
	print '*****Enter 1 to get the url of the App*****';
	print '*****Enter 2 to post to the App*****';
	print '*****Enter 3 to put the data to the App*****';
	print '*****Enter 4 to delete the data from the App*****';
	print '***********Enter 5 to quit****************';
	option = input('Enter an integer between 1 and 5 \t');
	logging.info('Next entered \t' + str(option))


