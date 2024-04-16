
    
    
# from googleapiclient.discovery import build

# # Replace 'YOUR_API_KEY' with your actual YouTube API key
# API_KEY = 'AIzaSyDDsgxGtOTIjYq16EsiXhDP9coPLtwC1tI'

# def fetch_video_links(search_query, max_results=10):
#     youtube = build('youtube', 'v3', developerKey=API_KEY)

#     search_response = youtube.search().list(
#         q=search_query,
#         part='id,snippet',
#         maxResults=max_results,
#         type='video'
#     ).execute()

#     videos = []
#     for search_result in search_response.get('items', []):
#         video_id = search_result['id']['videoId']
#         video_url = f"https://www.youtube.com/watch?v={video_id}"
#         video = {
#             'title': search_result['snippet']['title'],
#             'video_id': video_id,
#             'video_url': video_url
#         }
#         videos.append(video)

#     return videos

# # Example usage
# search_query = 'bedardiya song with layrix'
# videos = fetch_video_links(search_query)

# for video in videos:
#     print(f"Title: {video['title']}")
#     print(f"Video ID: {video['video_id']}")
#     print(f"Video URL: {video['video_url']}")
#     print("-" * 30)
    
from flask import Flask, render_template, request, session, url_for, redirect, jsonify
import pymysql
from werkzeug.utils import secure_filename
import pathlib
import pandas as pd
import cv2
import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import json





app = Flask(__name__)
app.secret_key = 'any random string'
app.config['UPLOADED_PHOTOS_DEST'] = 'static/profile/'
app.config['UPLOADED_PHOTOS_DEST1'] = 'static/product/'
app.config['UPLOADED_PHOTOS_DEST2'] = 'static/skindetecttype'

app.secret_key = 'any random string'
model = load_model('VGGSKin.hp5')

def dbConnection():
    connection = pymysql.connect(host="localhost", user="root", password="root", database="032-Cosmetics")
    return connection

def dbClose():
    try:
        dbConnection().close()
    except:
        print("Something went wrong in Close DB Connection")
        
        
                
con = dbConnection()
cursor = con.cursor()


@app.route('/', methods=["GET","POST"])
def main():
    
    return render_template('main.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        Email = request.form.get("Email")
        Password = request.form.get("password")
        print(Password)
        con = dbConnection()
        cursor = con.cursor()
        result_count = cursor.execute('SELECT * FROM userregisters WHERE Email = %s AND Password = %s', (Email, Password))
        print(result_count)
        
        if result_count == 1:
            res = cursor.fetchone()
            print(res)
            session['user'] = res[1]
            session['uid'] = res[0]
            session['image'] = res[5]
            # Successful login logic
            # return jsonify({'message': 'Login successful', 'user_id': res[0]})
            return "success"
        else:
            # Failed login logic
            # return jsonify({'message': 'Login failed'})
            return "fail"

        con.close()
    

@app.route('/register',methods=['POST','GET'])
def register():
    
    return render_template('register.html')

@app.route('/register1',methods=['POST'])
def register1():
    
    print("ouy")
    if request.method =='POST':
        print("in record")
        details = request.form
      
        Username = details['Username']
        email = details['email']
        Mobile = details['Mobile'] 
        Password = details['Password']
        Address = details['Address'] 
        Pancard = details['Pancard']
        uploadimg = request.files['file']
        
        
        con = dbConnection()
        cursor = con.cursor()
        cursor.execute('SELECT * FROM userregisters WHERE Email = %s', (email))
        res = cursor.fetchone()
      
        
        filename_secure = secure_filename(uploadimg.filename)
        uploadimg.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename_secure))
        filenamepath = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename_secure)
        
        if not res:
            sql = "INSERT INTO userregisters(Username, Email, Mobile, Password, Profile_Img, Address, Pancard) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            val = (Username, email, Mobile, Password, filenamepath,Address,Pancard)
            cursor.execute(sql, val)
            con.commit()
          
    
            message = "Registration USER successfully added by USER side. Username: " + Username
            # return redirect(url_for('index'))
            return jsonify({'message': message})
            message = "Already available"
            
        else:
            message = "Registration USER not  added by USER side. Username: " + Username
            dbClose()
            # return redirect(url_for('index'))
            return jsonify({'message': message})
              
@app.route('/SessionHandle1',methods=['POST','GET'])
def SessionHandle1():
    if request.method == "POST":
        details = request.form
        name = details['name']
        session['name'] = name
        strofuser = name
        print (strofuser.encode('utf8', 'ignore'))
        return strofuser      

