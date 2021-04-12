## Description
* I have created REST APIs using Flask as it is a microframework and it has a lightweight and modular design and given the problem statement scenario I thought Flask will be a good choice.   
* MySQL is used as a database. It contains 3 tables for audio files Song, Podcast and Audiobook.   
* I have used Singleton classes in the scenarios where only one-time object needs to be created and used many times in the application.   
* Marshmallow is used as a serializer as well as for validation of the data. 
* There are 4 endpoints for POST, PUT, DELETE and GET API. According to the file type given in the path, dynamically operations are executed.
## How to run the application
### Installing dependencies
#### Docker
```
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
#### docker-compose
```
sudo curl -L "https://github.com/docker/compose/releases/download/1.28.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
### Building the application
```
sudo docker-compose build
```
### Starting the services
```
sudo docker-compose up -d
```

After this following services will be in running state:

``backend`` -> Flask WSGI server running via gunicorn which is exposing APIs 

``db`` -> mysql db container

``nginx`` -> Reverse proxy services which will forward the incoming requests to the backend service

**Note**: ``backend`` service will wait till mysql container server is ready for listening requests. Once mysql is started, gunicorn server will be started. 
You can check the logs of ``backend`` service using ``docker logs backend``.

### Migrating the database:
Once all the services are up use the following command for the initial migration of the database
```
sudo docker exec backend python3 manage.py db upgrade
```

## Calling APIs:
### POST API:
**Endpoint**: ``http://localhost/api/v1/audioFile/<file_type>``

**Body**:
audio file id is automatically created so you only have to pass the fields according to file type.

**Response**:
```
200 -> Resouce added and response will contain JSON data of added resource.
400 -> In case of invalid data
500 -> Server Error
```

**Example**:

Sample Request:
```
curl --location --request POST 'http://localhost/api/v1/audioFile/song' \
--data-raw '{"name": "sample_song","duration": 300}'
```
Sample Response:
```
Status code: 200
Response body:
{
	"uploaded_time": "2021-04-12T09:54:26",
	"id": 3,
	"duration": 300,
	"name": "sample_song"
}
```

### PUT API:
**Endpoint**: ``http://localhost/api/v1/audioFile/<file_type>/<file_id>``

**Body**:
JSON data containg fields for update

**Response**:
```
200 -> Resouce updated successfully.
400 -> In case of invalid data
404 -> Resource not found
500 -> Server Error
```

**Example**:

Sample Request:
```
curl --location --request PUT 'http://localhost/api/v1/audioFile/song/3' \
--data-raw '{"duration": 500}'
```
Sample Response:
```
Status code: 200
```

### GET API:

**Endpoint**: 

``http://localhost/api/v1/audioFile/<file_type>``


``http://localhost/api/v1/audioFile/<file_type>/<file_id>``

**Response**:
```
200 -> Resouces fethed successfully and response body will contain list of resources
404 -> Resource not found
500 -> Server Error
```

**Example**:

Sample Request:
```
curl --location --request GET 'http://localhost/api/v1/audioFile/song/3'
```

Sample Response:
```
Status code: 200
Response body:
[
	{
		"uploaded_time": "2021-04-12T09:58:29",
		"id": 3,
		"duration": 500,
		"name": "sample_song"
	}
]
```

Sample Request:
```
curl --location --request GET 'http://localhost/api/v1/audioFile/song'
```
Sample Response:
```
Status code: 200
Response body:
[
  {
    "uploaded_time": "2021-04-12T09:46:19",
    "id": 1,
    "duration": 100,
    "name": "song1"
  },
  {
    "uploaded_time": "2021-04-12T09:46:26",
    "id": 2,
    "duration": 200,
    "name": "song2"
  },
  {
    "uploaded_time": "2021-04-12T09:58:29",
    "id": 3,
    "duration": 500,
    "name": "sample_song"
  }
]
```


### DELETE API:
**Endpoint**: ``http://localhost/api/v1/audioFile/<file_type>/<file_id>``

**Response**:
```
200 -> Resouces deleted successfully.
404 -> Resource not found
500 -> Server Error
```

**Example**:

Sample Request:
```
curl --location --request DELETE 'http://localhost/api/v1/audioFile/song/3
Sample Response:
```

Sample Response:
```
Status code: 200
```

## Running Tests:
Change ``APP_ENV=test`` in the ``backend/conf.env`` file.

After changing up the service using following command:
``sudo docker-compose up -d``

Use the following command for the initial migration of the test database
```
sudo docker exec backend python3 manage.py db upgrade
```

For running tests:
``sudo docker exec backend python3 tests/test_audio.py``
