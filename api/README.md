# Proof Of Existence REST API

## Quick Start

- Install dependencies

   `pip install -r requirements.txt`

- Start python webserver

   `python poe_server.py`
   

### HTTP API
##### Publish document
```
curl -H "Content-type:application/json" --data '{"name": "name",
                                                "email": "email@test.com",
                                                "message": "test message",
                                                "signature": "SHA256signature"}' http://localhost:8000/publish
```

##### Verify document
```
curl http://localhost:8000/verify?signature=SHA256signature
``` 

##### Fetch latest document info
```
curl http://localhost:8000/details?count=3
```