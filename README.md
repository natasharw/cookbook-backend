# Cookbook Backend

A backend API for a cookbook built with Django REST Framework, Postgres and Docker.

## Overview

This application creates an online catalog for a personal cookbook for users to create, edit and view recipes filtered by their cooking time.

Currently the features are:
* Models for recipe timings and recipes
* Users can create timing categories
* Users can add individual recipes
* Users can view recipes as a list, with an optional filtering on timing, or in detail
* Users can edit and delete individual recipes
* Built in Docker containers

## Prerequisites
* Install [Docker](https://docs.docker.com/get-docker/)

## Install
#### Clone repository
```
git clone git@github.com:natasharw/cookbook-backend.git
```

#### Switch to repository folder
```
cd cookbook-backend
```

## Run
#### Build the services
```
docker-compose build
```

#### Run services in a detached Docker session
```
docker-compose up -d
```

## Test
#### Run tests in Docker container
```
docker-compose exec web python manage.py test -v 2
```

## Use

#### Create timings and test recipes using admin site
* ```docker-compose exec web python manage.py createsuperuser```
* Follow on-screen instructions
* Open browser to `http://127.0.0.1:8000/admin/`
* Log in with superuser credentials
* Create timings and recipes

#### Get all recipes
<i>Request:</i>

`GET /api/recipes`
```
curl -i -H 'Accept: application/json' http://localhost:8000/api/recipes/
```

<i>Response:</i>

```
HTTP/1.1 200 OK
Date: Sun, 12 Apr 2020 13:09:07 GMT
Server: WSGIServer/0.2 CPython/3.8.0
Content-Type: application/json
Vary: Accept, Cookie
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: SAMEORIGIN
Content-Length: 2

[]
```

#### Get all recipes in one time category
<i>Request:</i>  

`GET /api/recipes/?timing=id`
```
curl -i -H 'Accept: application/json' http://localhost:8000/api/recipes/?timing=id
```

<i>Response</i>

```
HTTP/1.1 200 OK
Date: Sun, 12 Apr 2020 16:25:42 GMT
Server: WSGIServer/0.2 CPython/3.8.0
Content-Type: application/json
Vary: Accept, Cookie
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: SAMEORIGIN
Content-Length: 64

[{"pk":5,"name":"testing","owner":null,"timing":2,"detail":"2"}]
```
#### Create a new recipe
<i>Request:</i>  

`POST /api/recipes/`  
```
curl -i -H 'Accept: application/json' -d 'name=Bar&timing=1' http://localhost:8000/api/recipes/
```

<i>Response:</i>

```
HTTP/1.1 201 Created
Date: Sun, 12 Apr 2020 13:43:53 GMT
Server: WSGIServer/0.2 CPython/3.8.0
Content-Type: application/json
Vary: Accept, Cookie
Allow: GET, POST, HEAD, OPTIONS
X-Frame-Options: SAMEORIGIN
Content-Length: 59

{"pk":3,"name":"Bar","owner":null,"timing":1,"detail":null}
```

#### Get a recipe by ID
<i>Request:</i>  

`GET /api/recipes/id`
```
curl -i -H 'Accept: application/json' http://localhost:8000/api/recipes/1
```
<i>Response:</i>

```
HTTP/1.1 200 OK
Date: Sun, 12 Apr 2020 13:17:17 GMT
Server: WSGIServer/0.2 CPython/3.8.0
Content-Type: application/json
Vary: Accept, Cookie
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: SAMEORIGIN
Content-Length: 83

{"pk":1,"name":"Foo","owner":1,"timing":1,"detail":"bar"}
```

#### Change a recipe
<i>Request:</i>  

`PUT /api/recipes/id`
```
curl -i -H 'Accept: application/json' -X PUT -d 'name=Foo&timing=1&status=changed' http://localhost:8000/api/recipes/1
```

<i>Response:</i>

```
HTTP/1.1 200 OKapi/recipes/1
Date: Sun, 12 Apr 2020 13:21:29 GMT
Server: WSGIServer/0.2 CPython/3.8.0
Content-Type: application/json
Vary: Accept, Cookie
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: SAMEORIGIN
Content-Length: 61

{"pk":1,"name":"Foo","owner":1,"timing":1,"detail":"changed"}
```

#### Delete a recipe
<i>Request:</i>

`DELETE /api/recipes/id` 

```
curl -i -H 'Accept: application/json' -X DELETE http://localhost:8000/api/recipes/2
```

<i>Response:</i>

```
HTTP/1.1 204 No Content
Date: Sun, 12 Apr 2020 13:25:20 GMT
Server: WSGIServer/0.2 CPython/3.8.0
Vary: Accept, Cookie
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
X-Frame-Options: SAMEORIGIN
Content-Length: 0
```

## Finish
#### Bring down docker containers
```
docker-compose down
```
