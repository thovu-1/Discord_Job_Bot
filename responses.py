from random import choice, randint
import requests
import json
import os

def get_response(user_input: str) -> str:
    text: str = user_input.lower()

    if text == 'hello':
        return 'Hello There!'
    elif 'jobs' in text:

        search: str = 'developer'  # Default search
        if len(text) > 4:
            search = text[5:]  # Dynamic search

        url = "https://indeed12.p.rapidapi.com/jobs/search"

        querystring = {"query": search, "location": "saskatoon", "page_id": "1", "locality": "ca", "fromage": "14",
                       "radius": "50", "sort": "date"}
        headers = {
            "X-RapidAPI-Key": os.getenv('RapidAPI_Key'),
            "X-RapidAPI-Host": os.getenv('RapidAPI_Host')
        }

        response = requests.get(url, headers=headers, params=querystring)

        data = json.loads(response.text)
        # print(json.dumps(data, indent=4))
        final_link = ''

        if data['indeed_final_url']:
            final_link = data['indeed_final_url']

        # print("HITS HERE")
        # print(json.dumps(data['hits'], indent=4))

        jobs = data['hits']

        msg = 'A List of ' + search + ' jobs from up to 14 days ago\n' + final_link + '\n\n'
        for job in jobs:
            company: str = 'Company: ' + job['company_name']
            title: str = 'Title: ' + job['title']
            salary: str = ''
            link: str = ('https://ca.indeed.com/jobs?q=developer&l=saskatoon&fromage=14&radius=50&sort=date&vjk=' +
                         str(job['id']))
            if job['salary']:
                tempsalary = job['salary']

                if tempsalary['min'] == tempsalary['max']:
                    minsalary: str = str(tempsalary['min'])
                    frequency: str = str(tempsalary['type'])

                    salary = 'Salary: $' + str(minsalary) + '\t' + 'Type: ' + frequency
                else:
                    minsalary: str = str(tempsalary['min'])
                    maxsalary: str = str(tempsalary['max'])
                    frequency: str = str(tempsalary['type'])

                    salary = 'Salary: $' + minsalary + '-' + maxsalary + '\t' + 'Type: ' + frequency

            if len(msg) < 1900:
                if job['salary']:
                    temp = title + '\n' + company + '\n' + salary + '\n' + link + '\n\n'

                else:
                    temp = title + '\n' + company + '\n' + link + '\n\n'

                msg += temp
            else:
                return msg + '\nRan out of room... Visit:' + final_link
        return msg
    else:
        return choice(['English mother father do you speak it...',
                       'Damn that\'s crazy...',
                       'wat?'])
