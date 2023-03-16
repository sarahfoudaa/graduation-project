from turtle import done
from flask import Flask , request ,jsonify
import werkzeug

import json
from tensorflow.keras.models import load_model
import numpy as np
import cv2 
#model = load_model("D:/semester_7/project1/results/VGG_FCN.h5")
model = load_model("D:/semester_7/project1/flask/cityscapessss.h5")

app = Flask(__name__)

@app.route('/upload' , methods=["GET"])
@app.route('/upload' , methods=["POST"])
def upload():
    if(request.method == "POST"):
        imagefile = request.files['image']
        filename=werkzeug.utils.secure_filename(imagefile.filename)
        image_path = "./uploadfolder/" + imagefile.filename
        imagefile.save("./uploadfolder/" + filename)
        
        img = cv2.imread(image_path)
       # img = np.array(img)
        #img = load_img(image_path, target_size=(224,224))
       # img = imagefile
        #img = cv2.resize(img, (128,128))
       # img = img_to_array(img)

        lables = {
                0 :'unlabeled'           ,
			    1 :'ego vehicle'         ,
			    2 :'rectification border',
			    3 :'out of roi'          ,
		    	4 :'static'              ,
		    	5 :'dynamic'             ,
		    	6 :'ground'              ,
		    	7 :'road'                ,
		    	8 :'sidewalk'            ,
		    	9 :'parking'             ,
		    	10 :'rail track'         ,
		    	11 :'building'           ,
		    	12 :'wall'               ,
		    	13 :'fence'              ,
			    14 :'guard rail'         ,
		    	15 :'bridge'             ,
		    	16 :'tunnel'             ,
		    	17 :'pole'               ,
		    	18 :'polegroup'          ,
		    	19 :'traffic light'      ,
		    	20 :'traffic sign'       ,
		    	21 :'vegetation'         ,
		    	22 :'terrain'            ,
		    	23 :'sky'                ,
		    	24 :'person'             ,
		    	25 :'rider'              ,
		    	26 :'car'                ,
		    	27 :'truck'              ,
		    	28 :'bus'                ,
		    	29 :'caravan'            ,
		    	30 :'trailer'            ,
		    	31 :'train'              ,
		    	32 :'motorcycle'         ,
		    	33 :'bicycle'            ,
		    	-1 :'license plate'      ,
		    }

        img = cv2.resize(img, (128,128), interpolation = cv2.INTER_AREA)
        imgLables = []
        s=model.predict(np.expand_dims(img, axis = 0))
        check = np.zeros((128, 128), dtype=np.uint8)
        for i in range(0, len(s[0])):
            check[i]= np.argmax(s[0][i], axis = 1)
        uniq = np.unique(check)
        for i in range (len(uniq)):
            imgLables.append(lables[i])
        ss= check
        lablesString=''
        for i in range (len(imgLables)):
            lablesString = lablesString +' .'+ imgLables[i] 
        print(lablesString)
        print("done")
        return jsonify({
            "message": lablesString
            
        })
        print("done")

if __name__ =="__main__":
    app.run(debug=True , port=3000)
