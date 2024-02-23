from settings import *
import random
import time
class RubixCube():
    def __init__(self):
        self.colorDict = {0:"#2ecc71",1:"#f1c40f",2:"#e67e22",3:"#c0392b",4:"#ecf0f1",5:"#3498db"}
        self.facePos = {0:(1,1),1:(3,1),2:(0,1),3:(2,1),4:(1,0),5:(1,2)}
        self.front = [[0,0,0],[0,0,0],[0,0,0]]
        self.bot = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.left = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        self.right = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
        self.top = [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
        self.back = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
        self.history = []
        self.clickStart = ()

        self.timer = 0
        self.startTime = time.time()
        self.win = False

        self.shuffleCount = 0
        self.shuffling = False

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
        self.win = False
        self.front = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.bot = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        self.left = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        self.right = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]
        self.top = [[4, 4, 4], [4, 4, 4], [4, 4, 4]]
        self.back = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]

    def shuffleClicked(self):
        if self.shuffling:
            self.shuffleCount += 1
            if self.shuffleCount % 2 == 0:
                turn = random.randint(0,11)
                match turn:
                    case 0:
                        self.fTurn()
                    case 1:
                        self.frTurn()
                    case 2:
                        self.bTurn()
                    case 3:
                        self.brTurn()
                    case 4:
                        self.lTurn()
                    case 5:
                        self.lrTurn()
                    case 6:
                        self.rTurn()
                    case 7:
                        self.rrTurn()
                    case 8:
                        self.uTurn()
                    case 9:
                        self.urTurn()
                    case 10:
                        self.dTurn()
                    case 11:
                        self.drTurn()

        if self.shuffleCount == 100:
            self.shuffleCount = 0
            self.shuffling = False
            self.history = []
            self.win = False

            if self.front == [[0, 0, 0], [0, 0, 0], [0, 0, 0]] and self.bot == [[1, 1, 1], [1, 1, 1], [1, 1, 1]] and self.left == [[2, 2, 2], [2, 2, 2], [2, 2, 2]]\
                and self.right == [[3, 3, 3], [3, 3, 3], [3, 3, 3]] and self.top == [[4, 4, 4], [4, 4, 4], [4, 4, 4]] and self.back == [[5, 5, 5], [5, 5, 5], [5, 5, 5]]:
                self.shuffling = True

    def solve(self):
        self.getWhiteCross()

    def getWhiteCross(self):
        whitePieceLocation = []
        for face in [(self.front,"f"),(self.back,"b"),(self.left,"l"),(self.right,"r"),(self.top,"u")]:
            for pos in [(0,1),(1,0),(1,2),(2,1)]:
                if face[0][pos[0]][pos[1]] == 4:
                    whitePieceLocation.append((face[1],pos))

        print(whitePieceLocation)
        # if self.bot[0][1] != 4:
        #     if self.left[1][2] == 4:
        #        self.frTurn()
        #     elif self.right[1][0] == 4:
        #        self.fTurn()
        #     elif self.bot[2][1] == 4:
        #         self.fTurn()
        #         self.fTurn()

            # elif self.left[1][2] == 1:
            #     self.fTurn()
            # elif self.right[1][0] == 1:
            #     self.frTurn()




    def spinFace(self,face):
        face = [[face[2][0],face[1][0],face[0][0]],
                      [face[2][1],face[1][1],face[0][1]],
                      [face[2][2],face[1][2],face[0][2]]]
        return face
    def spinRFace(self,face):
        face = [[face[0][2], face[1][2], face[2][2]],
                      [face[0][1], face[1][1], face[2][1]],
                      [face[0][0], face[1][0], face[2][0]]]
        return face

    def fTurn(self):
        self.front = self.spinFace(self.front)

        temp = (self.top[2][0],self.top[2][1],self.top[2][2])
        self.top[2][0] = self.left[0][2]
        self.top[2][1] = self.left[1][2]
        self.top[2][2] = self.left[2][2]

        self.left[0][2] = self.bot[0][0]
        self.left[1][2] = self.bot[0][1]
        self.left[2][2] = self.bot[0][2]

        self.bot[0][0] = self.right[2][0]
        self.bot[0][1] = self.right[1][0]
        self.bot[0][2] = self.right[0][0]

        self.right[2][0] = temp[2]
        self.right[1][0] = temp[1]
        self.right[0][0] = temp[0]

    def frTurn(self):
        self.front = self.spinRFace(self.front)

        temp = (self.top[2][0],self.top[2][1],self.top[2][2])
        self.top[2][0] = self.right[0][0]
        self.top[2][1] = self.right[1][0]
        self.top[2][2] = self.right[2][0]

        self.right[2][0] = self.bot[0][0]
        self.right[1][0] = self.bot[0][1]
        self.right[0][0] = self.bot[0][2]

        self.bot[0][0] = self.left[0][2]
        self.bot[0][1] = self.left[1][2]
        self.bot[0][2] = self.left[2][2]

        self.left[0][2] = temp[2]
        self.left[1][2] = temp[1]
        self.left[2][2] = temp[0]

    def bTurn(self):
        self.back = self.spinFace(self.back)

        temp = (self.top[0][0],self.top[0][1],self.top[0][2])
        self.top[0][0] = self.right[0][2]
        self.top[0][1] = self.right[1][2]
        self.top[0][2] = self.right[2][2]

        self.right[0][2] = self.bot[2][2]
        self.right[1][2] = self.bot[2][1]
        self.right[2][2] = self.bot[2][0]

        self.bot[2][2] = self.left[2][0]
        self.bot[2][1] = self.left[1][0]
        self.bot[2][0] = self.left[0][0]

        self.left[2][0] = temp[0]
        self.left[1][0] = temp[1]
        self.left[0][0] = temp[2]

    def brTurn(self):
        self.back = self.spinRFace(self.back)

        temp = (self.top[0][0],self.top[0][1],self.top[0][2])
        self.top[0][0] = self.left[2][0]
        self.top[0][1] = self.left[1][0]
        self.top[0][2] = self.left[0][0]

        self.left[2][0] = self.bot[2][2]
        self.left[1][0] = self.bot[2][1]
        self.left[0][0] = self.bot[2][0]

        self.bot[2][2] = self.right[0][2]
        self.bot[2][1] = self.right[1][2]
        self.bot[2][0] = self.right[2][2]

        self.right[0][2] = temp[0]
        self.right[1][2] = temp[1]
        self.right[2][2] = temp[2]

    def lTurn(self):
        self.left = self.spinFace(self.left)

        temp = (self.front[0][0],self.front[1][0],self.front[2][0])
        self.front[0][0] = self.top[0][0]
        self.front[1][0] = self.top[1][0]
        self.front[2][0] = self.top[2][0]

        self.top[0][0] = self.back[2][2]
        self.top[1][0] = self.back[1][2]
        self.top[2][0] = self.back[0][2]

        self.back[2][2] = self.bot[0][0]
        self.back[1][2] = self.bot[1][0]
        self.back[0][2] = self.bot[2][0]

        self.bot[0][0] = temp[0]
        self.bot[1][0] = temp[1]
        self.bot[2][0] = temp[2]

    def lrTurn(self):
        self.left = self.spinRFace(self.left)

        temp = (self.front[0][0],self.front[1][0],self.front[2][0])
        self.front[0][0] = self.bot[0][0]
        self.front[1][0] = self.bot[1][0]
        self.front[2][0] = self.bot[2][0]

        self.bot[0][0] = self.back[2][2]
        self.bot[1][0] = self.back[1][2]
        self.bot[2][0] = self.back[0][2]

        self.back[2][2] = self.top[0][0]
        self.back[1][2] = self.top[1][0]
        self.back[0][2] = self.top[2][0]

        self.top[0][0] = temp[0]
        self.top[1][0] = temp[1]
        self.top[2][0] = temp[2]

    def rTurn(self):
        self.right = self.spinFace(self.right)

        temp = (self.front[0][2],self.front[1][2],self.front[2][2])
        self.front[0][2] = self.bot[0][2]
        self.front[1][2] = self.bot[1][2]
        self.front[2][2] = self.bot[2][2]

        self.bot[0][2] = self.back[2][0]
        self.bot[1][2] = self.back[1][0]
        self.bot[2][2] = self.back[0][0]

        self.back[2][0] = self.top[0][2]
        self.back[1][0] = self.top[1][2]
        self.back[0][0] = self.top[2][2]

        self.top[0][2] = temp[0]
        self.top[1][2] = temp[1]
        self.top[2][2] = temp[2]

    def rrTurn(self):
        self.right = self.spinRFace(self.right)

        temp = (self.front[0][2],self.front[1][2],self.front[2][2])
        self.front[0][2] = self.top[0][2]
        self.front[1][2] = self.top[1][2]
        self.front[2][2] = self.top[2][2]

        self.top[0][2] = self.back[2][0]
        self.top[1][2] = self.back[1][0]
        self.top[2][2] = self.back[0][0]

        self.back[2][0] = self.bot[0][2]
        self.back[1][0] = self.bot[1][2]
        self.back[0][0] = self.bot[2][2]

        self.bot[0][2] = temp[0]
        self.bot[1][2] = temp[1]
        self.bot[2][2] = temp[2]

    def uTurn(self):
        self.top = self.spinFace(self.top)

        temp = self.front[0]
        self.front[0] = self.right[0]
        self.right[0] = self.back[0]
        self.back[0] = self.left[0]
        self.left[0] = temp

    def urTurn(self):
        self.top = self.spinRFace(self.top)

        temp = self.front[0]
        self.front[0] = self.left[0]
        self.left[0] = self.back[0]
        self.back[0] = self.right[0]
        self.right[0] = temp

    def dTurn(self):
        self.bot = self.spinFace(self.bot)

        temp = self.front[2]
        self.front[2] = self.left[2]
        self.left[2] = self.back[2]
        self.back[2] = self.right[2]
        self.right[2] = temp


    def drTurn(self):
        self.bot = self.spinRFace(self.bot)

        temp = self.front[2]
        self.front[2] = self.right[2]
        self.right[2] = self.back[2]
        self.back[2] = self.left[2]
        self.left[2] = temp

    def undo(self):
        if len(self.history) > 0:
            move = self.history[-1]
            match move:
                case "F":
                    self.frTurn()
                case "FR":
                    self.fTurn()
                case "B":
                    self.brTurn()
                case "BR":
                    self.bTurn()
                case "L":
                    self.lrTurn()
                case "LR":
                    self.lTurn()
                case "R":
                    self.rrTurn()
                case "RR":
                    self.rTurn()
                case "U":
                    self.urTurn()
                case "UR":
                    self.uTurn()
                case "D":
                    self.drTurn()
                case "DR":
                    self.dTurn()

            self.history.pop(-1)
            self.win = False

    def getTime(self):
        if len(self.history) == 0 and self.win == False:
            self.timer = 00
        elif self.win == False:
            self.timer += 1

    def displayTime(self):
        text = fontBig.render(f"{self.timer//60}:{self.timer//6%10}", True, WHITE)
        textRect = text.get_rect(midleft=(MARGINSIZE + TILESIZE * 7, MARGINSIZE + TILESIZE + TILESIZE // 2))
        screen.blit(text,textRect)

    def getWin(self):
        if self.win == False:
            if self.front == [[0, 0, 0], [0, 0, 0], [0, 0, 0]] and self.bot == [[1, 1, 1], [1, 1, 1],[1, 1, 1]] and self.left == [[2, 2, 2],[2, 2, 2],[2, 2, 2]] \
                    and self.right == [[3, 3, 3], [3, 3, 3], [3, 3, 3]] and self.top == [[4, 4, 4], [4, 4, 4],[4, 4, 4]] and self.back == [[5, 5, 5], [5, 5, 5], [5, 5, 5]]:
                self.win = True

    def display(self):
        self.drawCube()
        self.drawLine()
        self.shuffleClicked()
        self.displayTime()
        self.getTime()
        # self.displayLines()

cube = RubixCube()
