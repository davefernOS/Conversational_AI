# Conversational_AI - Dialogflow
Starter Code for University of Michigan Conversational AI Major Design Experience using Google Dialogflow 

## How to Use

- Backend: https://79889e96.ngrok.io/ Already connected with dialog flow
- Front End should be run on local host `python front_end.py` and then acessed at 0.0.0.0:5000

## How To Run

*Currently only one ngrok session can run so you must tunnel the front end once to extract your coordinates and then tunnel the back end and have the front end just through local host*

1. `./ngrok http 5000` and in another terminal `python front_end.py`
2. Go to 0.0.0.0:5000 and get your coordinates 
3. Close ngrok session and run `./ngrok http 5001`and `python back_end.py`
4. Update the redirected https tunnel in dialog flow 
5. Query on front end


- Alternatively you can just run demo with no coordinates and it will default to 0,0 



## Dialog Flow - Conversational Agent Framework

1. **Intents**

Dialogflow greatly simplifies the organization of your conversational agent into intents. Each intent contains:
- Contexts - Remembered values that can persist between intents
- Events - Non verbal triggers dependent on your integration platform ex) preset wake up time on Google Assistant or Amazon Alexa
- Training Phrases - Used for the ML algorithm determine de appropriate intent given a query
- Actions and Parameters - Allows you to extract specific parts of a query as parameters used in constructing the appropriate response
- Responses - A set of responses to a specific intent query (able to use parameters), including default responses
- Fulfillment - Options to connects back-end POST calls to resolve query. The URL for your back end is specified in the Fulfillment tab [Must Be HTTP**S**]

---

2. **Fulfillment**

In setting up your back end server, you will provide a **https** URL as a web-hook (ngrok can facilitate this immensely), which will then receive a POST request, and you then return the appropriate information such as a full response or simply slot values to be matched with the pre-written responses in the console
```
@app.route('/', methods=['POST'])
def receive_requests():
```

We then use ngrok to redirect a URL to the local-host port on our machine so that Dialogflow can call our back end without a hosting service. Reference the Ngrok section for details.

In between receiving a request and returning a response we must implement our internal logic to find the desired response and if applicable, a follow up intent to be called.
- API Calls: Using the requests library we may attain information based on the query parameters and construct a response 
```
URL = 'https://api.sunrise-sunset.org/json?lat={}&lng={}&date={}'.format(lat, lng, date)
req = requests.get(url = URL).json()
```
- Database Queries: Using SQL calls we can retrive information from our database to fufill the query and construct a response
```
db_cursor.execute('SELECT * FROM posts WHERE date=04202020')
results = db_cursor.fetchall()
```

*And in the end we return a json object such as a response a.k.a. fulfillmentText:* 
`return {'fulfillmentText': 'The Sunset will be at {}.'.format(results['sunset'])}`

---

3. **Integrations**
- Dialogflow Console: You can input the script provided by Dialogflow to interact with the Conversational Agent in testing without needing to develop your front end. Look at DEMO page on the example website

- Front End Implementation 
	TODO
	TODO
	TODO


## ngrok - Url tunnel to local host
*[Ngrok Docs](https://ngrok.com/docs)*

Download the executable. Then unzip and connect to your account './ngrok authtoken [Your Token On Account Page]' and then you can redirect to the desired port './ngrok http [PORT NUMBER]'

```
# Example of Steps to redirect to port 5000 -> 0.0.0.0:5000
unzip ngrok.zip
./ngrok authtoken 1aXwBEJvJ0HWDnh1OHfgoaIUNR1_642e2KjjXCpkDq1VgB98z
./ngrok http 5000
```

you should then see a terminal window as such, and there is a http and a https link which will redirect to your desired port - in this case 5000. As you make requests to the forwarding URL you will see the traffic under the *Connections* section

```
ngrok by @inconshreveable

Tunnel Status                 online
Version                       2.0/2.0
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://92832de0.ngrok.io -&gt; localhost:5000
Forwarding                    https://92832de0.ngrok.io -&gt; localhost:5000

Connnections                  ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.00
```


## Requests - API calls for Fulfillment 

Allows user to make GET/POST and other types of requests easily in back end, whcih is especially useful for your back end fulfillment.

[Documentation](https://requests.readthedocs.io/en/master/)

**Example Usage:**
```
URL = 'https://api.sunrise-sunset.org/json?lat={}&lng={}&date={}'.format(lat, lng, date)
response = requests.get(url = URL).json()

# Which returns the following object
	{
      "results":
      {
        "sunrise":"7:27:02 AM",
        "sunset":"5:05:55 PM",
        "solar_noon":"12:16:28 PM",
        "day_length":"9:38:53",
        "civil_twilight_begin":"6:58:14 AM",
        "civil_twilight_end":"5:34:43 PM",
        "nautical_twilight_begin":"6:25:47 AM",
        "nautical_twilight_end":"6:07:10 PM",
        "astronomical_twilight_begin":"5:54:14 AM",
        "astronomical_twilight_end":"6:38:43 PM"
      },
       "status":"OK"
	}
  
```

## Database - SQL Lite
A SQL Database Engine to store data. 

Command Line Installation
```
#Mac 
brew install sqlite3

#Linux/WSL 
sudo apt-get install sqlite3
```

Starts database engine, which then can be easily written to with SQL commands
```sqlite3 database.sqlite3```

A better method is to declare a database schema and a data file

```
touch database/schema.sql
touch database/data.sql
```

In schema:
```
CREATE TABLE tides(
  the_date integer,
  high_1 VARCHAR(40),
  high_2 VARCHAR(40),
  low_1 VARCHAR(40),
  low_2 VARCHAR(40)
);
```

In Data:
```
INSERT INTO tides(the_date, high_1, high_2, low_1, low_2)
VALUES (20200420, '2:04, 2.00 M', '14:19, 2.16 M', '8:03, 0.36 M', '20:27, 0.30 M');
```

And then to manage:
```
#Create
sqlite3 database.sqlite3 < database/schema.sql
sqlite3 database.sqlite3 < database/data.sql

#Destroy
rm -rf database.sqlite3
```

The database can now be accessed using the get_db function in settings.py 
```
database = settings.get_db()

db_cursor = database.cursor()

# And with a cursor with which we can make queries
db_cursor.execute('SELECT * FROM posts WHERE date=04202020')
```















