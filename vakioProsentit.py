import requests

dataset = None
percentage = None

def get_dataset():
	return dataset

def get_vakio_data():
	global dataset
	url = 'https://www.veikkaus.fi/api/v1/sport-games/draws?game-names=SPORT'
	headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'X-ESA-API-Key': 'ROBOT'}
	response = requests.get(url, headers=headers)
	dataset = response.json()

def parse_percentages(row_id):
	global percentage
	games = percentage['resultPopularityDTOs']
	id_list_perc = list(filter(lambda d: d['eventId'] in row_id, games))
	percentages = {}
	for team in id_list_perc:
		if team['away'] == True:
			percentages['away'] = team['percentage']
		elif team['home'] == True:
			percentages['home'] = team['percentage']
		elif team['tie'] == True:
			percentages['tie'] = team['percentage']
	print(percentages)
	return percentages


def parse_rows(rows):
	for row in rows:
		hometeam = row['outcome']['home']['name']
		awayteam = row['outcome']['away']['name']
		row_id = row['id']
		percentages = parse_percentages(row_id)
		print(row_id)
		print(hometeam + ' - ' + awayteam)
		print(str(percentages['home']) + ' - ' + str(percentages['tie']) + ' - ' + str(percentages['away']))

def get_draws():
	for draw in dataset['draws']:
		if draw['status'] == 'OPEN':
			print(draw['id'])
			get_percentage(draw['id'])
			print(draw['name'])
			print('-----------------------------')
			# print(draw)['rows']
			parse_rows(draw['rows'])


def get_percentage(game_id):
	global percentage
	url = 'https://www.veikkaus.fi/api/v1/sport-games/draws/SPORT/'+ game_id +'/popularity'
	headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'X-ESA-API-Key': 'ROBOT'}
	response = requests.get(url)
	percentage = response.json()
	print(percentage)

def main():
	get_vakio_data()
	get_draws()
	## get_percentage()

if __name__ == "__main__":
    main()