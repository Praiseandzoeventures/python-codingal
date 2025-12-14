import pygame

def main():
    pygame.init()
    screen__width, screen__height = 500, 500
    screen=pygame.display.set_mode((screen__width, screen__height))
    pygame.display.set_caption("Color Changing Sprite")
    colors={
        "red":pygame.Color ("red"),
        "green":pygame.Color("green"),
        "blue":pygame.Color ("blue"),
        "yellow":pygame.Color ("yellow"),
        "white":pygame.Color ("white")
    }
    current_color= colors["white"]
    
    x,y=30,30
    sprite_width, sprite_height=60,60
    
    clock=pygame.time.Clock()
    done=False
    while not done:
        for event in pygame.event.get():
           if event.type==pygame.QUIT:
                done=True
                
        pressed =pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:x-=3
        if pressed[pygame.K_r]:x+=3
        if pressed[pygame.K_UP]:y-=3
        if pressed[pygame.K_DOWN]:y+=3
        
        x=min(max(x,0), screen__width - sprite_width)
        y=min(max(y,0), screen__height - sprite_height)
        
        if x ==0:current_color= colors["blue"]
        elif x == screen__width - sprite_width:current_color= colors["red"]
        elif y ==0:current_color= colors["green"]
        elif y == screen__height - sprite_height:current_color= colors["yellow"]
        else:
            current_color= colors["green"]
        screen.fill((0,0,0))
        pygame.draw.rect(screen, current_color, pygame.Rect(x,y,sprite_width,sprite_height))
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
if __name__ == "__main__":
    main()