import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car=CarManager()
scoreboard= Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()
    if player.ycor() == 280:
       player.go_to_start()
       car.leve_up()
       scoreboard.increase_level()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            scoreboard.game_over()
            game_is_on=False

screen.exitonclick()





