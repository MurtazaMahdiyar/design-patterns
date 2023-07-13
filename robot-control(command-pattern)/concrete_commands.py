from iCommand import ICommand
from robot import Robot


class MoveRight(ICommand):

    def execute(self, robot: Robot):
        if isinstance(robot, Robot):
            print(f"{robot.id} ({robot.name}) : moving-right")

    def unexecute(self, robot: Robot):
        if isinstance(robot, Robot):
            print(f"{robot.id} ({robot.name}) : moving-left")


class MoveLeft(ICommand):

    def execute(self, robot: Robot):
        if isinstance(robot, Robot):
            print(f"{robot.id} ({robot.name}) : moving-left")

    def unexecute(self, robot: Robot):
        if isinstance(robot, Robot):
            print(f"{robot.id} ({robot.name}) : moving-right")


class MoveForward(ICommand):

    def execute(self, robot: Robot):
        if isinstance(robot, Robot):
            print(f"{robot.id} ({robot.name}) : moving-forward")

    def unexecute(self, robot: Robot):
        if isinstance(robot, Robot):
            print(f"{robot.id} ({robot.name}) : moving-backward")


class MoveBackward(ICommand):

    def execute(self, robot: Robot):
        if isinstance(robot, Robot):
            print(f"{robot.id} ({robot.name}) : moving-backward")

    def unexecute(self, robot: Robot):
        if isinstance(robot, Robot):
            print(f"{robot.id} ({robot.name}) : moving-forward")
