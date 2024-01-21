import pygame
pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Votre Jeu")

background_image = pygame.image.load("/Users/mbm/Desktop/Guess-the-price-game/FigmaTry.png").convert()

screen.blit(background_image, (0, 0))

background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
font = pygame.font.Font(None, 36)  # You can choose the font and size
text = font.render("Your Text Here", True, (25, 255, 255))  # RGB color for text

# Get the rect object for the text surface
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Autres mises à jour de jeu ici

    # Afficher l'image de fond
    screen.blit(background_image, (0, 0))
    screen.blit(text, text_rect)
    # Mettre à jour l'affichage
    pygame.display.flip()

pygame.quit()
