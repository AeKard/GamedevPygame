import pygame, sys
from setting import *

pygame.init()
clock = pygame.time.Clock()
# Main SCREEN
SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

#SCREEN CONTROL
ctr_login = True
# LOGIN SCREEN BackGround
# btn Image in login
exit_btn = pygame.image.load('Button/0_exit_btn.png').convert_alpha()
exit_scaled = pygame.transform.scale(exit_btn,(50,50))
exit_center_rect = exit_scaled.get_rect(center = (640,500))

login_btn = pygame.image.load('Button/1_login_btn.png').convert_alpha()
login_scaled = pygame.transform.scale(login_btn,(50,50))
login_center_rect = login_scaled.get_rect(center = (400, 450))

register_btn = pygame.image.load('Button/2_register_btn.png').convert_alpha()
register_scaled = pygame.transform.scale(register_btn,(50,50))
register_center_rect = register_scaled.get_rect(center = (900, 450))

button_pressed_exit = False
button_pressed_login = False
button_pressed_register = False
#GLOBAL FONT
base_font = pygame.font.Font('font/Pixeltype.ttf',50) # initialize the font fonttype, Fontsize
#FONT
login_surface = base_font.render('Login', False, 'black') # login AA color
login_rect = login_surface.get_rect(center = (SCREEN_WIDTH / 2,SCREEN_HEIGHT / 2 - 100))


#FONT USERINPUT
user_font = pygame.font.Font('font/Pixeltype.ttf',30) # initialize the font fonttype, Fontsize
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')

user_input = 'Username'
user_surface_rect = pygame.Rect(SCREEN_WIDTH/2 - 100,340,190,32)

pass_input = 'Password'
pass_surface_rect = pygame.Rect(SCREEN_WIDTH/2 - 100, 400,190,32)

user_active = False
pass_active = False

#BUTTON IS PRESSED?

# GAME LOOP
while True:
    # MAIN SCREEN
    SCREEN.fill('white')
    if ctr_login:
        # LOGIN SCREEN
        pygame.draw.rect(SCREEN, '#55CEFF', pygame.Rect(320,180,640,400),0,10)
        pygame.draw.rect(SCREEN, '#00ABF0', pygame.Rect(320,180,640,400),5,10)
        # Draw in login_surf
        #btn
        SCREEN.blit(exit_scaled, exit_center_rect)
        SCREEN.blit(login_scaled, login_center_rect)
        SCREEN.blit(register_scaled, register_center_rect)
        #login text
        SCREEN.blit(login_surface, login_rect)
        #Login Input text box
        pygame.draw.rect(SCREEN, 'blue',user_surface_rect,2)
        user_surface =  user_font.render(user_input,False,(255,250,250))
        SCREEN.blit(user_surface,(user_surface_rect.x + 5, user_surface_rect.y + 10))
        
        pygame.draw.rect(SCREEN, 'blue',pass_surface_rect,1,5)
        pass_surface =  user_font.render(pass_input,False,(255,250,250))
        SCREEN.blit(pass_surface,(pass_surface_rect.x + 5, pass_surface_rect.y + 10))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Login Interface user INPUTS
        if ctr_login:
            # Button Inputs
                
            # Typing Inputs
            if event.type == pygame.MOUSEBUTTONDOWN:
                if user_surface_rect.collidepoint(event.pos):
                    user_active = True
                else:
                    user_active = False
                if pass_surface_rect.collidepoint(event.pos):
                    pass_active = True
                else:
                    pass_active = False
            if event.type == pygame.KEYDOWN:
                if user_active == True:
                    if len(user_input) < 16:
                        if event.key == pygame.K_BACKSPACE:
                            user_input = user_input[:-1]
                        else:
                            user_input += event.unicode
                        print(user_input)
                if pass_active == True:
                    if len(pass_input) < 16:
                        if event.key == pygame.K_BACKSPACE:
                            pass_input = pass_input[:-1]
                        else:
                            pass_input += event.unicode


    dt = clock.tick(60)
    pygame.display.update()

