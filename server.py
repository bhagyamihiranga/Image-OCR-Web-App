from flask import Flask,render_template,send_file,session,request,redirect
import pytesseract 
import wget
import os
import cv2 
app = Flask(__name__)

app.secret_key = 'i_dont_have_a_girl_fraind'

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        if os.path.isfile('./download.png'):
           os.remove('download.png')
          
           if request.form.get('url') == "":
               if  request.files['img'].filename == '':
                    return redirect('/')
               else:
                   file = request.files['img']
                   file.save(dst='./download.png')
                   try:
                     
                        img_data = cv2.imread('./download.png')
                        grey = cv2.cvtColor(img_data,cv2.COLOR_BGR2RGB)
                                
                        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
                        convert_data = pytesseract.image_to_string(grey)
                                
                                
                        with open('test.txt','w',encoding='utf-8') as file:
                                file.write(convert_data)
                                session['sucess'] = convert_data
                                return redirect('/download')
                            
                   except Exception as e:
                              return redirect('/')
           else:
                 
                  try:
                    wget.download(url=request.form.get('url'),out='download.png')
                    img_data = cv2.imread('./download.png')
                    grey = cv2.cvtColor(img_data,cv2.COLOR_BGR2RGB)
                            
                    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
                    convert_data = pytesseract.image_to_string(grey)
                            
                            
                    with open('test.txt','w',encoding='utf-8') as file:
                            file.write(convert_data)
                            session['sucess'] = convert_data
                            return redirect('/download')
                        
                  except Exception as e:
                       return redirect('/')
                
            

          
        else:
           
            

           if request.form.get('url') == "":
               if request.files['img'].filename == '':
                    return redirect('/')
               else:
                   file = request.files['img']
                   file.save(dst='./download.png')
                   try:
                      
                        img_data = cv2.imread('./download.png')
                        grey = cv2.cvtColor(img_data,cv2.COLOR_BGR2RGB)
                                
                        pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
                        convert_data = pytesseract.image_to_string(grey)
                                
                                
                        with open('test.txt','w',encoding='utf-8') as file:
                                file.write(convert_data)
                                session['sucess'] = convert_data
                                return redirect('/download')
                            
                   except Exception as e:
                              return redirect('/')
           else:
                 
                  try:
                    wget.download(url=request.form.get('url'),out='download.png')
                    img_data = cv2.imread('./download.png')
                    grey = cv2.cvtColor(img_data,cv2.COLOR_BGR2RGB)
                            
                    pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
                    convert_data = pytesseract.image_to_string(grey)
                            
                            
                    with open('test.txt','w',encoding='utf-8') as file:
                            file.write(convert_data)
                            session['sucess'] = convert_data
                            return redirect('/download')
                        
                  except Exception as e:
                       return redirect('/')
                
            

@app.route("/download",methods=['POST','GET'])
def download():
   if session.get('sucess'):
       if request.method == "GET":
           return render_template('download.html',content=session.get('sucess'))
       else:
           session.pop('sucess')
           return send_file('./test.txt',download_name="Fike.txt",as_attachment=True)
           
   else:
      return redirect('/')

app.run('0.0.0.0',port=4500,debug=True)