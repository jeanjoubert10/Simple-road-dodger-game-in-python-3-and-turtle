# Simple Road Dodger Game in Pyton 3 and Turtle
# Written in osX and IDLE J Joubert 5 Jan 2020
# May need some speed adjustment in windows (time.sleep)

# Playing with simple background and gif animation

import turtle
import time
import random


win = turtle.Screen()
win.title('Road gif animation')
win.setup(510,510)
win.bgpic('1.gif')
win.tracer(0)
win.listen()

road_list = ['1.gif', '2.gif', '3.gif', '4.gif', '5.gif', '6.gif', '7.gif',
             '8.gif', '9.gif', '10.gif', '11.gif']

car_list = ['car1.gif', 'car2.gif', 'car3.gif']

rock_list = ['rock1.gif', 'rock2.gif', 'rock3.gif', 'rock4.gif']

crash_list = ['crash1.gif', 'crash2.gif']

counter = 0
back_index = 0
car_index = 0


def animate_background():
    global back_index
    
    win.bgpic(road_list[back_index])
    back_index += 1
    if back_index == 11:
        back_index = 0


for i in car_list:
    win.register_shape(i)

for rock in rock_list:
    win.register_shape(rock)

for crash in crash_list:
    win.register_shape(crash)

car = turtle.Turtle()
car.shape('car1.gif')
car.up()
car.goto(0,-150)


rock = turtle.Turtle()
rock.shape('rock1.gif')
rock.up()
rock.state = 'ready'
rock.goto(1000,1000)


def animate_car():
    global car_index, counter
    counter += 1
    
    if counter%20 == 0:
        car.shape(car_list[car_index])
        car_index += 1
        if car_index == 3:
            car_index = 0
            
    
def car_right():
    if car.xcor()<220:
        car.goto(car.xcor()+30, car.ycor())


def car_left():
    if car.xcor()>-220:
        car.goto(car.xcor()-30, car.ycor())


def animate_rock():
    if rock.state == 'road':

       
            
        rock.goto(rock.xcor()+rock.dx, rock.ycor()+rock.dy)

        if rock.ycor()<0:
            rock.shape('rock2.gif')
        if rock.ycor()<-50:
            rock.shape('rock3.gif')
        if rock.ycor()<-100:
            rock.shape('rock4.gif')
        
            
        if rock.ycor() <= -200:
            rock.goto(1000,1000)
            rock.state = 'ready'

        

win.onkey(car_right, 'Right')
win.onkey(car_left, 'Left')

rock_start = [-30, 0, 30]

while True:
    win.update()
    animate_background()
    animate_car()

    time.sleep(0.01)

    delay = random.random()
    if delay <0.05 and rock.state == 'ready':
        rock = turtle.Turtle()
        rock.up()
        rock.shape('rock1.gif')
        rock.state = 'road'
        rock.goto(random.choice(rock_start), 70)
        rock.dy = -3
        
        if rock.xcor()<0:
            rock.dx = -1
        elif rock.xcor() == 0:
            rock.dx = 0
        elif rock.xcor() >0:
            rock.dx = 1
        
        
        
    if rock.state == 'road':
        animate_rock()

    # Game over
    if -170 >= rock.ycor() >= -195 and rock.distance(car)<150:
        car.goto(0,0)
        car.s = 'crash1.gif'
        car.shape(car.s)
        win.update()
        break

print('game over')
counter = 0

while True:
    counter += 1
    if car.s == 'crash1.gif' and counter%20 == 0:
        car.s = 'crash2.gif'
        car.shape(car.s)
    elif car.s == 'crash2.gif' and counter%20 == 0:
        car.s = 'crash1.gif'
        car.shape(car.s)
    win.update()
    time.sleep(0.01)





    
        
        
