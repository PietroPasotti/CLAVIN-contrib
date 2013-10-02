import sys 
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','gdelt.settings')
from django.core.management import setup_environ
from gdelt import settings
setup_environ(settings)

from gdelt.models import GDELT

def fn(a):
    if a == '':
        return None 
    else:
        return float(a)

def intn(a):
    if a == '':
        return None 
    else:  
        return int(a)
def un(a):
    return a.decode('utf-8')


f = [ ('GLOBALEVENTID', long), 
 ('SQLDATE', intn),
 ('MonthYear', un),
 ('Year', un),
 ('FractionDate', fn),
 ('Actor1Code', un),
 ('Actor1Name', un),
 ('Actor1CountryCode', un), 
 ('Actor1KnownGroupCode', un),
 ('Actor1EthnicCode', un),
 ('Actor1Religion1Code', un),
 ('Actor1Religion2Code', un),
 ('Actor1Type1Code', un),
 ('Actor1Type2Code', un),
 ('Actor1Type3Code', un),
 ('Actor2Code', un),
 ('Actor2Name', un),
 ('Actor2CountryCode', un),
 ('Actor2KnownGroupCode', un),
 ('Actor2EthnicCode', un),
 ('Actor2Religion1Code', un),
 ('Actor2Religion2Code', un),
 ('Actor2Type1Code', un),
 ('Actor2Type2Code', un),
 ('Actor2Type3Code', un),
 ('IsRootEvent', intn),
 ('EventCode', un),
 ('EventBaseCode', un),
 ('EventRootCode', un),
 ('QuadClass', intn),
 ('GoldsteinScale', fn), 
 ('NumMentions', intn),
 ('NumSources', intn),
 ('NumArticles', intn),
 ('AvgTone', fn),
 ('Actor1Geo_Type', intn), 
 ('Actor1Geo_FullName', un), 
 ('Actor1Geo_CountryCode', un),
 ('Actor1Geo_ADM1Code', un),
 ('Actor1Geo_Lat', fn),
 ('Actor1Geo_Long', fn),
 ('Actor1Geo_FeatureID', un),
 ('Actor2Geo_Type', intn),
 ('Actor2Geo_FullName', un), 
 ('Actor2Geo_CountryCode', un),
 ('Actor2Geo_ADM1Code', un),
 ('Actor2Geo_Lat', fn),
 ('Actor2Geo_Long', fn),
 ('Actor2Geo_FeatureID', un),
 ('ActionGeo_Type', intn),
 ('ActionGeo_FullName', un), 
 ('ActionGeo_CountryCode', un),
 ('ActionGeo_ADM1Code', un),
 ('ActionGeo_Lat', fn),
 ('ActionGeo_Long', fn),
 ('ActionGeo_FeatureID', un),
 ('DATEADDED', intn),
 ('SOURCEURL', un)
]

for line in open("20130401.export.CSV","r"):
    line = line[:-1]
    line = line.split("\t")
    #for f in line:
    #    print repr(f)
    #sys.exit()
    g = GDELT()
  
 
     
    try:
        for i in range(57):
            setattr(g, f[i][0], f[i][1](line[i]))
            print f[i], line[i]

    except:
        print f[i]
        print line[i]
        for f in line:
            print repr(f)
        sys.exit()
        
    g.save()


