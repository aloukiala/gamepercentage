import requests

dataset = None
percentage = None

def get_vakio_data():
	url = 'https://www.veikkaus.fi/api/v1/sport-games/draws?game-names=MULTISCORE'
	headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'X-ESA-API-Key': 'ROBOT'}
	response = requests.get(url, headers=headers)
	dataset = response.json()

def parse_percentages(row_id):
	percentage['resultPopularityDTOs']

def parse_rows(rows):
	for row in rows:
		hometeam = row['outcome']['home']['name']
		awayteam = row['outcome']['away']['name']
		row_id = row['outcome']['away']['id']
		percentages = parse_percentage(row_id)
		print(hometeam + ' - ' + awayteam)


def get_draws():
	for draw in dataset['draws']:
		if draw['status'] == 'OPEN':
			print(draw['name'])
			print('-----------------------------')
			print(draw)['rows']
			parse_rows(draw['rows'])


def get_percentage(game_id):
	url = 'https://www.veikkaus.fi/api/v1/sport-games/draws/SPORT/'+ game_id +'/popularity'
	response = requests.get(url)
	percentage = response.json()


def main():
	get_vakio_data()
	get_draws()
	get_percentage()

if __name__ == "__main__":
    main()