import pygame

pygame.init()
screen=pygame.display.set_mode((400, 300))
done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True

    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))
    
    pygame.display.flip()
    
text=pygame.font.Font(None, 36).render("Hello world", True, pygame.Color("pink"))

text_rect= text.get_rect(center=(SCREEN_WIDTH //2+110))

def game_loop(): 
    clock=pygame.time.Clock()
    running = True
    while running :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(text, text_rect)

        pygame.display.update() 