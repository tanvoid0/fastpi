# Self
`pip freeze > requirements.txt`

# Installation
`pip install -r requirements.txt`

# Run

`docker build -t fastpi .`

`docker run --rm -it  -p 80:80/tcp tanvoid0/fastpi:latest`
`docker push fastpi:latest`


`docker tag fastpi tanvoid0/fastpi:latest`
`docker push tanvoid0/fastpi:latest`