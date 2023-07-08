import requests
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
linkedin_profile_url = 'https://www.linkedin.com/in/tanmoy-barman-22693a270'
api_key = 'YOUR_API_KEY'
headers = {'Authorization': 'Bearer ' + api_key}

response = requests.get(api_endpoint,
                        params={'url': linkedin_profile_url,'skills': 'include'},
                        headers=headers)

profile_data = response.json()
profile_data

profile_data['full_name']
profile_data['occupation']