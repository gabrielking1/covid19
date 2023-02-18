import requests
import json
from app.models import Worlds, Country


def worker():

    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/world"

    headers = {
	"X-RapidAPI-Key": "148de2c9d7mshb66037a0a2757e3p12e732jsn8bdf81c925cf",
	"X-RapidAPI-Host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    data = response.json()
    for item in data:
        Worlds.objects.filter(world_id=item['id']).update_or_create(
        world_id = item['id'],
        country = item['Country'],
        RecoveryProporation = item['Recovery_Proporation'],
        TotalCases = item['TotalCases'],
        NewCases = item['NewCases'],
        TotalDeath = item['TotalDeaths'],
        NewDeath =  item['NewDeaths'],
        TotalRecovered  = item['TotalRecovered'],
        NewRecovered = item['NewRecovered'],
        ActiveCases = item['ActiveCases'],
        SeriousCritical = item['Serious_Critical']
        )

   
    url = "https://vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com/api/npm-covid-data/"

    headers = {
	"X-RapidAPI-Key": "148de2c9d7mshb66037a0a2757e3p12e732jsn8bdf81c925cf",
	"X-RapidAPI-Host": "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    dataa = response.json()
    for item in dataa:
        Country.objects.filter(country_id=item['id']).update_or_create(
        country_id = item['id'],
        rank = item['rank'],
        country = item['Country'],
        continent = item['Continent'],
        TotalTests = item['TotalTests'],
        Population = item['Population'],
        RecoveryProporation = item['Recovery_Proporation'],
        TotalCases = item['TotalCases'],
        NewCases = item['NewCases'],
        TotalDeath = item['TotalDeaths'],
        NewDeath =  item['NewDeaths'],
        TotalRecovered  = item['TotalRecovered'],
        NewRecovered = item['NewRecovered'],
        ActiveCases = item['ActiveCases'],
        SeriousCritical = item['Serious_Critical'],
        Fatality = item['Case_Fatality_Rate']
        )

