import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import background
import player
from wastes_generator import WastesGenerator

# Définition des constantes
GAME_NAME: str = "gameName"
WINDOW_WIDTH: int = 1920
WINDOW_HEIGHT: int = 1080
FPS: int = 30

# Initialisation de pygame
pygame.init()

# Clock pour les FPS
clock = pygame.time.Clock()

# Générer la fenêtre du jeu
pygame.display.set_caption(GAME_NAME)  # Changement du titre de la fenêtre

# Chargement de la taille de la fenêtre en plein écran
screen: pygame.Surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.FULLSCREEN)

# Dictionnaire contenant les touches du clavier en clé et en valeur un booléen qui indique si elles sont pressées
key_pressed: dict = {}

# Initialisation de l'arrière plan
game_background = background.Background(screen)

# Initialisation du joueur
game_player = player.Player()

# Booléen indiquant si le jeu est en cours
game_running: bool = True

wastes_generator = WastesGenerator()

# Dimensions de l'écran (peuvent être différents de WINDOW_WIDTH et WINDOW_HEIGHT)
SCREEN_WIDTH: int = screen.get_width()
SCREEN_HEIGHT: int = screen.get_height()

# Boucle du jeu
while game_running:
    # Afficher l'arrière plan
    game_background.draw(screen)

    # Mettre à jour l'arrière plan
    game_background.update()

    # Afficher le joueur
    game_player.draw(screen)

    # Mettre à jour les déchets
    wastes_generator.update(screen)

    # Mettre à jour le joueur
    if key_pressed.get(pygame.K_LEFT) == True:
        game_player.update(SCREEN_WIDTH, 0)
    elif key_pressed.get(pygame.K_RIGHT) == True:
        game_player.update(SCREEN_WIDTH, 1)
    else:
        game_player.update(screen_width=SCREEN_WIDTH)

    # Si le joueur saute
    if key_pressed.get(pygame.K_SPACE) == True:
        game_player.jump()

    # Mettre à jour l'écran
    pygame.display.flip()

    # Pour chaque évènement
    for event in pygame.event.get():
        # Si l'évènement est une touche pressée
        if event.type == pygame.KEYDOWN:
            # On indique dans notre dictionnaire que cette touche est pressée
            key_pressed[event.key] = True
        elif event.type == pygame.KEYUP: # Si l'évènement est une touche relâchée
            key_pressed[event.key] = False

        # Si l'évènement est la fermeture de la fenêtre
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()

    # Fixer le nombre de FPS
    clock.tick(FPS)
