Experimental CLAVIN Scala web server
=====================================


## Prerequisites 

Play framework 

http://www.playframework.com/



## Point to the correct index directory

Edit conf/application.conf and put in the correct index path 

    clavin.index = "/Users/tpinney/project/CLAVIN/IndexDirectory"

## Start the server 

    play run 


## Send a document to the REST service

Sample document of the wikipedia Yak article 

    curl -H"Content-Type:text/plain" -d@document.txt http://localhost:9000

This will return JSON of the resolved locations 



