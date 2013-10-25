import requests 
from collections import Counter
from pprint import pprint


class Clavin:

    def __init__(self, server):
        self.server = server
        self.resolved = {}


    def locationsDictionary(self):
        return self.resolved['locations']

    def whichClavin(self):
        return self.version
        
#    def parse(self, document):
    #def connect(self, server):
    #    self.server = server 
    #    # connect to web server, should return basic metadata to verify it is working 

    def resolve(self, document):
        headers = {'content-type': 'text/plain'}
        r = requests.post(self.server, data=document, headers=headers)
        results = r.json()
        self.resolvedLocations = [resolvedLocation(record) for record in results['locations']]
        self.version = results['version']
        self.resolved = results
        return results

    def toString(self):
        formatted = u"{name}\t{countryName}\tadmin 1 code: {admin1Code}\tpop: {population}\tid: {geonameID}\n"
        resolved = self.resolved['locations']
        for loc in resolved:
            print formatted.format(**loc)

    def whichCountries(self):
        countries = [location.countryName for location in self.resolvedLocations]
        howmany = Counter(countries)
        for country,occs in howmany.iteritems():
           print("{}\t\t\t\t{} times".format(country,occs))
        return howmany  

    def locationsByCountry(self):
        loc_by_country = {}
        for country in set([location.countryName for location in self.resolvedLocations]):
            loc_by_country[country] = list(set([location.name for location in self.resolvedLocations if location.countryName == country]))
#This does not actually print very pretty
#       pprint(loc_by_country)  
        return loc_by_country
        


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

 
