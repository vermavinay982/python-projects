from flask import Flask, redirect, jsonify, request
from datetime import datetime
import json

# Flask Config
app = Flask(__name__)
app.config['DEBUG'] = False
# Endpoints


start_total=30

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/book_token', methods=['GET'])
def sell_token():
    # name=request.data
    if 'name' in request.args:
        name = request.args['name']
    else:
        return "Name not returned"
    if name=='reset':
        reset_token()
        return "Reseted All Records"
        
    try:
        with open("person_data.json", "r") as read_file: 
            data = json.load(read_file) 
            # print(data)
    except:
        print("Program Initialised")
        data={}
        
    if name=='show':
        return jsonify(data)

    token=get_token()

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
    print("done")

    return jsonify({"name":name, "token":token})
    # return f"{name} is given token number {token}"

def reset_token():
    print("Program Initialised")
    t_data={}
    t_data['sold_token'] = 0
    t_data['total_token'] = start_total 
    with open("token_data.json", "w") as outfile: 
        json.dump(t_data, outfile, indent=4) 

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

    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', threaded=False, use_reloader=False)
