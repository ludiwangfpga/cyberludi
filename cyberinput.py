from flask import Flask, render_template
from flask_socketio import SocketIO
import serial
from serial.serialutil import SerialException
import time

ser = serial.Serial('COM7', 921600, timeout=1)
try:
    # Enter "AT command mode"
    ser.write(bytes.fromhex('41 54 2b 41 54 0d 0a'))
    response = ser.read(1000)
    print(f"msg: {response}")

    # Rotate the motor forward for 1 second
    ser.write(bytes.fromhex('41 54 00 07 e8 0c 01 00 0d 0a'))
    response = ser.read(1000)
    print(f"msg: {response}")

    # Stop the motor for 1 second
    ser.write(bytes.fromhex('41 54 00 07 e8 4c 01 00 0d 0a'))
    response = ser.read(1000)
    print(f"msg: {response}")

    # Rotate the motor backward for 1 second
    ser.write(bytes.fromhex('41 54 00 07 e8 8c 01 00 0d 0a'))
    response = ser.read(1000)
    print(f"msg: {response}")

    # Stop the motor for 1 second
    ser.write(bytes.fromhex('41 54 98 07 e8 0c 08 3c 19 31 31 30 33 31 0a 0d 0a'))
    response = ser.read(1000)
    print(f"msg: {response}")
    ser.write(bytes.fromhex('41 54 30 07 e8 0c 08 01 01 00 00 00 00 00 00 0d 0a'))
    response = ser.read(1000)
    print(f"定位0点: {response}")
    time.sleep(1)
    ser.write(bytes.fromhex('41 54 30 07 e8 0c 08 01 01 00 00 00 00 00 00 0d 0a'))
    response = ser.read(1000)
    print(f"msg: {response}")
    time.sleep(1)
    ser.write(bytes.fromhex('41 54 90 07 e8 0c 08 05 70 00 00 01 00 00 00 0d 0a'))
    response = ser.read(1000)
    print(f"msg: {response}")
    ser.write(bytes.fromhex('41 54 18 07 e8 0c 08 00 00 00 00 00 00 00 00 0d 0a'))
    response = ser.read(1000)
    print(f"msg: {response}")
    time.sleep(1)
    ser.write(bytes.fromhex('41 54 18 07 e8 0c 08 00 00 00 00 00 00 00 00 0d 0a'))
    response = ser.read(1000)
    print(f"开始旋转: {response}")
    ser.write(bytes.fromhex('41 54 90 07 e8 0c 08 16 70 00 00 00 00 80 40 0d 0a'))
    response = ser.read(1000)
    print(f"停止: {response}")
    time.sleep(1)
    ser.write(bytes.fromhex('41 54 90 07 e8 0c 08 17 70 00 00 00 00 80 40 0d 0a'))
    response = ser.read(1000)
    print(f"开始旋转: {response}")
    ser.write(bytes.fromhex('41 54 90 07 e8 0c 08 16 70 00 00 00 00 e0 40 0d 0a'))
    response = ser.read(1000)
    print(f"停止: {response}")
    ser.write(bytes.fromhex('41 54 20 07 e8 0c 08 00 00 00 00 00 00 00 00 0d 0a'))
    response = ser.read(1000)
    print(f"停止模式: {response}")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the serial port
    ser.close()
