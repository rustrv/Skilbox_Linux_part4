import time
def move_forward():
    print("Робот движется вперед")
    #например GPIO.output(motor1_pin1, GPIO.HIGH)
    time.sleep(2)  # Робот движется вперед в течение 2 секунд
    stop_motors()

def move_backward():
    print("Робот движется назад")
    time.sleep(2)
    #например GPIO.output(motor2_pin1, GPIO.HIGH)
    stop_motors()

def stop_motors():
    print("Двигатели остановлены")
    #например GPIO.output(motor1_pin1, GPIO.LOW)
    # аппапример GPIO.output(motor2_pin1, GPIO.LOW)

try:
    move_forward()
    time.sleep(1)
    move_backward()
    time.sleep(1)
    stop_motors()

except KeyboardInterrupt:
    pass