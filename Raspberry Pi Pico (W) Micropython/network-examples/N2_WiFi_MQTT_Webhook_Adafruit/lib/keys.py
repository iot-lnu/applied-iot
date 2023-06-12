import ubinascii              # Conversions between binary data and various encodings
import machine                # To Generate a unique id from processor

# Wireless network
WIFI_SSID =  "Your_WiFi_Name"
WIFI_PASS = "Your_WiFi_Password" # No this is not our regular password. :)

# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "Your_Adafruit_User_Name"
AIO_KEY = "Your_Adafruit_Application_Key"
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
AIO_LIGHTS_FEED = "Your_lights_Feed_Address"
AIO_RANDOMS_FEED = "Your_randoms_Feed_Address"