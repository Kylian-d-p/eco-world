from wastes_generator import WastesGenerator
import player
from background.background import Background
import pygame
import os
import time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

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
screen: pygame.Surface = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT), pygame.RESIZABLE)

# Dimensions de l'écran (peuvent être différents de WINDOW_WIDTH et WINDOW_HEIGHT)
SCREEN_WIDTH: int = screen.get_width()
SCREEN_HEIGHT: int = screen.get_height()

# Dictionnaire contenant les touches du clavier en clé et en valeur un booléen qui indique si elles sont pressées
key_pressed: dict = {}

# Initialisation de l'arrière plan
game_background = Background(SCREEN_WIDTH, SCREEN_HEIGHT)

# Initialisation du joueur
game_player = player.Player(SCREEN_HEIGHT)

# Booléen indiquant si le jeu est en cours
game_running: bool = True

# Entier indiquant la vitesse de déplacement du joueur
player_speed: int = 10

# Initialisation du générateur de déchets
wastes_generator = WastesGenerator(SCREEN_HEIGHT)

# Score du joueur
score: float = 0

# Liste des déchets qui sont déjà entrés en collision avec le joueur
collided_wastes: list[pygame.sprite.Sprite] = []

# Boucle du jeu
while game_running:
    # Afficher l'arrière plan
    game_background.draw(screen, player_speed)

    # Afficher le joueur
    game_player.draw(screen)

    # Mettre à jour les déchets
    wastes_generator.update(screen, player_speed)

    # Si le joueur saute
    if key_pressed.get(pygame.K_SPACE) == True:
        game_player.jump()

    # Mettre à jour le joueur
    if key_pressed.get(pygame.K_LEFT) == True:
        game_player.update(SCREEN_WIDTH, SCREEN_HEIGHT, 0)
    elif key_pressed.get(pygame.K_RIGHT) == True:
        game_player.update(SCREEN_WIDTH, SCREEN_HEIGHT, 1)
    else:
        game_player.update(SCREEN_WIDTH, SCREEN_HEIGHT)

    
    # Gestion des collisions entre le joueur et les déchets
    collided_waste: list[pygame.sprite.Sprite] = pygame.sprite.spritecollide(game_player, wastes_generator.wastes_group, False, pygame.sprite.collide_mask)
    if collided_waste != [] and collided_waste[0] not in collided_wastes:
        wastes_generator.collided(collided_waste[0])
        collided_wastes.append(collided_waste[0])
        score /= 1.5

    # On ajoute le score
    score += 0.1

    # Afficher le score
    score_text = pygame.font.Font(None, 50).render(
        f"Score : {int(score)}", True, (255, 255, 255))
    screen.blit(score_text, (SCREEN_WIDTH - 200, 50))

    # Mettre à jour l'écran
    pygame.display.flip()

    # Pour chaque évènement
    for event in pygame.event.get():
        # Si l'évènement est une touche pressée
        if event.type == pygame.KEYDOWN:
            # On indique dans notre dictionnaire que cette touche est pressée
            key_pressed[event.key] = True
        elif event.type == pygame.KEYUP:  # Si l'évènement est une touche relâchée
            key_pressed[event.key] = False

        # Si l'évènement est la fermeture de la fenêtre
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()

    # Fixer le nombre de FPS
    clock.tick(FPS)
