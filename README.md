# Weather REST-API

I used Fast API, MongoDB, Docker and [Openweathermap](https://openweathermap.org/api) API to create it. <br>
There's a simple template using HTML and CSS too. <br>
I used a simple cashing simple in this project but in real projects it should be replaced with Redis database.

## How to run?
I used [Darkube](https://hamravesh.com/darkube) to run this project so I didn't make docker compose file for MongoDB, if you want to use similar services you can follow steps but if you don't you should make a docker compse file.

### Using Docker
if you want to use Docker there are two simple steps
- `docker build . -t weather_api`
- `docker run -p 80:80 weather_api`nknjkn

### Without Docker
- `pip install -r requirements.txt`
- `uvicorn main:app --host 0.0.0.0 --port 80`

After running project you can check documentation on 0.0.0.0/docs .

sfsf
