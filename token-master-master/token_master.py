#  TODO
from datetime import datetime
import json
"""
when 

"""
start_total=10

def parse_dict(path):
    try:
        with open(path, "r") as read_file: 
            data = json.load(read_file) 
            print(data)
    except:
        print("Program Initialised")
        data={}
        t_data['sold_token'] = 0
        t_data['total_token'] = start_total 
        with open("token_data.json", "w") as outfile: 
           json.dump(t_data, outfile, indent=4) 

def sell_token(name,token):
    try:
        with open("person_data.json", "r") as read_file: 
            data = json.load(read_file) 
            # print(data)
    except:
        print("Program Initialised")
        data={}
        
    token=token

    if token is None:
        print(f"Token Ended Not alloted to {name}\n Try Again Later")
        key=str(datetime.now())
        data[key]={}
        data[key]['name']=name
        data[key]['token#']=None
    else:
        key=str(datetime.now())
        data[key]={}
        data[key]['name']=name
        data[key]['token#']=token

        print(f"{name} is given token number {token}")


    with open("person_data.json", "w") as outfile: 
        json.dump(data, outfile, indent=4) 


def get_token():
    global start_total
    try:
        with open("token_data.json", "r") as read_file: 
            t_data = json.load(read_file) 
            print(t_data)
    except:
        print("Program Initialised")
        t_data={}
        t_data['sold_token'] = 0
        t_data['total_token'] = start_total 
        with open("token_data.json", "w") as outfile: 
           json.dump(t_data, outfile, indent=4) 

    sold_token=t_data['sold_token']
    total_token=t_data['total_token']
    if int(sold_token)>=int(total_token):
        print("Token Ended")
    else:
        t_data={}
        sold_token+=1
        print("Token Sold")
        t_data['sold_token'] = sold_token
        t_data['total_token'] = total_token     
        with open("token_data.json", "w") as outfile: 
           json.dump(t_data, outfile, indent=4) 
        return sold_token

if __name__=='__main__':
    name = input("Enter your name: ")
    sell_token(name)
