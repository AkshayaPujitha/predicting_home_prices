import json
import pickle
import numpy as np
locations=None
model=None
data_columns=None
location=None



def get_home_price(location1,sqft,bhk,bath):
    location1.lower()
    #loc_index=
    try:
        if location1 in locations:
            loc_index=locations.index(location1)
        else:
            return -1
    except:
        return -1

    x = np.zeros(len(data_columns)-1)
    #print(len(x))
    x[3] = sqft
    x[1] = bath
    x[2] = bhk
    x[0]=location[loc_index]
    #print(x)
    

    return model.predict([x])[0]
    #return locations

def load_saved_artifacts():
    global locations
    global data_columns
    global model
    global location
    with open('server/artifacts/columns.json','r') as f:
        locations=json.load(f)['locations']
    
    with open('server/artifacts/columns.json','r') as f:
        data_columns=json.load(f)['data_columns']
    
    with open('server/artifacts/columns.json','r') as f:
        location=json.load(f)['location']
    
    with open("server/artifacts/banglore_home_prices_model.pickle",'rb') as f:
        model=pickle.load(f)

def get_location_names():
    #print(locations)
    load_saved_artifacts()
    return locations



if __name__=="__main__":
    load_saved_artifacts()
    print(get_home_price("1st Phase JP Nagar",1000,2,2))
    #print(data_columns)
    #print(get_locations_names())