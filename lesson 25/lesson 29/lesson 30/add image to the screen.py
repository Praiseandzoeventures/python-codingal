import pygame
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT=500,500

display_surface= pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Add Image and background image")

background__image= pygame.transform.scale(pygame.image.load("lesson 25/lesson 29/lesson 30/images/background.jpg").convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

penguin_image=pygame.transform.scale( pygame.image.load("lesson 25/lesson 29/lesson 30/images/penguin.png").convert_alpha(),(200,200))

pygame__rect= penguin_image.get_rect(center=(SCREEN_WIDTH //2,SCREEN_HEIGHT //2-30))

text=pygame.font.Font(None, 36).render("Hello world", True, pygame.Color("pink"))

text_rect= text.get_rect(center=(SCREEN_WIDTH //2+110))

def game_loop():
    clock=pygame.time.Clock()
    running = True
while running :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display_surface.blit(background__image, (0,0))
        display_surface.blit(penguin_image, pygame__rect)
        display_surface.blit(text, text_rect)

        pygame.display.update()
        
pygame.quit()