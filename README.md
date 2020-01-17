Automatic Car Light Adjuster

      
Contents: -
1.	Overview
2.	Things used in this project
a.	Hardware Components
b.	Software apps and Online Services
3.	Story
a.	Introduction
b.	Demonstration
c.	Hardware Connections
d.	Schematics
e.	Complete Code to run the design     

 
                                                                                        

Overview: -

Automatic adjust lights of cars from main light to dipper light when the opposite side car’s light glare emits on the LDR sensor to avoid the accidents in nights, after both the cars passes each other then the light come again in its actual state.

 
 
                                                                                                   
Things used in project: -

Hardware Components:
1.	Bolt IoT Bolt Wi-Fi Module
2.	USB-A to Mini-USB Cable
3.	LDR Sensor
4.	2 Resistance 330 ohms
5.	5 mm LED: Yellow and White
6.	Male to Male Breadboard Jumper Dupont
7.	Male to Male Jumper Wires



Software Components:
1.	Bolt IoT Android App
2.	Linux Mint


         

 
Story: -
Introduction: -
IoT is changing and Improving our living style day by day. We all were hear about auto driving car and Smart Summon. Nowadays lots of companies are working on self-driving car and achieving their goal too. My main aim to build this project is to prevent the road accidents which happens in night time due to glare of car’s headlight which emits directly on opposite side car’s driver.
Sometimes the car drivers are forgot to switch the light from Headlight to Dipper in night when they are passing from any other car. The glare of the car’s headlights is very high and when it emit on the opposite side car’s driver eyes, then he/she lost the control on their car and accident will happen.

                    


                                   

Demonstration: -                 

We know that IoT are also used in cars to make then smart. Like when we are about to reach home then the doors of garage will automatic open and we are able to park our car there. Same as I am also going to use IoT concept to solve this car’s headlight glare problem to prevent accidents. 
  
I am going to use LDR Sensor which senses the intensity of light and also set a Maximum limit value e.g. 500. 
If the sensor value is small than 500(which means the Intensity of light of opposite side car’s headlight is not much and it is safe to pass) then the main headlight will be On, and If the sensor value is greater than 500 ( which means the Intensity of light of opposite side car’s headlight is very high and it is not safe to pass with that condition) then the main headlight will be automatically turned OFF and at the same time Dipper light of the car will be turned ON, and then it is good to go. This can work along with the manual mode means driver can switch the main headlight and dipper light manually. If we install this system in all car (Normal cars or Automated cars) then all cars can pass safely without losing any lives. 

     










 
Hardware Connections: -

 

 
1.	We connect one pin of LDR Sensor to 3V3 input pin and other pin of LDR Sensor is to A0 output pin of Bolt Wi-Fi module. We also use 1 Resistance of 330 ohms which is connected with A0 output pin and GND pin of Bolt Wi-Fi Module.
2.	We connect 1st LED (as main headlight of car) Small leg of LED is -ve and Large leg of LED is +ve side. Connect the Large leg of LED with GPIO 0 pin and Small leg of LED to GND along with the 330 ohms Resistance.
3.	We connect 2nd LED (as Dipper light of car) Small leg of LED is -ve and Large leg of LED is +ve side. Connect the Large leg of LED with GPIO 1 pin and Small leg of LED to GND along with the 330 ohms Resistance.
4.	And we are done here.













 
Schematics: -
Now from here our coding part is going to start:

I have done this project on Linux Mint OS, and here is the process to achieve this. 
Update the packages on Linux Mint OS
Execute the command below so that the packages on Linux Mint are updated to the latest version. If you skip this step, you may encounter an error while installing the Boltiot package.

sudo apt-get -y update

Install python3 pip3
pip3 is a package manager for python3 used to install and manage packages and python libraries. It is system independent.
Install pip3 using the following command,

sudo apt install python3-pip

Installing boltiot library using pip
Now we will install the boltiot python library on your Ubuntu server.
Type the below command in terminal to install boltiot python library.

sudo pip3 install boltiot

Now we are done with bolt.

Now its time to get the Bolt Wi-Fi module API_Key and Device_ID
1.	Go to your Bolt Cloud Account
The API key and Device ID of the Bolt module can be determined as follows:
•	Connect your Bolt Device to the Bolt Cloud as per instructions given at https://cloud.boltiot.com/.
•	The following screen will appear after that.The Bolt Device ID is highlighted in yellow.






 
 
•	Go to the API section to know the API Key
 
 



	

