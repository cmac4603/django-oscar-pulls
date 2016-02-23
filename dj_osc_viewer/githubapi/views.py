from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# url & parameters for github api json request
url = 'https://api.github.com/repos/django-oscar/django-oscar/pulls'
params = {'sort': 'updated', 'direction': 'desc'}

# main page view
def index(request):
    resp = requests.get(url=url, params=params)
    data = json.loads(resp.text)
    titlekeys = []
    titlevalues = []
    titlelist = []
    titledict = {}
    createdkeys = []
    createdvalues = []
    createdlist = []
    createddict = {}
    updatedkeys = []
    updatedvalues = []
    updatedlist = []
    updateddict = {}
    webdict = {}
    weblist = []
# creates keys list for final dictionary
    for i in range(1,31):
        titlekeys.append('t'+str(i))
        createdkeys.append('c'+str(i))
        updatedkeys.append('u'+str(i))
# creates values list for final dictionary
    for i in range(-30,0):
        titlevalues.append(data[i]["title"])
        createdvalues.append(data[i]["created_at"])
        updatedvalues.append(data[i]["updated_at"])
# creation of title/created_at/updated_at dictionaries
    titlelist = list(zip(titlekeys, titlevalues))
    createdlist = list(zip(createdkeys, createdvalues))
    updatedlist = list(zip(updatedkeys, updatedvalues))

    for (k,v) in zip(titlekeys, titlevalues):
        titledict[k] = v

    for (k,v) in zip(createdkeys, createdvalues):
        createddict[k] = v

    for (k,v) in zip(updatedkeys, updatedvalues):
        updateddict[k] = v
# creation of final dictionary returned
    webdict = titledict.copy()
    webdict.update(createddict)
    webdict.update(updateddict)
    weblist.append(webdict)
    context = {'data' : weblist}
    return render(request, 'githubapi/index.html', context)
