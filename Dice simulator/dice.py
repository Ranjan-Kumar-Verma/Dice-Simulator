import random
import pygame
pygame.font.init()

# CONSTANTS
WIDTH, HEIGHT = 500, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
IMG_WIDTH, IMG_HEIGHT = 150, 150
TITLE_FONT = pygame.font.SysFont("comicsans", 30)
BUTTON_FONT = pygame.font.SysFont("comicsans", 25)

#Images
DICE_IMG = pygame.transform.scale(pygame.image.load("dice-shield.png"), (IMG_WIDTH, IMG_HEIGHT))


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Disc Simulator")

def roll_dice():
    global DICE_IMG
    image_list = ["dice-one.png", "dice-two.png", "dice-three.png", "dice-four.png", "dice-five.png", "dice-six.png"]

    DICE_IMG = pygame.transform.scale(pygame.image.load(random.choice(image_list)), (IMG_WIDTH, IMG_HEIGHT))
    WIN.blit(DICE_IMG, (WIDTH//2-IMG_WIDTH//2, HEIGHT//2 - IMG_HEIGHT//2))
    pygame.display.update()
    # DICE_IMG = pygame.image.load(random.choices(image_list, k = 1))



def draw_window(button):
    WIN.fill(WHITE)
    WIN.blit(DICE_IMG, (WIDTH//2-IMG_WIDTH//2, HEIGHT//2 - IMG_HEIGHT//2))

    title = TITLE_FONT.render(" Welcome to Dice Simulator ", 1, BLACK)
    WIN.blit(title, (WIDTH//2 - title.get_width()//2, 25))

    btn_text = BUTTON_FONT.render(" ROLL ", 1, BLACK)
    WIN.blit(btn_text, (button.x + button.width//2 - btn_text.get_width()//2, button.y + 6))
    pygame.draw.rect(WIN, BLACK, button, 3)
    pygame.display.update()
    # print(title.get_width())

def main():
    button = pygame.Rect(WIDTH//2 - IMG_WIDTH//4-10, 70, IMG_WIDTH//2+20, 30 )
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed() and button.collidepoint(mouse):
                    roll_dice()


        draw_window(button)

if __name__ == "__main__":
    main()
