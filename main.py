import cv2
import time
from my_functions import *


source = 'test_video.mp4'

#cap = cv2.VideoCapture(0)

frame_size = (640, 480) 
save_video = False  
show_video = True  
save_img = False  

cap = cv2.VideoCapture(source)

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        frame = cv2.resize(frame, frame_size)  # resizing image
        original_frame = frame.copy()
        frame, results = object_detection(frame)

        rider_list = []
        head_list = []
        number_list = []

        for result in results:
            x1, y1, x2, y2, cnf, clas = result
            if clas == 0:
                rider_list.append(result)
            elif clas == 1:
                head_list.append(result)
            elif clas == 2:
                number_list.append(result)


        for rdr in rider_list:
            time_stamp = str(time.time())
            x1r, y1r, x2r, y2r, cnfr, clasr = rdr
            for hd in head_list:
                x1h, y1h, x2h, y2h, cnfh, clash = hd
                if inside_box([x1r, y1r, x2r, y2r], [x1h, y1h, x2h, y2h]):  # if this head inside this rider bbox
                    try:
                        head_img = original_frame[y1h:y2h, x1h:x2h]
                        helmet_present = img_classify(head_img)
                    except:
                        helmet_present[0] = None

                    if helmet_present[0] == True:  # if helmet P
                        frame = cv2.rectangle(frame, (x1h, y1h), (x2h, y2h), (0, 255, 0), 1)
                        frame = cv2.putText(frame, f'{round(helmet_present[1], 1)}', (x1h, y1h + 40),
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    elif helmet_present[0] == None:  # Poor P
                        frame = cv2.rectangle(frame, (x1h, y1h), (x2h, y2h), (0, 255, 255), 1)
                        frame = cv2.putText(frame, f'{round(helmet_present[1], 1)}', (x1h, y1h),
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    elif helmet_present[0] == False:  # if helmet A
                        frame = cv2.rectangle(frame, (x1h, y1h), (x2h, y2h), (0, 0, 255), 1)
                        frame = cv2.putText(frame, f'{round(helmet_present[1], 1)}', (x1h, y1h + 40),
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                        try:
                            number_plate_img = original_frame[y2r:y2r + int(0.3 * (y2r - y1r)), x1r:x2r]
                            cv2.imwrite(f'number_plates/{time_stamp}.jpg', number_plate_img)
                        except:
                            print('Could not save number plate')

        if save_img:  # save img
            cv2.imwrite('saved_frame.jpg', frame)
        if show_video:  # show video
            frame = cv2.resize(frame, (900, 450))  # resizing to fit on the screen
            cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break



cap.release()
cv2.destroyAllWindows()
print('Execution completed')
