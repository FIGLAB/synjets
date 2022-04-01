import serial
import time
arduino = serial.Serial(port='COM11', baudrate=115200, timeout=1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    arduino.flush()
    time.sleep(0.5)
    data = arduino.readline()
    print(data) # printing the value
    return data

# value = write_read("left")
# value = write_read(str("left"))
arduino.write(bytes("right", 'utf-8'))
arduino.flush()
time.sleep(0.5)
data = arduino.readline()
print(data) # printing the value

time.sleep(2)
x = "left"
print(x)
arduino.write(bytes(x, 'utf-8'))
arduino.flush()
time.sleep(0.5)
data = arduino.readline()
print(data) # printing the value

time.sleep(2)
write_read("right")
# while True:
#     word = input("Enter word: ") # Taking input from user
#     print(word)
#     print(type(word))
#     print(word=="left")
#     print(word==b'left')
#     value = write_read(word)

arduino.close()
