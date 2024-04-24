import cv2
import mediapipe as mp
import time
import math
import util
from playsound import playsound
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# face bounder indices
FACE_OVAL=[ 10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288, 397, 365, 379, 378, 400, 377, 152, 148, 176, 149, 150, 136, 172, 58, 132, 93, 234, 127, 162, 21, 54, 103,67, 109]

# lips indices for Landmarks
LIPS=[ 61, 146, 91, 181, 84, 17, 314, 405, 321, 375,291, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95,185, 40, 39, 37,0 ,267 ,269 ,270 ,409, 415, 310, 311, 312, 13, 82, 81, 42, 183, 78 ]
LOWER_LIPS =[61, 146, 91, 181, 84, 17, 314, 405, 321, 375, 291, 308, 324, 318, 402, 317, 14, 87, 178, 88, 95]
UPPER_LIPS=[ 185, 40, 39, 37,0 ,267 ,269 ,270 ,409, 415, 310, 311, 312, 13, 82, 81, 42, 183, 78]
# Left eyes indices
LEFT_EYE =[ 362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385,384, 398 ]
LEFT_EYEBROW =[ 336, 296, 334, 293, 300, 276, 283, 282, 295, 285 ]

# right eyes indices
RIGHT_EYE=[ 33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161 , 246 ]
RIGHT_EYEBROW=[ 70, 63, 105, 66, 107, 55, 65, 52, 53, 46 ]
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

class eyeDetection:
    def __init__(self):
        face_mesh_sol = mp.solutions.face_mesh
        faceMesh = face_mesh_sol.FaceMesh()
        mp_draw = mp.solutions.drawing_utils
        count = 0
        delay1=0
        delay2=0
        start_time = time.time()
        cam = cv2.VideoCapture(0)

        while True:
            count+=1
            ret, frame = cam.read()
            end_time = time.time()-start_time
            fps = count/end_time
            frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            result = faceMesh.process(frame_rgb)
            if result.multi_face_landmarks:
                landmark_coords=self.landmarkDetection(frame,result,False)
                left_eye_indices=[landmark_coords[p] for p in LEFT_EYE]
                right_eye_indices=[landmark_coords[p] for p in RIGHT_EYE]

                # Function to calculate distance of both eyes landmarks
                horizontal_distance, vertical_distance = self.lm_Distance(left_eye_indices,right_eye_indices,frame)
                # print('HOr-average',horizontal_distance)

                # Check Distance
                print('VVVVVVVVV',horizontal_distance)
                if vertical_distance > 9 and vertical_distance <=10:
                    cv2.putText(frame, f'Ok', (400, 50), cv2.FONT_HERSHEY_PLAIN,2, (0, 255, 0),2)
                else:
                    cv2.putText(frame, f'Not Ok...', (400, 50), cv2.FONT_HERSHEY_PLAIN,2, (0, 0, 225),2)

                if horizontal_distance < 23:
                    cv2.putText(frame, f'Out of Focus', (400, 80), cv2.FONT_HERSHEY_PLAIN,2, (0, 0, 225),2)

                    delay1+=1
                    if delay1>10:
                        print('side ',delay1)
                        self.alert()
               
                
                elif vertical_distance < 9.0:
                    cv2.putText(frame, f'Sleep/blink {vertical_distance}', (100, 100), cv2.FONT_HERSHEY_PLAIN,2, (0, 255, 0))
                    print('delay and alert', delay2)
                    delay2 += 1
                    if delay2 >4:
                        self.alert()
                        # break
                else:
                    delay1 = 0
                    delay2 = 0
                # frame=util.fillPolyTrans(frame,[landmark_coords[p] for p in FACE_OVAL],(255,255,0),0.3)
                frame=util.fillPolyTrans(frame,[landmark_coords[p] for p in RIGHT_EYE],(0,255,0),0.1)
                frame=util.fillPolyTrans(frame,[landmark_coords[p] for p in LEFT_EYE],(0,255,0),0.1)
               
                frame = util.textWithBackground(frame,'Face LandMarks',cv2.FONT_HERSHEY_PLAIN,2,(20,70),2,(0,0,255),
                                                (0,255,0),bgOpacity=0.3)
                                                
            if cv2.waitKey(1)==13:
                break

            cv2.putText(frame,str(int(fps)),(50,40),cv2.FONT_HERSHEY_PLAIN,1,(255,0,255),2)
            cv2.imshow('Frame',frame)

        cam.release()
        cv2.destroyAllWindows()
    
    def alert(self):
        playsound('alert1.mp3')

    # Detecting coordinates of landmark
    def landmarkDetection(self,img,result,draw=True):

        h,w = img.shape[:2]
        mesh_coords = [(int(point.x * w),int(point.y * h)) for point in result.multi_face_landmarks[0].landmark]
        if draw:
            [cv2.circle(img,p,2,(220,255,0),-1) for p in mesh_coords]
        return mesh_coords

    def lm_Distance(self,le_indices,re_indices,img):
        #Left eye inices point
        # horizontal line
        lx1,ly1 =le_indices[0]
        lx2,ly2 = le_indices[8]
        #vertical line
        vlx1,vly1 = le_indices[4]
        vlx2,vly2 = le_indices[13]
        # cv2.circle(img,(vlx1,vly1),2,(0,255,0),-1)

        #Right eye indices point
        # horizontal line
        rx1, ry1 = re_indices[0]
        rx2, ry2 = re_indices[8]
        # vertical line
        vrx1,vry1 = re_indices[3]
        vrx2,vry2 = re_indices[12]
        # cv2.circle(img,(vrx1,vry1),2,(0,255,0),-1)

        # cv2.line(img,(lx1,ly1),(lx2,ly2),(0,255,0),3)
        # cv2.line(img,(rx1,ry1),(rx2,ry2),(0,255,0),3)
        # cv2.line(img,(vlx1,vly1),(vlx2,vly2),(0,255,0),3)
        # cv2.line(img,(vrx1,vry1),(vrx2,vry2),(0,255,0),3)

        #Calculating distance for verticle line
        le_distance = math.sqrt((vlx1-vlx2)**2 + (vly1-vly2)**2)
        re_distance = math.sqrt((vrx1-vrx2)**2 +(vry1-vry2)**2)
        #Calculating distance for horizontal line
        leH_distance = math.sqrt((lx1-lx2)**2 +(ly1-ly2)**2)
        reH_distance = math.sqrt((rx1-rx2)**2 +(ry1-ry2)**2)
        # averg_distance fro horizontal line
        horizontal_average = (leH_distance+reH_distance)//2

        # Average for verticle line
        verticle_averagDistance = (le_distance+re_distance)//2
        return horizontal_average, verticle_averagDistance

object = eyeDetection()