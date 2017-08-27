import csv
import requests
import json

def pretty_print(json_obj):
    return json.dumps(json_obj, indent=4)

def planet_request(planet=None):
    planet1 = "http://swapi.co/api/planets/{}/".format(planet)
    p1_req = requests.get(planet1).json()

    return p1_req

#planet_request()

def get_residents_name(i):
    p1_res = planet_request(i)
    p1_name = p1_res['name']
    return p1_name

def get_all_residents_of_planet_1():
    for i in range(1,62):
        p1_res = planet_request(i)
        #print(pretty_print(p1_res))

        p1_name = get_residents_name(i)
        p1_url = p1_res['url']

        output_list = [p1_name, p1_url]

        res_urls = p1_res['residents']
        #print(pretty_print(res_urls))
        for url in res_urls:
            resident_res = requests.get(url).json()

            resident_name = resident_res['name']
            output_list.append(resident_name)
        

        with open('planet_pop4.csv', 'a') as planet_pop:
            planet_writer = csv.writer(planet_pop)
            planet_writer.writerow(output_list)

get_all_residents_of_planet_1()
