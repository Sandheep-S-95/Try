from flask import *
import sqlite3

import requests

headers = {
	"x-rapidapi-key": "60d952eb8amsh3fb0c42a1c985d1p1fbce5jsn67be98652c4c",
	"x-rapidapi-host": "open-weather13.p.rapidapi.com"
}


app=Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/citypage",methods=["GET"])
def city_page():
    return render_template("city.html")

@app.route("/city",methods=["POST"])
def city():
    city=request.form["city"]
    try:
        conn=sqlite3.connect("./Database/weather")
        cur=conn.cursor()
        city.lower()###
        url = "https://open-weather13.p.rapidapi.com/city/"+city+"/EN"
        response = requests.get(url, headers=headers)
        print(response.json())
        response=response.json()####
        res={
             "city":response['name'],
             "latitude":float(response["coord"]["lat"]),
             "longitude":float(response["coord"]["lon"]),
             "temp":float(response["main"]["temp"]),
             "max_temp":float(response["main"]["temp_max"]),
             "min_temp":float(response["main"]["temp_min"])
        }####
        print(res)

        cur.execute("INSERT INTO userCities(city,latitude,longitude,temp,max_temp,min_temp) VALUES(?,?,?,?,?,?)",
                    (res["city"],res["latitude"],res["longitude"],res["temp"],res["max_temp"],res["min_temp"]))
        conn.commit()
        conn.close()
        return render_template("result.html",msg="SUCCESSFULLY INSERTED : "+str(response))
    except Exception as e:
        return render_template("result.html",msg=" e  "+str(e))


@app.route("/view",methods=["GET"])
def view():
    try:
        conn=sqlite3.connect("./Database/weather")
        conn.row_factory=sqlite3.Row
        cur=conn.cursor()
        cur.execute("SELECT * FROM userCities")
        rows=cur.fetchall()
        return render_template("view.html",rows=rows)
    except Exception as e:
        return render_template("result.html",msg=" e "+str(e))


def main():
    app.run(host="0.0.0.0", port=10000, debug=False)
main()