@app.route('/adminlogin')
def adminlogin():
    return render_template('adminlogin.html')


@app.route('/index')
def index():
    username=session['user']
    img=session['image']
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM products')
    data = cursor.fetchall()
    
    return render_template('index.html',username=username,img=img,data=data)

@app.route('/adminhome')
def adminhome():
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM products')
    data = cursor.fetchall()
    
    return render_template('adminhome.html',data=data)


@app.route('/fontawesome')
def fontawesome():
    username=session['user']
    img=session['image']
    return render_template('fontawesome.html',username=username,img=img)


@app.route('/mapgoogle')
def mapgoogle():
    username=session['user']
    img=session['image']
    
    return render_template('mapgoogle.html',username=username,img=img)

@app.route('/mapgoogleadmin',methods=['POST','GET'])
def mapgoogleadmin():
    if request.method == "POST":
        details = request.form
        NAME = details['NAME']
        PRICE = details['PRICE']
        DESCRIPTION = details['DESCRIPTION']
        TYPE= details['Type']
        PCS = details['PCS']
        uploadimg = request.files['file']
        
        con = dbConnection()
        cursor = con.cursor()
        filename_secure = secure_filename(uploadimg.filename)
        uploadimg.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename_secure))
        filenamepath = os.path.join(app.config['UPLOADED_PHOTOS_DEST'], filename_secure)
        
        sql = "INSERT INTO products(NAME, PRICE, DESCRIPTION, TYPE, PCS, filenamepath) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (NAME, PRICE, DESCRIPTION, TYPE, PCS,filenamepath)
        cursor.execute(sql, val)
        con.commit()
        
        message = "Product Added successfully" 
        print(message)
        return render_template('mapgoogleadmin.html',message=message)
        
        
        
    
    
    
    
    return render_template('mapgoogleadmin.html')

@app.route('/pagesblank')
def pagesblank():
    username=session['user']
    img=session['image']
    return render_template('pagesblank.html',username=username,img=img)


@app.route('/pages')
def pages():
    username=session['user']
    img=session['image']
   
    return render_template('pages.html',username=username,img=img)


@app.route('/profile')
def profile():
    username=session['user']
    img=session['image']
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM userregisters WHERE Username = %s and Profile_Img = %s', (username,img))
    data = cursor.fetchone()
    print(data)
 
    
    return render_template('profile.html',username=username,img=img,data=data)


@app.route('/tablebasic')
def tablebasic():
    username=session['user']
    img=session['image']
    
    
    return render_template('tablebasic.html',username=username,img=img)

@app.route('/logout')
def logout():
    session.pop('user')
    return redirect(url_for('main'))

@app.route('/logout1')
def logout1():
   
    return redirect(url_for('main'))

@app.route('/viewpro/<productId>')
def viewpro(productId):
    username=session['user']
    img=session['image']
    print(productId)

    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM products WHERE PRODUCT_ID = %s ', (productId))
    data = cursor.fetchone()
    # print(data)
    row=list(data)
    print(row)
    cursor.execute('SELECT * FROM recomdedpro WHERE productid = %s ', (productId))
    reviews = cursor.fetchall()
    
    return render_template('viewpro.html',username=username,img=img,row=row,reviews=reviews)

####################################################################feedback users############################################################
@app.route('/Review', methods=["POST"])
def Review():
    print("GET")
    USERID=session['uid']
    username=session['user']
    img=session['image']
    
    
    if request.method =='POST':
        print("Post")
        rating = request.form.get('rating')
        comment = request.form.get('comment')
        productname = request.form.get('productname')
        productid = request.form.get('productid')
        producttype = request.form.get('producttype')
       
        con = dbConnection()
        cursor = con.cursor()
        sql = "INSERT INTO Recomdedpro(productname, productid, comment, username, username_img, USERID ,producttype,rating) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (productname, productid, comment, username, img, USERID ,producttype, rating)
        cursor.execute(sql, val)
        print("Query submitted...")
        con.commit()
        
        msg = "Review Submited Successfuly....." 
        return msg
            
      
