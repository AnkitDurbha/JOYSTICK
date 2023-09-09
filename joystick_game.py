import RPi.GPIO as GPIO
import time
from ADCDevice import *
import turtle
import random
t = turtle.Turtle()
t.speed(0)

Z_Pin = 12      # define Z_Pin
adc = ADCDevice() # Define an ADCDevice class object

def setup():
    global adc
    if(adc.detectI2C(0x48)): # Detect the pcf8591.
        adc = PCF8591()
    elif(adc.detectI2C(0x4b)): # Detect the ads7830
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Z_Pin,GPIO.IN,GPIO.PUD_UP)   # set Z_Pin to pull-up mode
def play_game():
    level_counter = turtle.Turtle()
    counter = 1
    t.penup()
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    t4 = turtle.Turtle()
    t5 = turtle.Turtle()
    t1.penup()
    t2.penup()
    t3.penup()
    t4.penup()
    t5.penup()
    t1.speed(0)
    t2.speed(0)
    t3.speed(0)
    t4.speed(0)
    t5.speed(0)
    t.goto(-470, -300)
    t.pendown()
    t.goto(470, -300)
    t.goto(-470,-300)
    t.penup()
    t1.goto(random.randint(-400, 400), -300)
    t2.goto(random.randint(-400, 400), -300)
    t3.goto(random.randint(-400, 400), -300)
    t4.goto(random.randint(-400, 400), -300)
    t5.goto(random.randint(-400, 400), -300)
    
    t1.shape('circle')
    t2.shape('circle')
    t3.shape('circle')
    t4.shape('circle')
    t5.shape('circle')
    level_counter.penup()
    level_counter.speed(0)
    level_counter.goto(-300, 300)
    level_counter.hideturtle()
    start_time = time.time()
    while counter <= 10:
        val_Z = GPIO.input(Z_Pin)
        val_X = adc.analogRead(1)
        level_counter.write('Level: ' + str(counter), font=("Courier New", 16, "normal"))
        if val_X > 150:
            t. seth(0)
            t.forward(10)
        elif val_X < 40:
            t.seth(180)
            t.forward(10)
        elif val_Z == 0:
            t.seth(90)
            t.forward(30)
            time.sleep(0.2)
            t.backward(30)
        if val_X > 150 and val_Z == 0:
            t. seth(90)
            t.forward(30)
            t.right(90)
            t.forward(20)
            t.right(90)
            t.forward(30)
        elif val_X < 40 and val_Z == 0:
            t. seth(90)
            t.forward(30)
            t.left(90)
            t.forward(20)
            t.left(90)
            t.forward(30)
        if t.xcor() > 470:
            counter += 1
            t.goto(-470, -300)
            t1.goto(random.randint(-400, 400), -300)
            t2.goto(random.randint(-400, 400), -300)
            t3.goto(random.randint(-400, 400), -300)
            t4.goto(random.randint(-400, 400), -300)
            t5.goto(random.randint(-400, 400), -300)
            level_counter.clear()
        elif t.xcor() < -470:
            t.goto(-470, -300)
        if t.xcor() > t1.xcor() and t.xcor() < t1.xcor() + 15:
            t.goto(t1.xcor(), -300)
        elif t.xcor() > t2.xcor() and t.xcor() < t2.xcor() + 15:
            t.goto(t2.xcor(), -300)
        elif t.xcor() > t3.xcor() and t.xcor() < t3.xcor() + 15:
            t.goto(t3.xcor(), -300)
        elif t.xcor() > t4.xcor() and t.xcor() < t4.xcor() + 15:
            t.goto(t4.xcor(), -300)
        elif t.xcor() > t5.xcor() and t.xcor() < t5.xcor() + 15:
            t.goto(t5.xcor(), -300)
        
    gold = turtle.Turtle()
    gold.shape('circle')
    gold.color('gold')
    gold.speed(0)
    gold.penup()
    gold.goto(0, 0)
    gold.shapesize(10, 10)
    t.goto(-100, 0)
    t.hideturtle()
    end_time = time.time()
    elapsed_time = round(end_time - start_time, 0)
    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()
    t4.hideturtle()
    t5.hideturtle()
    t.write('It took you ' + str(elapsed_time) + ' seconds to beat the game!')

def destroy():
    adc.close()
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        play_game()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()