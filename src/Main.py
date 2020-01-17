"""
Project Title: Automatic car light Adjuster
Author: Abhishek Rai
Project Description: Automatic adjust lights of cars from main light to dipper light
when the opposite side car’s light glare emits on the LDR sensor to avoid the accidents
in nights. after both the cars passes each other then the light come again in its actual state.



"""

from boltiot import Bolt
import json, time


class CarLight:
    def __init__(self):
        # Enter your own generated bolt API Key & Your own Device Id
        self.api_key = "638f9a4d-809a-4e47-ac2a-4436e195b503"
        self.device_id = "BOLT290339"

        # Setting Threshold value
        self.maximum_limit = 170

        ## Connecting to the bolt IoT Module
        self.mybolt = Bolt(self.api_key, self.device_id)
        print(format("Automatic Car light Controller and Adjuster", '_^50'))
        self.error = '{"success": "0", "message": "A Connection error occurred"}'
        self.offline = '{"value": "offline", "time": null, "success": 1}'

    def start(self):
        #  Checking Bolt Device is offline or Online
        result = self.mybolt.isOnline()
        if result == self.error:
            print("\n Check weather your computer or bolt device is connected to Internet.....")
        elif result == self.offline:
            print("\n Bolt Device is offline")
        else:
            while True:
                print("\n Collecting Value from Sensor")
                # Collecting Response from the sensor
                response = self.mybolt.analogRead('A0')
                data = json.loads(response)
                if data['value'].isnumeric():
                    intent = int(data['value'])
                    print("value from sensor is: " + str(intent))
                    # Comparing Light Intensity & Threshold Value
                    if intent > self.maximum_limit:
                        # If light Intensity is Higher Than Threshold Value Then Dipper is On.
                        analog_ack = self.mybolt.analogWrite('1', '120')
                        digital_ack = self.mybolt.digitalWrite('0', 'LOW')
                        print("Car's Dipper light is On ")
                    else:
                        # Else Main Headlight is On & Dipper is Off
                        analog_ack = self.mybolt.digitalWrite('0', 'HIGH')
                        digital_ack = self.mybolt.digitalWrite('1', 'LOW')
                        print("Car's main Headlight is On")
                else:
                    print(f"[Error] {data['value']}")
                time.sleep(1)


def main():
    carLight = CarLight()
    carLight.start()


if __name__ == '__main__':
    main()
