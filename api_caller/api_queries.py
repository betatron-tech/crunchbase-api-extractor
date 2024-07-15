import requests
from global_methods import read_txt, load_yaml_config
from logger.logger import Logger


class CrunchbaseExtractor:
    def __init__(self):
        print("SETUP OF CRUNCHBASE EXTRACTOR")
        config = load_yaml_config('config/config.yaml')
        self.api_key = config['CRUNCHBASE_API_KEY']
        self.base_url = 'https://api.crunchbase.com/api/v4'

    def get_organization_data(self, entity_id):
        headers = {
            'X-CB-User-Key': self.api_key,
            'Content-Type': 'application/json'
        }
        url = f'{self.base_url}/entities/organizations/{entity_id}'
        print(f"URL: {url}")
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()  # Get the response data in JSON format
            print(data)
        else:
            print(f'Error: {response.status_code} - {response.text}')

