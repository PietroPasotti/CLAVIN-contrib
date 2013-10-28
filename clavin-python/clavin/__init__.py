import requests 
from collections import Counter
from pprint import pprint


class Clavin:

    def __init__(self, server):
        self.server = server

    def locationsDictionary(self):
        return self.dict_format['locations']

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
        self.result = Result(results)
        self.dict_format = results
        return self.result

    def __unicode__(self):
        formatted = u"{name}\t{countryName}\t"
#admin 1 code: {admin1Code}\tpop: {population}\tid: {geonameID}\n"
	as_unicode = [loc.name for loc in self.result.locations]
	return as_unicode

    def whichCountries(self):
        countries = [location.countryName for location in self.locations]
        howmany = Counter(countries)
        for country,occs in howmany.iteritems():
           print("{}\t\t\t\t{} times".format(country,occs))
        return howmany  

    def locationsByCountry(self):
        loc_by_country = {}
        for country in set([location.countryName for location in self.locations]):
            loc_by_country[country] = list(set([location.name for location in self.locations if location.countryName == country]))
#This does not actually print very pretty
#       pprint(loc_by_country)  
        return loc_by_country
        


#    def __unicode__(self):    


class Location:

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
#        formatted = u"{self.name}\t{self.countryName}\tadmin 1 code: {self.admin1Code}\tpop: {self.population}\tid: {self.geonameID}\n"
        return u"{}\t{}\tadmin 1 code: {}\tpop: {}\tCLAVIN-id: {}".format(self.name, self.countryName, self.admin1Code, self.population, self.geonameID)



class Result:

    def __init__(self,result):
        self.version = result['version']
        self.locations = [Location(record) for record in result['locations']]

    def __unicode__(self):
        u_str = "Clavin version {}\n".format(self.version)
        for loc in self.locations:
            u_str+=(unicode(loc)+"\n")
        return u_str