#################################################recommended business###############################################################################
@app.route('/viewproadmin/<productId>')
def viewproadmin(productId):
   
    con = dbConnection()
    cursor = con.cursor()
    cursor.execute('SELECT * FROM products WHERE PRODUCT_ID = %s ', (productId))
    data = cursor.fetchone()
    # print(data)
    row=list(data)
    print(row)
    cursor.execute('SELECT * FROM recomdedpro WHERE productid = %s ', (productId))
    reviews = cursor.fetchall()
    
    return render_template('viewproadmin.html',row=row,reviews=reviews)

################################################################################################################################
@app.route('/upload',methods=['POST','GET'])
def upload():
    USERID=session['uid']
    if request.method == "POST":
        print("===============================================")
        file = request.files['file']
        print(file)
           
         
        filename = secure_filename(file.filename)
        print(filename)
        file.save(os.path.join(app.config['UPLOADED_PHOTOS_DEST2'], filename))
        img = cv2.imread("static/skindetecttype/"+str(filename))
           
         
        image_size=224
        #img = cv2.imread(path1+"//"+i)
        path="static/skindetecttype/"+"//"+str(filename)
        img = image.load_img(path, target_size=(image_size, image_size))
        x = image.img_to_array(img)
        print(type(x))
        img_4d=x.reshape(1,224,224,3)
          
        predictions = model.predict(img_4d)
        print(predictions)
        pred=np.argmax(predictions[0])
        print("===============================================")
        print(pred)
        print("===============================================")
        dict1 = {0:'Combination',1:'Dry',2:'Normal',3:'Oily'}
        op=dict1[pred]
        print(op)
           
        if op == "Combination":
             final_prediction = "Combination"
        elif op == "Dry":
             final_prediction = "Dry"
        elif op == "Oily":
             final_prediction = "Oily"
        elif op == "Normal":
             final_prediction = "Normal"
        else:
             final_prediction = "Unknown"
        
        message = "Cosmetics suggestion System based on Skin Condition" +" "+ final_prediction
        
        print(message)
        
        rec_lst = []
        try:
            rec_lst = recommend(int(USERID))
            print("in")
            print(rec_lst)
        except:
            print("outy")
            rec_lst = [1,2]
            print(rec_lst)
          
        mainrowlst = []
        for k in rec_lst:
            cursor.execute('SELECT * FROM products WHERE PRODUCT_ID = %s;',(str(k)))
            row = cursor.fetchall()
            print(row)
            mainrowlst.append(row)
            
        
        jsonObj = json.dumps([mainrowlst,message,path])
           
        return jsonObj 
  
    return jsonObj
       
      
       
    #    cursor.execute('SELECT * FROM products where TYPE= %s;',(str(final_prediction)))
    #    row = cursor.fetchall()
    #     # print(row)
    #     # jsonObj = json.dumps(row)
    #    jsonObj = json.dumps([row,message,path])
       
    #    print("jsonObj")
    #    print(jsonObj)
    #    return jsonObj
     
    # return jsonObj


#################################################recommended product###############################################################################
def recommend(USERID):
    conn = dbConnection()
    cur = conn.cursor()
    sql="SELECT USERID,productid,rating from recomdedpro"
    cur.execute(sql)
    table_rows = cur.fetchall()
    print(table_rows)
    df = pd.DataFrame(table_rows,columns=['USERID','productid','rating'])
    #df.to_csv("Reco.csv")
    print()
    print("printign np.unique(df['productid']")
    print(np.unique(df['productid']))
    a=len(np.unique(df['productid']))

    print()
    print("printing a")
    print(a)
    print()
    df = df.astype({"USERID": int,"productid": int,"rating": int })
    ratings_utility_matrix=df.pivot_table(values='rating', index='USERID', columns='productid', fill_value=0)
    X = ratings_utility_matrix.T
    print("---------------------------")
    print(X)
    print("--------------------")
    import sklearn
    from sklearn.decomposition import TruncatedSVD
    SVD = TruncatedSVD(n_components=int(2))
    decomposed_matrix = SVD.fit_transform(X)
    correlation_matrix = np.corrcoef(decomposed_matrix)
    print("==========")
    print(correlation_matrix)
    i = USERID
    
    product_names = list(X.index)
    print('----------------product_names-------------------')
    print(product_names)
    print(i)
    print('-----------------------------------')
    product_ID = product_names[i]
    correlation_product_ID = correlation_matrix[product_ID]
    Recommend = list(X.index[correlation_product_ID > 0.70])
#     Recommend.remove(i) 
    print("complete")
    
    return Recommend[0:3]




if __name__ == '__main__':
    # app.run(debug=True)
    app.run('0.0.0.0')