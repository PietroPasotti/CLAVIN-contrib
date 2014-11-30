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
        try:
            results = r.json()
        except Exception as e:
            global output
            output = r # at least we won't lose it all
            print('Json went astray. Request saved in global "output".')
            raise e
            
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
        
        for key,value in record.items():
            setattr(self, key, value)
        
        return
        
    def __unicode__(self):
        return u"{}\t{}\tadmin 1 code: {}\tpop: {}\tCLAVIN-id: {}".format(self.name, self.matchedName, self.admin1Code, self.population, self.geonameID)

    def __str__(self):
        return unicode(self).encode('utf-8')

class Result:
    """A class to store the CLAVIN version and list of resolved Location objects"""

    def __init__(self,res):
        try:
            #self.version = res['version'] # no 'version' is specified in the result!!
            self.locations = [Location(record) for record in res['resolvedLocations']]
        except Exception as e:
            print('Dafuq. Storing result in global "result".')
            global result
            result = res
            raise e
            
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
            loc_by_country[country] = list(set([location.name for location in self.locations if location.matchedName == country])) 
        return loc_by_country




