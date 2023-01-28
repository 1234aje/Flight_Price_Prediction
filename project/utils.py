import json
import pickle
import numpy as np
import config

class FlightPrice():

    def __init__(self,dep_time, time_taken, stop, arr_time,class1,days_left,from1,to,airline):
        self.dep_time   = dep_time
        self.time_taken = time_taken
        self.stop       = stop
        self.arr_time   = arr_time
        self.class1     = class1
        self.days_left  = days_left
        self.from1      = from1
        self.to         = to
        self.airline    = airline

    def models(self):
        with open(config.model_path,"rb") as f:
            self.model = pickle.load(f)
        
        with open(config.scal_path,"rb") as f:
            self.scal = pickle.load(f)

        with open(config.json_path,"r") as f:
            self.column = json.load(f)

    def get_prediction(self):
        self.models()
        self.cols = self.column["columns"]
        test_array = np.zeros(len(self.cols))
        test_array[0] = self.column["dep_time"][self.dep_time]
        test_array[1] = self.time_taken
        test_array[2] = self.stop
        test_array[3] = self.column["arr_time"][self.arr_time]
        test_array[4] = self.column["class"][self.class1]
        test_array[5] = self.days_left
        
        a_index = np.where(self.cols == self.airline )[0]
        test_array[a_index] = 1

        f_index = np.where(self.cols == self.from1 )[0]
        test_array[f_index] = 1

        
        t_index = np.where(self.cols == self.to )[0]
        test_array[t_index] = 1

        scal_data = self.scal.transform([test_array])
        price = self.model.predict(scal_data)

        return price
    

        

        



        

        


            

        
        
        

