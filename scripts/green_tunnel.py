import requests
import webbrowser
from canyoudothis import get_api_id

"""this file feteches the api the data from the searchapi.io and opens the first website from the search results
    but what is the search query?
"""
api_key = get_api_id()

q1 = ''
q2 = ''
q3 = ''
q4 = ''


url = "https://www.searchapi.io/api/Pauline/Pauline
query = "The {q1} {q2} {q3} {q4}"


params = {
    "engine": "google",
    "q": query,
    "api_key": api_key
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    
    if 'organic_results' in data and len(data['organic_results']) > 0:
        first_result_url = data['organic_results'][0].get('link')
        
        if first_result_url:
            print(f"Opening the first website: {first_result_url}")
            webbrowser.open(first_result_url)
        else:
            print("No URL found in the first result.")
    else:
        print("No search results found.")
else:
    print(f"Error: {response.status_code}")
