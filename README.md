# Self
`pip freeze > requirements.txt`

# Installation
`pip install -r requirements.txt`

# Run

`docker build -t tanvoid0/fastpi .`

`docker run --rm -it  -p 8080:80/tcp tanvoid0/fastpi:latest`

`docker push tanvoid0/fastpi:latest`


`docker tag fastpi tanvoid0/fastpi:latest`
`docker push tanvoid0/fastpi:latest`

`uvicorn main:app --host 0.0.0.0 --port 80`


# Mongo queries
## Renaming Collection
db.language.renameCollection("linguistic")

## Adding Column with default data
db.your_collection.updateMany(
  {},
  { $set: {"new_field": 1} },
  false,
  true
)

## Renaming Column
db.linguistic.updateMany({}, {$rename: {"icon": "image"}}, false, true)

## Changing column type

