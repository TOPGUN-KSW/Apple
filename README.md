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
1. Install the modules using pip install
attrs                        22.1.0
click                        8.1.3
colorama                     0.4.6
dill                         0.3.6
fastapi                      0.80.0
Flask                        2.2.2
flatbuffers                  2.0
fonttools                    4.29.0
keras                        2.11.0
Keras-Preprocessing          1.1.2
natsort                      8.2.0
networkx                     2.8.8
numba                        0.56.4
numpy                        1.21.6
oauthlib                     3.2.0
onnxruntime                  1.12.1
opencv-python                4.5.5.62
opencv-python-headless       4.6.0.66
opt-einsum                   3.3.0
packaging                    21.3
pandas                       1.5.1
Pillow                       9.2.0
pip                          22.3.1
protobuf                     3.19.4
pyasn1                       0.4.8
pyasn1-modules               0.2.8
pydantic                     1.10.2
PyMatting                    1.1.8
pyparsing                    3.0.7
pyreadline3                  3.4.1
PySocks                      1.7.1
python-dateutil              2.8.2
python-multipart             0.0.5
pytz                         2022.6
PyWavelets                   1.4.1
rembg                        2.0.25
requests                     2.27.1
requests-oauthlib            1.3.1
rsa                          4.8
scikit-image                 0.19.3
scikit-learn                 1.1.3
scipy                        1.7.3
sympy                        1.11.1
tdqm                         0.0.1
tensorboard                  2.11.0
tensorboard-data-server      0.6.1
tensorboard-plugin-wit       1.8.1
tensorflow                   2.11.0
tensorflow-estimator         2.11.0
tensorflow-gpu               2.7.0
tensorflow-intel             2.11.0
tensorflow-io-gcs-filesystem 0.23.1
torch                        1.13.1
torchaudio                   0.13.1
torchvision                  0.14.1
watchdog                     2.1.9
Werkzeug                     2.2.2
2. Download all the files from the Github directory written below
KSW_2022_Fall_Program/TopGun/code/Flask/
3. Then name the folder to 'Flask'
4. Download all the files from the Shared Google Drive directory written below
Shared with me/Dataset/models
5. Then, place the downloaded files from Shared Google Drive into the Flask folder
6. Run CMD and type in the command below to run the Flask server
python server.py
### Android
1. Run the Android application after running the server.


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


   
