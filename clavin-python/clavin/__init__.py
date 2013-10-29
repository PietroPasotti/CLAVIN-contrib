import requests 
from collections import Counter

class Clavin:
    """CLAVIN (Cartographic Location And Vicinity INdexer)
        Copyright (C) 2012-2013 Berico Technologies
        http://clavin.bericotechnologies.com"""

    def __init__(self, server):
        self.server = server

    def resolve(self, document):
        headers = {'content-type': 'text/plain'}
        r = requests.post(self.server, data=document, headers=headers)
        results = r.json()
        self.dict_format = results
        self.result = Result(results)
        return self.result

    def __unicode__(self):
        return "Python-Clavin at {}".format(self.server)

    def __str__(self):
        return unicode(self).encode('utf-8')

    def whichClavin(self):
        return self.result.version

# TODO:        
#    def parse(self, document):

class Location:
    """A class to store the data fields returned from the server for resolved locations"""

    def __init__(self,record):
        self.geonameID = record['geonameID']
        self.name = record['name']
        self.countryName = record['countryName']
        self.admin1Code = record['admin1Code']
        self.locationText = record["locationText"]
        self.locationPosition = record["locationPosition"]
        self.fuzzy = record["fuzzy"]
        self.confidence = record["confidence"]
        self.population = record['population']
        self.latitude = record['latitude']
        self.longitude = record['longitude']

    def __unicode__(self):
        return u"{}\t{}\tadmin 1 code: {}\tpop: {}\tCLAVIN-id: {}".format(self.name, self.countryName, self.admin1Code, self.population, self.geonameID)

    def __str__(self):
        return unicode(self).encode('utf-8')

class Result:
    """A class to store the CLAVIN version and list of resolved Location objects"""

    def __init__(self,result):
        self.version = result['version']
        self.locations = [Location(record) for record in result['locations']]

    def __unicode__(self):
        u_str = "Clavin version {}\n".format(self.version)
        for loc in self.locations:
            u_str+=(unicode(loc)+"\n")
        return u_str

    def __str__(self):
        return unicode(self).encode('utf-8')

    def whichCountries(self):
        countries = [location.countryName for location in self.locations]
        howmany = Counter(countries)
        return howmany  

    def locationsByCountry(self):
        loc_by_country = {}
        for country in set([location.countryName for location in self.locations]):
            loc_by_country[country] = list(set([location.name for location in self.locations if location.countryName == country])) 
        return loc_by_country




