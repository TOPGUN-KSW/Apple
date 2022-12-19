#### KSW 2022 Fall Program
# 🍎 Predicting the sweetness of multiple apples by applying apple images on Hybrid Machine Learning: Machine Learning and Deep Learning    


## Team TopGun
    
| Name         |Call sign| University               | Department                                   | Email               | Github    |
| :-----------------:| :---------: | :------------------------: | :------------------------------------: | :-------------------: | :-------------------------: |
| Heejun Park |YODA   | Yeonsei Univ.| Computer and Telecommunications Engineering|parkie0517@gmail.com| https://github.com/parkie0517|
| Hanbi Kim |PHEONIX  | Chungbuk Nat'l Univ.   | Computer Science | hanbikim20@g.cbnu.ac.kr  | https://github.com/hanbikim    |
| Jeongho Ha |JAY | Jeju Nat'l Univ.       | Computer Engineering | hjh4212@naver.com| https://github.com/hjh1248    |
| Seokkhyeon Heo|EASY | Jeju Nat'l Univ.   | Blockchain Security |gj4535@gmail.com| https://github.com/gj1515   |
| Taeyun Kim |KAMTAE  | Jeju Nat'l Univ.  | Tourism Management & Big Data Science |persimm0ncrack@gmail.com| https://github.com/kamtae |
| Jeffrey Tsai| GOKU | Purdue Univ.  | Computer & Information Technology | jeffrey051622@gmail.com    ||
| Kyungrock Kwon| ROCK | Purdue Univ.  | Systems Analysis & Design |kyungrock99@gmail.com |  |

<br>

## Research problem statement
Farmers harvest apples without checking the sweetness level. They pick all apples and send them to Agricultural Products Processing Center (APC). Then a machine in APC measures their level. The problem is to harvest apples without knowing the Brix value, i.e., not checking whether it has commercial value. it is challenging for farmers to predict the optimal harvesting time based only on their experience. For consumers, it is difficult to select the best apples in terms of sugar level or sweetness.     

There are two universal ways to measure sugar levels: The destructive sugar levels measurement method (DM) and the Non-destructive sugar levels measurement method (NDM). DM measures sugar levels by testing the juice from cut fruits. It is a more affordable method than NDM. A disadvantage is that cut fruits lose their value to be sold. NDM displays sugar levels by detecting the reflected wavelength from the apples that were irradiated to near-infrared. It measures the sweetness of apples without damaging the fruits and shows the sugar levels immediately. However, the method is expensive, and the accuracy of the outputs is not stable. 

<br>

## Overview
<img src="https://user-images.githubusercontent.com/74577775/208288156-982ce322-40cf-445e-b77b-bc0fa2b04fef.png" width="1000" height="400"></img>


## Research novelty
    1. Develop a Hybrid Machine Learning (HML) model that combines ML and DL models.
    2. Predict apple sweetness(Brix level) from apple images taken by a smartphone.
    3. Detect multiple apples and provide appel sweetness(Brix level) of apples at once.

<br>

## How to run the project
#### Download the Dataset folder from google Drive

### Machine Learning
1. Install the modules using the below command at the terminal.  
pip install pandas  
pip install numpy  
pip install sckit-learn  
pip install joblib  
2. Insert the low.pkl, medium.pkl, high.pkl files into the path of Machine_Learning/ensemble/models/ from ML_3models folder in dataset
3. You can set the terminal path to '.../Machine_Learning/' and execute it.
### Deep Learning
1. Insert the Final_3Class_Effiv2_l file into the decompressed Dataset folder.
### Flask Server
1. Install the modules using pip install<br>
attrs                        22.1.0 <br>
click                        8.1.3 <br>
colorama                     0.4.6 <br>
dill                         0.3.6 <br>
fastapi                      0.80.0 <br>
Flask                        2.2.2 <br>
flatbuffers                  2.0 <br>
fonttools                    4.29.0 <br>
keras                        2.11.0 <br>
Keras-Preprocessing          1.1.2 <br>
natsort                      8.2.0<br>
networkx                     2.8.8<br>
numba                        0.56.4<br>
numpy                        1.21.6<br>
oauthlib                     3.2.0<br>
onnxruntime                  1.12.1<br>
opencv-python                4.5.5.62<br>
opencv-python-headless       4.6.0.66<br>
opt-einsum                   3.3.0<br>
packaging                    21.3<br>
pandas                       1.5.1<br>
Pillow                       9.2.0<br>
pip                          22.3.1<br>
protobuf                     3.19.4<br>
pyasn1                       0.4.8<br>
pyasn1-modules               0.2.8<br>
pydantic                     1.10.2<br>
PyMatting                    1.1.8<br>
pyparsing                    3.0.7<br>
pyreadline3                  3.4.1<br>
PySocks                      1.7.1<br>
python-dateutil              2.8.2<br>
python-multipart             0.0.5<br>
pytz                         2022.6<br>
PyWavelets                   1.4.1<br>
rembg                        2.0.25<br>
requests                     2.27.1<br>
requests-oauthlib            1.3.1<br>
rsa                          4.8<br>
scikit-image                 0.19.3<br>
scikit-learn                 1.1.3<br>
scipy                        1.7.3<br>
sympy                        1.11.1<br>
tdqm                         0.0.1<br>
tensorboard                  2.11.0<br>
tensorboard-data-server      0.6.1<br>
tensorboard-plugin-wit       1.8.1<br>
tensorflow                   2.11.0<br>
tensorflow-estimator         2.11.0<br>
tensorflow-gpu               2.7.0<br>
tensorflow-intel             2.11.0<br>
tensorflow-io-gcs-filesystem 0.23.1<br>
torch                        1.13.1<br>
torchaudio                   0.13.1<br>
torchvision                  0.14.1<br>
watchdog                     2.1.9<br>
Werkzeug                     2.2.2<br>
2. Download all the files from the Github directory
->**KSW_2022_Fall_Program/TopGun/code/Flask/**
3. Then name the folder to 'Flask'
4. Download all the files from the Shared Google Drive directory
->**Shared with me/Dataset/Flask**
5. Then, place the downloaded files from Shared Google Drive into the Flask folder
6. Type **python server.py** command to run the Flask server in CMD


### Android
1. Run the flask sever.
2. In ResultActivty.java and Sever.java, change the String ipv4Address value to 2nd ip address at the CMD when running the flask
3. In ResultActivty.java and Sever.java, change the String portNumber to 2nd port number at the CMD when running the flask

<br>

## Environment Setting
### Preprocessing
    - YOLO V4
### Machine Learning
    - Python 3.8.2
    - scikit-learn
### Deep Learning    
    - Python 3.8.16
    - Pytorch 1.13.0+cu116
    - EfficientNetV2-l
### Andriod Application
    - Gradle version 7.4
    - Android sdk 32
    - Glide 4.14.2
### Server
    - Flask okhttp 4.10.0


   
<br><br>
