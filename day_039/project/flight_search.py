import requests
import os 
from datetime import datetime

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.api_key = os.environ.get("FLIGHTS_API_KEY")
        self.api_secret = os.environ.get("FLIGHTS_API_SECRET")
        self._token = self._get_new_token()


    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
            }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self.api_key,
            'client_secret': self.api_secret
        }
        try:
            response = requests.post(url="https://test.api.amadeus.com/v1/security/oauth2/token", headers=header, data=body)
        except:
            print("Failed to get a response from ")
            return "" 
        else:
            return response.json()['access_token']
        

    def get_destination_code(self, city_name):
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(
            url= "https://test.api.amadeus.com/v1/reference-data/locations/cities",
            headers=headers,
            params=query
        )
        
        print(f"Status code {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):

        # print(f"Using this token to check_flights() {self._token}")
        headers = {"Authorization": f"Bearer {self._token}"}
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "GBP",
            "max": "10",
        }

        response = requests.get(
            url="https://test.api.amadeus.com/v2/shopping/flight-offers",
            headers=headers,
            params=query,
        )

        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("Response body:", response.text)
            return None

        return response.json()