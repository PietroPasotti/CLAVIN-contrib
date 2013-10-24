# CLAVIN Python API

## Prerequisites 

pip install -r requirements.txt

clavin-server 


## Development 

Install virtualenv and required packages

    sudo pip install virtualenv 
    virtualenv ~/venvs/clavin 
    source ~/venvs/clavin/bin/activate 
    cd <clavin-python> 
    pip install -r requirements.txt 

## Usage

    from clavin import Clavin
    
    # connect to CLAVIN REST service  
    clv = Clavin("http://localhost:9000")

    # resolve locations in document and output results to stdout
    doc = open("document.txt","r").read()    
    res = clv.resolve(doc)
    print res 








