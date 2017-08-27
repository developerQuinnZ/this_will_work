import csv
import requests
import json

def pretty_print(json_obj):
    return json.dumps(json_obj, indent=4)

def get_all_pages():
    page_list = []
    for i in range(1,10):
        page = "http://swapi.co/api/people/?page={}".format(i)
        page_list.append(page)
    return page_list
    

def people_request():
    page_list = get_all_pages()
    people_list = []
    for page in page_list:
        this_page = page
        page_req = requests.get(this_page).json()

        for p in range(0,len(page_req["results"])):
            name = page_req['results'][p]['name']
            people_list.append(name)
           
        
    
    return people_list

people_request()
