import requests as rq
import json

def json_format(raw):
    text = json.dumps(raw, sort_keys= True, indent= 4)
    return text

ip = input("Iveskite norima Ip adresa: ")
raktas = "df6062b8305ba0956d2c5607b07daa13"
response = rq.get("http://api.ipstack.com/" +ip + "?access_key=" + raktas)
print(response.status_code)
print(json_format(response.json()))

# pasiimti kazkuri api ir is jo issitraukti, konvertuoti, atsispausdinti78.57.253.53
