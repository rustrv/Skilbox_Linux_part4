import time
def move_forward():
    print("Робот движется вперед")
    for duty_cycle in range(0, 101, 10):  # Постепенное увеличение скорости
        print("скорость: ",duty_cycle)
        # Здесь команда на шим контроллер например типа *.*(duty_cycle)
        time.sleep(1)


    stop_motors()



def move_backward():
    print("Робот движется назад")
    for duty_cycle in range(0, 101, 10):  # Постепенное увеличение скорости
        print("скорость: ", duty_cycle)
        # Здесь команда на шим контроллер например типа *.*(duty_cycle)
        time.sleep(1)
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