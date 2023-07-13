from concrete_commands import *
from robot_controller import RobotController
from robot import Robot


if __name__ == '__main__':
    right = MoveRight()
    left = MoveLeft()
    backward = MoveBackward()
    forward = MoveForward()

    list = {1: right, 2: left, 3: forward, 4: backward, 0: 'undo'}
    controller = RobotController(Robot(name='Robot-01'))

    controller.setCommand(right)
    controller.setCommand(left)
    controller.setCommand(backward)
    controller.setCommand(forward)

    print('{right -> 1, left -> 2, forward -> 3, backward -> 4, undo -> 0} or any-to-exit')

    while True:
        i = int(input('enter command: '))
        try:
            if i in list.keys():
                if i == 0:
                    controller.undoCommand()
                else:
                    controller.runCommand(list[i])
            else:
                break
        except:
            break
