import pygame

pygame.init()


width=600
height=600

screen = pygame.display.set_mode((width,height))

#COLORS
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


font = pygame.font.Font(None, 20)
#Large button
large_button = pygame.Rect(500,50,50,50)
large_button_text=font.render('Tall', True, BLACK)
large_button_rect = large_button_text.get_rect(center=(525, 75))
#Medium button
medium_button = pygame.Rect(500,125,50,50)
medium_button_text=font.render('Medium', True, BLACK)
medium_button_rect = medium_button_text.get_rect(center=(525,150))
#Small button
small_button = pygame.Rect(500,200,50,50)
small_button_text=font.render('Small', True, BLACK)
small_button_rect = small_button_text.get_rect(center=(525,225))



pilliar1=pygame.Rect(190,450,20,100)
pilliar2=pygame.Rect(390,450,20,100)
wall=pygame.Rect(190,450,20,100)



# size change
point1=450
point2=400

size={
    "Small":0,
    "Medium":-100,
    "Large":-200
}

nospam=1

running=True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        
    screen.fill(WHITE)
    if event.type == pygame.MOUSEBUTTONDOWN:
            if large_button.collidepoint(event.pos) and nospam==1:
                point1=450
                point2=400
                nospam=0
                point1+=size["Large"]
                point2+=size["Large"]
            elif not large_button.collidepoint(event.pos):
                nospam=1
            if medium_button.collidepoint(event.pos) and nospam==1:
                point1=450
                point2=400
                nospam=0
                point1+=size["Medium"]
                point2+=size["Medium"]
            elif not medium_button.collidepoint(event.pos):
                nospam=1
            if small_button.collidepoint(event.pos) and nospam==1:
                point1=450
                point2=400
                nospam=0
            elif not small_button_rect.collidepoint(event.pos):
                nospam=1
    pygame.draw.polygon(screen, GREEN, ((200,point2),(175,point1),(225,point1)))
    pygame.draw.polygon(screen, GREEN, ((400,point2),(375,point1),(425,point1)))
    pygame.draw.rect(screen,GREEN,(190,point1,20,400))
    pygame.draw.rect(screen,GREEN,(390,point1,20,400))
    pygame.draw.rect(screen,GREEN,(190,point1+30,200,400))
    pygame.draw.rect(screen,RED,small_button)
    pygame.draw.rect(screen,RED,medium_button)
    pygame.draw.rect(screen,RED,large_button)
    screen.blit(large_button_text, large_button_rect)
    screen.blit(medium_button_text, medium_button_rect)
    screen.blit(small_button_text, small_button_rect)
    pygame.display.update()




pygame.quit
