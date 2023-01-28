import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import background
import player

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

# Initialisation de l'arrière plan
game_background = background.Background(screen)

# Initialisation du joueur
game_player = player.Player()

# Booléen indiquant si le jeu est en cours
game_running: bool = True

# Boucle du jeu
while game_running:
    # Afficher l'arrière plan
    game_background.draw(screen)

    # Mettre à jour l'arrière plan
    game_background.update()

    # Afficher le joueur
    game_player.draw(screen)

    # Mettre à jour le joueur
    game_player.update()

    # Mettre à jour l'écran
    pygame.display.flip()

    # Pour chaque évènement
    for event in pygame.event.get():

        # Si l'évènement est la fermeture de la fenêtre
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()

    # Fixer le nombre de FPS
    clock.tick(FPS)
