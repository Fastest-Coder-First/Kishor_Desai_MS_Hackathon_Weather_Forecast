#Author:Kishor K Desai
#Email: kishord.bsc22@rvu.edu.in
#Phone No: 8277753033

#The API Key is generated from https://www.weatherapi.com/
apikey='45204c2cce3a4bea8da44728232406'

#Importing the required modules
import requests as r
import json
from tabulate import tabulate 

while True:
    def main(city): 
            #Function to get the weather details of the city
            def getWeather(city):
                # current_url=f"http://api.weatherapi.com/v1/current.json?key={apikey}&q={city}"
                # current_data=r.get(current_url)
                url_forecast_data = f"http://api.weatherapi.com/v1/forecast.json?key={apikey}&q={city}&days=3"
                forecast_data = r.get(url_forecast_data)
                return forecast_data.json()
            
            
            #Extracting the forecast details of the city
            result = getWeather(city)
            forecast=result['forecast']['forecastday'][0]

            #Parsing the Required Data from the JSON
            table1=[["Temperature","Feels Like","Condition","Humidity","Wind Speed","Wind Direction"],
                [
                    f"{result['current']['temp_c']}C/{result['current']['temp_f']}F",
                    f"{result['current']['feelslike_c']}C/{result['current']['feelslike_f']}F",
                    f"{result['current']['condition']['text']}",
                    f"{result['current']['humidity']}",
                    f"{result['current']['wind_kph']}KPH/{result['current']['wind_mph']}MPH",
                    f"{result['current']['wind_dir']}",
            ]
            ]
            #Printing the Current Weather Details
            print(f"\n  Current Weather Details of {result['location']['name']},{result['location']['region']},{result['location']['country']}:")
            print(tabulate(table1,stralign='center',tablefmt='fancy_grid'))



            #Parsing the Required Data from the JSON
            table2 = [[f"\tMax Temperature", "Min Temperature", "Condition", "Humidity", "Chance of Rain", "Precipitation"],
                    [f"{forecast['day']['maxtemp_c']}C/{forecast['day']['maxtemp_f']}F",
                    f"{forecast['day']['mintemp_c']}C/{forecast['day']['mintemp_f']}F",
                    forecast['day']['condition']['text'],
                    forecast['day']['avghumidity'],
                    f"{forecast['day']['daily_chance_of_rain']}%",
                    f"{forecast['day']['totalprecip_mm']} mm"]]
            #Printing the Current Weather Details
            print("\n\n  Forecast Details:")
            print(tabulate(table2,stralign='center',tablefmt='fancy_grid'))



            #Parsing the Required Data from the JSON
            table3=[
                [f"\tSunrise Time","Sunset Time","Moonrise Time","Moonset Time"],
                [forecast['astro']['sunrise'],forecast['astro']['sunset'],forecast['astro']['moonrise'],forecast['astro']['moonset']]
                ]
            #Printing the Current Weather Details
            print("\n\n  Astro Details:")
            print(tabulate(table3,stralign='center',tablefmt='fancy_grid'))
    
    def check():
        if __name__=='__main__':
            city=input("\n  Enter the City Name: ")
            #Error Handling
            try:
                city==int(city)
                print("\n  Invalid Input : City Name should be a String")
                check()
            except:
                main(city)
               
    
    check()
    break
