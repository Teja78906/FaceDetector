import cv2

def generate_dataset(img, id, img_id):
    cv2.imwrite("user."+str(id)+"."+str(img_id)+".jpg",img)
    
def draw_boundary(img , classifier , scale_factor , minNeighbors , color , text):
    gray_img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale(gray_img, scale_factor, minNeighbors)
    coords = []
    for (x,y,w,h) in features:
        cv2.rectangle(img , (x,y),(x+w,y+h),color,2)
        cv2.putText(img , text, (x,y-4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
        coords = [x,y,w,h]
    return coords, img

def detect(img , faceCascade, img_id):
    color = {"blue":(255,0,0), "red":(0,0,255), "green":(0,255,0)}
    coords , img = draw_boundary(img , faceCascade , 1.1 , 10, color['green'], "face")
    
    if len(coords)==4:
        x,y,w,h = coords
        roi_img = img[ y:y+h , x:x+w]
        user_id = 1
        generate_dataset(roi_img, user_id, img_id)
#         roi_img = img[ y:y+h , x:x+w]
#         coords = draw_boundary(roi_img , eyeCascade , 1.1 , 14, color['red'],"eye")
#         coords = draw_boundary(roi_img , noseCascade, 1.1 , 5, color['red'],"nose")
#         coords = draw_boundary(roi_img ,mouthCascade , 1.1 , 20, color['red'],"mouth")
        
    return img

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# eyesCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
# noseCascade = cv2.CascadeClassifier( 'nose.xml')
# mouthCascade = cv2.CascadeClassifier('mouth.xml')
img_id = 0
video_capture = cv2.VideoCapture(0)   
while True:
    _,img = video_capture.read()
     # Flip the frame horizontally
    img = cv2.flip(img, 1)
    img = detect(img , faceCascade ,img_id)
    cv2.imshow("face_detection",img)
    img_id+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()