import requests
import json

def queryRESTAPI():
    
    url = "https://jsonmock.hackerrank.com/api/countries"
    query = {'name':'Afghanistan'}

    try:
            
        response = requests.get(url, params=query, timeout=5)

        response.raise_for_status()
    
    except requests.exceptions.HTTPError as errh:
        print(errh)

    except requests.exceptions.ConnectionError as errc:
        print(errc)

    except requests.exceptions.Timeout as errt:
        print(errt)

    except requests.exceptions.RequestException as err:
        print(err)
        

    # json.loads take a string or byte data and convert it into a json object
    data = json.loads(response.text)

    # converts a json object into json formatted string with the given indent level
    # It basically pretty print the json data

    formatted_data = json.dumps(data,indent=2)
    print(formatted_data)


    print(data['data'][0]['capital'])
    capital_city = data['data'][0]['capital']
    if capital_city!='':
        return -1
    else:
        return capital_city

queryRESTAPI()



