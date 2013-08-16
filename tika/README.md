# CLAVIN Tika Integration

    # run tika-server
    java -jar tika-server-1.5-SNAPSHOT.jar
 
    # run clavin-server, more directions can be found here: https://github.com/Berico-Technologies/CLAVIN-contrib/tree/master/clavin-server
    play run 

    # pipe output from processed pptx file to clavin server and output resolved json 
    curl -T document.pptx http://localhost:9998/tika | curl -H"Content-Type:text/plain" --data @- http://localhost:9000


