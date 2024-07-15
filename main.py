import requests






def main():
    # Replace 'your_api_key' with your actual Crunchbase API key
    api_key = 'fb0d99c37b57c59790aeb5dd0134c2c1'
    base_url = 'https://api.crunchbase.com/api/v4/entities'
    entity_id = '8villages'  # Replace with the specific entity ID you want to query

    # Headers for the API request
    headers = {
        'X-CB-User-Key': api_key,
        'Content-Type': 'application/json'
    }

    # Construct the URL for the API request
    url = f'{base_url}/organizations/{entity_id}'

    # Send the GET request
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()  # Get the response data in JSON format
        print(data)
    else:
        print(f'Error: {response.status_code} - {response.text}')




if __name__ == "__main__":
    main()