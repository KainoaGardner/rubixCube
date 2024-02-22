from settings import *
import random
class RubixCube():
    def __init__(self):
        self.colorDict = {0:"#2ecc71",1:"#f1c40f",2:"#e67e22",3:"#e74c3c",4:"#ecf0f1",5:"#3498db"}
        self.facePos = {0:(1,1),1:(3,1),2:(0,1),3:(2,1),4:(1,0),5:(1,2)}
        self.front = [[0,0,0],[0,0,0],[0,0,0]]
        self.back = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.left = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        self.right = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
        self.top = [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
        self.bot = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
        self.history = []
        self.clickStart = ()

    def drawFace(self,face,x,y):
        for r,row in enumerate(face):
            for c in range(len(row)):
                pygame.draw.rect(screen,self.colorDict.get(face[r][c]),pygame.Rect(MARGINSIZE + x * (TILESIZE * 3) + c * TILESIZE,MARGINSIZE + y * (TILESIZE * 3) + r * TILESIZE,TILESIZE,TILESIZE))

        for i in range(4):
            if i % 3 == 0:
                pygame.draw.line(screen,BLACK,(MARGINSIZE + x * (TILESIZE * 3) + i * TILESIZE,MARGINSIZE + y * (TILESIZE * 3)),(MARGINSIZE + x * (TILESIZE * 3) + i * TILESIZE, MARGINSIZE + y * (TILESIZE * 3) + TILESIZE * 3),10)
                pygame.draw.line(screen, BLACK,(MARGINSIZE + x * (TILESIZE * 3), MARGINSIZE + y * (TILESIZE * 3) + i * TILESIZE), (MARGINSIZE + x * (TILESIZE * 3) + TILESIZE * 3, MARGINSIZE + y * (TILESIZE * 3) + i * TILESIZE), 10)
            else:
                pygame.draw.line(screen, BLACK, (MARGINSIZE + x * (TILESIZE * 3) + i * TILESIZE, MARGINSIZE + y * (TILESIZE * 3)), (MARGINSIZE + x * (TILESIZE * 3) + i * TILESIZE,MARGINSIZE + y * (TILESIZE * 3) + TILESIZE * 3), 4)
                pygame.draw.line(screen, BLACK,(MARGINSIZE + x * (TILESIZE * 3), MARGINSIZE + y * (TILESIZE * 3) + i * TILESIZE), (MARGINSIZE + x * (TILESIZE * 3) + TILESIZE * 3,MARGINSIZE + y * (TILESIZE * 3) + i * TILESIZE), 4)
    def drawCube(self):
        for f,face in enumerate([self.front,self.back,self.left,self.right,self.top,self.bot]):
            x = self.facePos.get(f)[0]
            y = self.facePos.get(f)[1]
            self.drawFace(face,x,y)

    def drawLine(self):
        if self.clickStart != ():
            mos = pygame.mouse.get_pos()
            xPos = (mos[0] - MARGINSIZE) // TILESIZE
            yPos = (mos[1] - MARGINSIZE) // TILESIZE
            if abs(self.clickStart[0] - xPos) >= 1:
                pygame.draw.line(screen,"black",(MARGINSIZE + self.clickStart[0] * TILESIZE + TILESIZE // 2,MARGINSIZE + self.clickStart[1] * TILESIZE + TILESIZE // 2),(mos[0],MARGINSIZE + self.clickStart[1] * TILESIZE + TILESIZE // 2),10)
            elif abs(self.clickStart[1] - yPos) >= 1:
                pygame.draw.line(screen,"black",(MARGINSIZE + self.clickStart[0] * TILESIZE + TILESIZE // 2,MARGINSIZE + self.clickStart[1] * TILESIZE + TILESIZE // 2),(MARGINSIZE + self.clickStart[0] * TILESIZE + TILESIZE // 2,mos[1]),10)

    def reset(self):
        self.history = []
        self.front = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.back = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.left = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        self.right = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
        self.top = [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
        self.bot = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]

    def shuffle(self):
        pass

    def solve(self):
        pass

    def fTurn(self):
        pass

    def frTurn(self):
        pass

    def bTurn(self):
        pass

    def brTurn(self):
        pass

    def lTurn(self):
        pass

    def lrTurn(self):
        pass

    def rTurn(self):
        pass

    def rrTurn(self):
        pass

    def uTurn(self):
        pass

    def urTurn(self):
        pass

    def dTurn(self):
        pass

    def drTurn(self):
        pass

    def undo(self):
        if len(self.history) > 0:
            cube = self.history[-1]
            self.front = cube[0]
            self.back = cube[1]
            self.left = cube[2]
            self.right = cube[3]
            self.top = cube[4]
            self.bot = cube[5]

            self.history.pop(-1)

    def makeHistory(self):
        cube = []
        for face in [self.front,self.back,self.left,self.right,self.top,self.bot]:
            faceSide = []
            for r in range(3):
                row = []
                for c in range(3):
                    row.append(face[r][c])
                faceSide.append(row)
            cube.append(faceSide)
        self.history.append(cube)

    def display(self):
        self.drawCube()
        self.drawLine()
        # self.displayLines()

cube = RubixCube()
