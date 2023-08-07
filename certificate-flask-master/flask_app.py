from flask import Flask, render_template, redirect, request
import cv2
from time import time
from PIL import Image,ImageDraw,ImageFont

# import imutils

str(time()).replace('.','')

app = Flask(__name__)
# 'static/img1.png'
# im_name="img.png"

def saveframe(text):
    # try:
    img=cv2.imread(r'/home/vermavinay982/certificate-flask/static/simple2.jpg')
        # img=imutils.resize(img,width=1000)
    # name = 'static/'+text+'.jpg'
    url='/home/vermavinay982/certificate-flask/'
    name = 'static/'+str(time()).replace('.','')+'img.png'

    # except:
    #     exit()
    #     name='static/img.png'
    #     name='static/simple2.jpg'

        # return name
    if img is None:
        name='CANT FIND IMAGE'
        return 'static/img.png'

    fontScale = 0.4
    color = (0, 0, 0)
    thickness = 1
    font = cv2.FONT_HERSHEY_SIMPLEX
    watermark=True


    # text='Vinay Verma'
    text=text
    if watermark:
        for x in range(1,len(img),200):
            for y in range(1,len(img[0]),70):
                cv2.putText(img, "Copyright@ Vinay", (x,y), font, fontScale, color, thickness, cv2.LINE_AA)

    # has successfully completed the Basic Interior Design Level 1 Course and is entitled to pursue Level 2 Course.

    data={
    1:{'text':text,'pos':(300,350),'color':(10,10,10),'size':1.5,'thick':3},
    2:{'text':'has participated in the webinar series on ML and AI','pos':(300,400),'color':(10,10,10),'size':0.7,'thick':1},
    3:{'text':'conducted by IEEE CS ADGITM','pos':(300,430),'color':(10,10,10),'size':0.7,'thick':1},
    4:{'text':'IEEE ADGITM ','pos':(300,650),'color':(10,10,10),'size':0.7,'thick':1}

    }

    #cv2.putText(img, "face", (x,y), font, fontScale, color, thickness, cv2.LINE_AA)

    for key in data.keys():
        d=data[key]
        print(d)
        cv2.putText(img,d['text'], d['pos'], font, d['size'], d['color'], d['thick'], cv2.LINE_AA)


    # cv2.imshow("asdfasdf",img)
    cv2.imwrite(url+name,img)
    print("image written")
    # cv2.waitKey(0)
    return name


@app.route('/', methods=['POST','GET'])
def index():
    # text=request.form['']
    # return render_template('old.html')
    # return render_template('form_send.html')
    # return "asdf"
    return redirect('/start')

@app.route('/start', methods=['POST','GET'])
def rtsp():

    print(request.method)
    # try:
    #   print(request.form['rtsp'])
    # except:
    #   print("taal diaa")
    name='static/img.png'
    # im=Image.open(name)
    # im=cv2.imread(name)
    # if im is None:
    #     return f"write hi khrab hai{name}"
    # cv2.imwrite('/home/vermavinay982/certificate-flask/static/new1.png',im)

    if 'name' in request.args:
        name = request.args['name']
        name=saveframe(name)
        # return name
        # return render_template('label_faces.html', title="Label", table_contents=content)

    return render_template('old.html',image=name)



if __name__=="__main__":


    app.run(debug=True,host='0.0.0.0')