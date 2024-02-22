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
                    if FButton.checkClicked(mos):
                        cube.fTurn()
                    elif FRButton.checkClicked(mos):
                        cube.frTurn()

                    elif BButton.checkClicked(mos):
                        cube.bTurn()
                    elif BRButton.checkClicked(mos):
                        cube.brTurn()

                    elif LButton.checkClicked(mos):
                        cube.lTurn()
                    elif LRButton.checkClicked(mos):
                        cube.lrTurn()

                    elif RButton.checkClicked(mos):
                        cube.rTurn()
                    elif RRButton.checkClicked(mos):
                        cube.rrTurn()

                    elif UButton.checkClicked(mos):
                        cube.uTurn()
                    elif URButton.checkClicked(mos):
                        cube.urTurn()

                    elif DButton.checkClicked(mos):
                        cube.dTurn()
                    elif DRButton.checkClicked(mos):
                        cube.drTurn()

                    elif resetButton.checkClicked(mos):
                        cube.reset()
                    elif mixButton.checkClicked(mos):
                        cube.shuffle()
                    elif solveButton.checkClicked(mos):
                        cube.solve()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    cube.undo()

        display()

        if FButton.checkClicked(mos):
            screen.blit(spinImage,(MARGINSIZE + TILESIZE * 3,MARGINSIZE + TILESIZE * 3))
        elif FRButton.checkClicked(mos):
            screen.blit(spinFlipImage,(MARGINSIZE + TILESIZE * 3,MARGINSIZE + TILESIZE * 3))

        elif BButton.checkClicked(mos):
            screen.blit(spinImage,(MARGINSIZE + TILESIZE * 9,MARGINSIZE + TILESIZE * 3))
        elif BRButton.checkClicked(mos):
            screen.blit(spinFlipImage,(MARGINSIZE + TILESIZE * 9,MARGINSIZE + TILESIZE * 3))

        elif LButton.checkClicked(mos):
            screen.blit(spinImage,(MARGINSIZE,MARGINSIZE + TILESIZE * 3))
        elif LRButton.checkClicked(mos):
            screen.blit(spinFlipImage,(MARGINSIZE,MARGINSIZE + TILESIZE * 3))

        elif RButton.checkClicked(mos):
            screen.blit(spinImage,(MARGINSIZE + TILESIZE * 6,MARGINSIZE + TILESIZE * 3))
        elif RRButton.checkClicked(mos):
            screen.blit(spinFlipImage,(MARGINSIZE + TILESIZE * 6,MARGINSIZE + TILESIZE * 3))

        elif UButton.checkClicked(mos):
            screen.blit(spinImage,(MARGINSIZE + TILESIZE * 3,MARGINSIZE))
        elif URButton.checkClicked(mos):
            screen.blit(spinFlipImage,(MARGINSIZE + TILESIZE * 3,MARGINSIZE))

        elif DButton.checkClicked(mos):
            screen.blit(spinImage,(MARGINSIZE + TILESIZE * 3,MARGINSIZE + TILESIZE * 6))
        elif DRButton.checkClicked(mos):
            screen.blit(spinFlipImage,(MARGINSIZE + TILESIZE * 3,MARGINSIZE + TILESIZE * 6))


        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()

main()