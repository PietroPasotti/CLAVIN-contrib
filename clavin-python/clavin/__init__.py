import requests 
import code
import json


class Clavin:

    def __init__(self, server):
        self.server = server
        self.results = {}


    def locationsDictionary(self):
        return self.results['locations']

    def whichClavin(self):
        return self.version
        


    #def connect(self, server):
    #    self.server = server 
    #    # connect to web server, should return basic metadata to verify it is working 

    def resolve(self, document):
        headers = {'content-type': 'text/plain'}
        r = requests.post(self.server, data=document, headers=headers)
        results = r.json()
        self.resolvedLocations = [resolvedLocation(record) for record in results['locations']]
        self.version = results['version']
        self.results = results
        return results

    def toString(self):
        formatted = u"{name}\t{countryName}\t{admin1Code}\t[pop: {population}]\tid: {geonameID}\n"
        resolved = self.results['locations']
        for loc in resolved:
            print formatted.format(**loc)

    def whichCountries(self):
        return list(set(location.countryName for location in self.resolvedLocations)) 


#    def __unicode__(self):    


class resolvedLocation:

    def __init__(self,record):
        self.name = record['name']
        self.countryName = record['countryName']
        self.admin1Code = record['admin1Code']
        self.population = record['population']
        self.geonameID = record['geonameID']
        self.latitude = record['latitude']
        self.longitude = record['longitude']

 
