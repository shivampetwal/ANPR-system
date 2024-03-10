
# Automatic-Number-Plate-Detection-For-Motorcyclists-Riding-Without-Helmet

## STEPS 

    1. Clone the repository:
        * git clone https://github.com/shivampetwal/ANPR-system.git
    
    2. Navigate to the project directory : 
        * cd ANPR-system
        
    3. install the required libraries using: 
        * pip install -r requirements.txt

    4. Run the main script:
        * py main.py
        * To quit the running application, press 'Q'.


 <img src="./imggif.gif"/>




## WORKING 

    1. Object Detection 📸
            * Utilize the YOLOv5 algorithm to detect key elements: the rider, license plate, 
              and the rider's head.
    
    2. Helmet Detection : 🪖🏍️
        * Implement an image classifier, specifically ResNet50, to determine whether the 
          rider is wearing a helmet.
        
    3. Decision-Making: 🤔💭✅
        * If the classifier indicates the rider is not wearing a helmet:
            + Save the license plate number in an image folder.
            + Capture an image of the rider in a separate folder.




## Technologies Used: 

    1. YOLOv5 Algorithm : 
            * YOLOv5 facilitates real-time object detection, efficiently identifying riders,
              license plates, and heads in images.
    
    2. ResNet50 Image Classifier : 
            * ResNet50, a robust image classifier, determines whether detected riders are 
              wearing helmets.
        
    3. OpenCV (cv2) : 
            * OpenCV handles image processing tasks, aiding in capturing, manipulating, 
              and integrating with YOLOv5

    4. PyTorch (torch) and torchvision:
            * PyTorch and torchvision form the foundation for neural network implementation,
              supporting YOLOv5 integration.

    5. Python Libraries (pandas, numpy, tqdm, matplotlib) :
            * Essential Python libraries are used for data manipulation, array operations, 
              and progress visualization.
    
    6. PyYAML
            * PyYAML manages configuration files, crucial for handling YOLOv5 parameters and settings.

    7. Seaborn and SciPy:
            * Seaborn and SciPy contribute to data visualization and scientific computing, enhancing
              plot generation and specific functionalities.

