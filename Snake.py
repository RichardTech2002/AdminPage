import pygame
import Snake.py
def main_menu():
     while True:
 
        WIN.fill((0,0,0))
        writetext("Nibbles Reboot", 215, 60, (153, 0, 153), 48)
 
        mx, my = pygame.mouse.get_pos()
 
        button_1 = pygame.Rect(275, 200, 200, 50)
        
        button_2 = pygame.Rect(275, 300, 200, 50)
        if button_1.collidepoint((mx, my)):
            if click:
                exefile = sanke.py
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        pygame.draw.rect(WIN, (255, 0, 0), button_1)
        writetext('Play Game', 300, 205, (200, 200, 0), 30)
        pygame.draw.rect(WIN, (255, 0, 0), button_2)
        writetext('options', 310, 305, (200, 200, 0), 36)
 
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        CLOCK.tick(60) 
