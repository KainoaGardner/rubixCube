from display import *
from rubixCube import *
from buttons import *
def main():
    run = True
    while run:
        mos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if cube.shuffling == False:
                        if FButton.checkClicked(mos):
                            cube.fTurn()
                            cube.history.append("F")
                        elif FRButton.checkClicked(mos):
                            cube.frTurn()
                            cube.history.append("FR")

                        elif BButton.checkClicked(mos):
                            cube.bTurn()
                            cube.history.append("B")
                        elif BRButton.checkClicked(mos):
                            cube.brTurn()
                            cube.history.append("BR")

                        elif LButton.checkClicked(mos):
                            cube.lTurn()
                            cube.history.append("L")
                        elif LRButton.checkClicked(mos):
                            cube.lrTurn()
                            cube.history.append("LR")

                        elif RButton.checkClicked(mos):
                            cube.rTurn()
                            cube.history.append("R")
                        elif RRButton.checkClicked(mos):
                            cube.rrTurn()
                            cube.history.append("RR")

                        elif UButton.checkClicked(mos):
                            cube.uTurn()
                            cube.history.append("U")
                        elif URButton.checkClicked(mos):
                            cube.urTurn()
                            cube.history.append("UR")

                        elif DButton.checkClicked(mos):
                            cube.dTurn()
                            cube.history.append("D")
                        elif DRButton.checkClicked(mos):
                            cube.drTurn()
                            cube.history.append("DR")

                        elif undoButton.checkClicked(mos):
                            cube.undo()
                        elif resetButton.checkClicked(mos):
                            cube.reset()
                        elif mixButton.checkClicked(mos):
                            cube.shuffling = True
                        elif solveButton.checkClicked(mos):
                            cube.solve()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    cube.undo()

        display()
        if cube.shuffling == False:
            if FButton.checkClicked(mos):
                spinImageRect = spinImage.get_rect(center = (MARGINSIZE + TILESIZE * 3 + TILESIZE * 1.5,MARGINSIZE + TILESIZE * 3 + TILESIZE * 1.5))
                screen.blit(spinImage,spinImageRect)
            elif FRButton.checkClicked(mos):
                spinImageRect = spinImage.get_rect(center=(MARGINSIZE + TILESIZE * 3 + TILESIZE * 1.5, MARGINSIZE + TILESIZE * 3 + TILESIZE * 1.5))
                screen.blit(spinFlipImage,spinImageRect)

            elif BButton.checkClicked(mos):
                spinImageRect = spinImage.get_rect(center=(MARGINSIZE + TILESIZE * 9 + TILESIZE * 1.5, MARGINSIZE + TILESIZE * 3 + TILESIZE * 1.5))
                screen.blit(spinImage,spinImageRect)
            elif BRButton.checkClicked(mos):
                spinImageRect = spinImage.get_rect(center=(MARGINSIZE + TILESIZE * 9 + TILESIZE * 1.5, MARGINSIZE + TILESIZE * 3 + TILESIZE * 1.5))
                screen.blit(spinFlipImage,spinImageRect)

            elif LButton.checkClicked(mos):
                spinImageRect = spinImage.get_rect(center=(MARGINSIZE + TILESIZE * 1.5, MARGINSIZE + TILESIZE * 3 + TILESIZE * 1.5))
                screen.blit(spinImage,spinImageRect)
            elif LRButton.checkClicked(mos):
                spinImageRect = spinImage.get_rect(center=(MARGINSIZE + TILESIZE * 1.5, MARGINSIZE + TILESIZE * 3 + TILESIZE * 1.5))
                screen.blit(spinFlipImage,spinImageRect)

            elif RButton.checkClicked(mos):
                spinImageRect = spinImage.get_rect(center=(MARGINSIZE + TILESIZE * 6 + TILESIZE * 1.5, MARGINSIZE + TILESIZE * 3 + TILESIZE * 1.5))
                screen.blit(spinImage,spinImageRect)
            elif RRButton.checkClicked(mos):
                spinImageRect = spinImage.get_rect(center=(MARGINSIZE + TILESIZE * 6 + TILESIZE * 1.5, MARGINSIZE + TILESIZE * 3 + TILESIZE * 1.5))
                screen.blit(spinFlipImage,spinImageRect)

            elif UButton.checkClicked(mos):
                spinImageRect = spinImage.get_rect(center=(MARGINSIZE + TILESIZE * 3 + TILESIZE * 1.5, MARGINSIZE + TILESIZE * 1.5))
                screen.blit(spinImage,spinImageRect)
            elif URButton.checkClicked(mos):
                spinImageRect = spinImage.get_rect(center=(MARGINSIZE + TILESIZE * 3 + TILESIZE * 1.5, MARGINSIZE + TILESIZE * 1.5))
                screen.blit(spinFlipImage,spinImageRect)

            elif DButton.checkClicked(mos):
                spinImageRect = spinImage.get_rect(center=(MARGINSIZE + TILESIZE * 3 + TILESIZE * 1.5, MARGINSIZE + TILESIZE * 6 + TILESIZE * 1.5))
                screen.blit(spinImage,spinImageRect)
            elif DRButton.checkClicked(mos):
                spinImageRect = spinImage.get_rect(center=(MARGINSIZE + TILESIZE * 3 + TILESIZE * 1.5, MARGINSIZE + TILESIZE * 6 + TILESIZE * 1.5))
                screen.blit(spinFlipImage,spinImageRect)


        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

main()