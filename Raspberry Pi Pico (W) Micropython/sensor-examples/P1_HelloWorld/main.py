import time
import machine

# Set the couter to zero
counter = 0
while True:
    print("Hello World {}".format(counter))     # Print "Hello World " with couter number
    counter = counter + 1                       # Increase couter by 1
    time.sleep(1)                               # Delay for 1 second
