from settings import *
class Button(pygame.sprite.Sprite):
    def __init__(self,text,x,y,color,size):
        self.x = x
        self.y = y
        self.size = size
        self.text = font.render(text,True,color)
        self.textRect = self.text.get_rect(center =(x + self.size[0] // 2,y + self.size[1]//2))



    def drawButton(self):
        pygame.draw.rect(screen,"#bdc3c7",pygame.Rect(self.x,self.y,self.size[0],self.size[1]))
        for i in range(2):
            pygame.draw.line(screen,BLACK,(self.x,self.y + i * self.size[1]),(self.x + self.size[0],self.y + i * self.size[1]),10)
            pygame.draw.line(screen, BLACK, (self.x + i * self.size[0], self.y), (self.x + i * self.size[0], self.y + self.size[1]),10)
        screen.blit(self.text,self.textRect)

    def checkClicked(self,pos):
        if self.x <= pos[0] < self.x + self.size[0] and self.y <= pos[1] < self.y + self.size[1]:
            return True
        else:
            return False




FButton = Button("F",MARGINSIZE + TILESIZE * 6,MARGINSIZE + TILESIZE * 6,WHITE,(TILESIZE,TILESIZE))
FRButton = Button("F'",MARGINSIZE + TILESIZE * 6,MARGINSIZE + TILESIZE * 7,WHITE,(TILESIZE,TILESIZE))
BButton = Button("B",MARGINSIZE + TILESIZE * 7,MARGINSIZE + TILESIZE * 6,WHITE,(TILESIZE,TILESIZE))
BRButton = Button("B'",MARGINSIZE + TILESIZE * 7,MARGINSIZE + TILESIZE * 7,WHITE,(TILESIZE,TILESIZE))
LButton = Button("L",MARGINSIZE + TILESIZE * 8,MARGINSIZE + TILESIZE * 6,WHITE,(TILESIZE,TILESIZE))
LRButton = Button("L'",MARGINSIZE + TILESIZE * 8,MARGINSIZE + TILESIZE * 7,WHITE,(TILESIZE,TILESIZE))
RButton = Button("R",MARGINSIZE + TILESIZE * 9,MARGINSIZE + TILESIZE * 6,WHITE,(TILESIZE,TILESIZE))
RRButton = Button("R'",MARGINSIZE + TILESIZE * 9,MARGINSIZE + TILESIZE * 7,WHITE,(TILESIZE,TILESIZE))
UButton = Button("U",MARGINSIZE + TILESIZE * 10,MARGINSIZE + TILESIZE * 6,WHITE,(TILESIZE,TILESIZE))
URButton = Button("U'",MARGINSIZE + TILESIZE * 10,MARGINSIZE + TILESIZE * 7,WHITE,(TILESIZE,TILESIZE))
DButton = Button("D",MARGINSIZE + TILESIZE * 11,MARGINSIZE + TILESIZE * 6,WHITE,(TILESIZE,TILESIZE))
DRButton = Button("D'",MARGINSIZE + TILESIZE *11,MARGINSIZE + TILESIZE * 7,WHITE,(TILESIZE,TILESIZE))

resetButton = Button("Reset",MARGINSIZE + TILESIZE * 6,MARGINSIZE + TILESIZE * 8,WHITE,(TILESIZE * 2,TILESIZE))
mixButton = Button("Mix",MARGINSIZE + TILESIZE * 8,MARGINSIZE + TILESIZE * 8,WHITE,(TILESIZE * 2,TILESIZE))
solveButton = Button("Solve",MARGINSIZE + TILESIZE * 10,MARGINSIZE + TILESIZE * 8,WHITE,(TILESIZE * 2,TILESIZE))


buttonGroup = [FButton,FRButton,BButton,BRButton,LButton,LRButton,RButton,RRButton,UButton,URButton,DButton,DRButton,resetButton,mixButton,solveButton]