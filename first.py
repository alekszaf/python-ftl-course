import serial

device = serial.Serial('COM9', baudrate=115200)

device.write(b'IDN\n')
answer = device.readline()
print(f'The answer is: {answer}')
device.close()

#This is just a comment to test git in VS code