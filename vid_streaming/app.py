from flask import Flask,render_template,Response
import cv2
app = Flask(__name__)
camera = cv2.VideoCapture(0)#using the system default camera
while True:
def generate_frames():
    while True:##to 
    ##read the camera frame
        success,frame = camera.read()##the .read() method has return two values i.e. if the camera is running,the frames if the camera is running
        if not success:
            break
        else:
            ret,buffer=cv2.imencode('.jpg',frame)

@app.route('/')
def Welcome():
    return render_template('index.html')

@app.route('/video')
def video():#video pass-on
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug =True)