from flask import Flask,render_template,jsonify,request
import numpy as np
import config
from project.utils import FlightPrice

app = Flask(__name__)

@app.route("/test")
def test1():
    return "successful"

@app.route("/predict",methods = ["GET"])
def flight_p():
    data = request.form

    dep_time   = data["dep_time"]
    time_taken = eval(data["time_taken"])
    stop       = int(data["stop"])
    arr_time   = data["arr_time"]
    class1     = data["class"]
    days_left  = eval(data["days_left"])
    from1      = data["from"]
    to         = "to_" + data["to"]
    airline   = data["airline"]

    obj =  FlightPrice(dep_time,time_taken,stop,arr_time,class1,days_left,from1,to,airline)
    price = obj.get_prediction()

    return jsonify({"result":f"The prdicted flight price is {np.around(price[0],2)}"})


if __name__ == "__main__":
    app.run(port = config.port_number)



