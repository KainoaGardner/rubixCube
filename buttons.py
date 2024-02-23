from settings import *
class Button(pygame.sprite.Sprite):
    def __init__(self,text,x,y,color,size,fontType):
        self.x = x
        self.y = y
        self.size = size
        self.text = fontType.render(text,True,color)
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




FButton = Button("F",MARGINSIZE + TILESIZE * 6,MARGINSIZE + TILESIZE * 6,WHITE,(TILESIZE,TILESIZE),font)
FRButton = Button("F'",MARGINSIZE + TILESIZE * 6,MARGINSIZE + TILESIZE * 7,WHITE,(TILESIZE,TILESIZE),font)
BButton = Button("B",MARGINSIZE + TILESIZE * 7,MARGINSIZE + TILESIZE * 6,WHITE,(TILESIZE,TILESIZE),font)
BRButton = Button("B'",MARGINSIZE + TILESIZE * 7,MARGINSIZE + TILESIZE * 7,WHITE,(TILESIZE,TILESIZE),font)
LButton = Button("L",MARGINSIZE + TILESIZE * 8,MARGINSIZE + TILESIZE * 6,WHITE,(TILESIZE,TILESIZE),font)
LRButton = Button("L'",MARGINSIZE + TILESIZE * 8,MARGINSIZE + TILESIZE * 7,WHITE,(TILESIZE,TILESIZE),font)
RButton = Button("R",MARGINSIZE + TILESIZE * 9,MARGINSIZE + TILESIZE * 6,WHITE,(TILESIZE,TILESIZE),font)
RRButton = Button("R'",MARGINSIZE + TILESIZE * 9,MARGINSIZE + TILESIZE * 7,WHITE,(TILESIZE,TILESIZE),font)
UButton = Button("U",MARGINSIZE + TILESIZE * 10,MARGINSIZE + TILESIZE * 6,WHITE,(TILESIZE,TILESIZE),font)
URButton = Button("U'",MARGINSIZE + TILESIZE * 10,MARGINSIZE + TILESIZE * 7,WHITE,(TILESIZE,TILESIZE),font)
DButton = Button("D",MARGINSIZE + TILESIZE * 11,MARGINSIZE + TILESIZE * 6,WHITE,(TILESIZE,TILESIZE),font)
DRButton = Button("D'",MARGINSIZE + TILESIZE *11,MARGINSIZE + TILESIZE * 7,WHITE,(TILESIZE,TILESIZE),font)

resetButton = Button("Reset",MARGINSIZE + TILESIZE * 7,MARGINSIZE + TILESIZE * 8,WHITE,(TILESIZE,TILESIZE),fontSmall)
undoButton = Button("Undo",MARGINSIZE + TILESIZE * 6,MARGINSIZE + TILESIZE * 8,WHITE,(TILESIZE,TILESIZE),fontSmall)
mixButton = Button("Mix",MARGINSIZE + TILESIZE * 8,MARGINSIZE + TILESIZE * 8,WHITE,(TILESIZE * 2,TILESIZE),font)
solveButton = Button("Solve",MARGINSIZE + TILESIZE * 10,MARGINSIZE + TILESIZE * 8,WHITE,(TILESIZE * 2,TILESIZE),font)


buttonGroup = [FButton,FRButton,BButton,BRButton,LButton,LRButton,RButton,RRButton,UButton,URButton,DButton,DRButton,resetButton,undoButton,mixButton,solveButton]