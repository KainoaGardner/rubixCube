from settings import *
from rubixCube import *
from buttons import *

def display():
    screen.fill("#95a5a6")
    for button in buttonGroup:
        button.drawButton()
    cube.display()

