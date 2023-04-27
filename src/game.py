from wastes.wastes_generator import WastesGenerator
import player
from background.background import Background
from obstacle.obstacles_generator import ObstaclesGenerator
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

# Initialisation du générateur d'obstacles
obstacles_generator = ObstaclesGenerator(SCREEN_HEIGHT)

# Booléen indiquant si le joueur a perdu
game_loosed: bool = True

# Raison de la perte
loose_reason: str = ""

# Chargement du bouton pour quitter le jeu dans 
quit_button = pygame.image.load("assets/buttons/quit.PNG").convert_alpha()

# Diminuer la taille du bouton pour quitter le jeu à max 120px de largeur et 120px de hauteur (garder le ratio)
quit_button = pygame.transform.smoothscale(quit_button, (120, int(quit_button.get_height() * 120 / quit_button.get_width()))).convert_alpha()

# Chargement du bouton pour lancer le jeu
play_button = pygame.image.load("assets/buttons/play.PNG").convert_alpha()

# Diminuer la taille du bouton pour lancer le jeu à max 300px de largeur et 300px de hauteur (garder le ratio)
play_button = pygame.transform.smoothscale(play_button, (300, int(play_button.get_height() * 300 / play_button.get_width()))).convert_alpha()

def outside_screen_callback() -> None:
    """
    Fonction de callback appelée lorsque le déchet sort de l'écran
    """
    global score, game_loosed, loose_reason
    score -= 5
    if score <= -50:
        game_loosed = True
        loose_reason = "Vous avez perdu car votre score était de -50 !"

# Boucle du jeu
while game_running:
    # Afficher l'arrière plan
    game_background.update(screen, player_speed)

    if not game_loosed:

        # Afficher le joueur
        game_player.draw(screen)

        # Mettre à jour les déchets
        wastes_generator.update(screen, player_speed, obstacles_generator.is_ground_available(SCREEN_WIDTH), outside_screen_callback)

        # Mettre à jour les obstacles
        obstacles_generator.update(screen, player_speed)

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
            score += 7

        # Gestion des collisions entre le joueur et les obstacles
        collided_obstacle: list[pygame.sprite.Sprite] = pygame.sprite.spritecollide(game_player, obstacles_generator.obstacles_group, False, pygame.sprite.collide_mask)
        if collided_obstacle != []:
            game_loosed = True
            loose_reason = "Vous avez perdu car vous avez touché un obstacle !"

        # Afficher le score
        score_text = pygame.font.Font(None, 50).render(
            f"Score : {int(score)}", True, (255, 255, 255))
        screen.blit(score_text, (SCREEN_WIDTH - 200, 50))
    else:
        # Afficher le message de défaite
        loose_text = pygame.font.Font(None, 100).render(loose_reason, True, (255, 255, 255))
        screen.blit(loose_text, (SCREEN_WIDTH / 2 - loose_text.get_width() / 2, SCREEN_HEIGHT / 2 - loose_text.get_height() / 2))

        # Afficher le bouton pour rejouer en dessous du message de défaite ou au milieu s'il n'y a pas de message de défaite
        if loose_reason != "":
            play_button_pos = (SCREEN_WIDTH / 2 - play_button.get_width() / 2, SCREEN_HEIGHT / 2 + loose_text.get_height() / 2 + 50)
        else:
            play_button_pos = (SCREEN_WIDTH / 2 - play_button.get_width() / 2, SCREEN_HEIGHT / 2 - play_button.get_height() / 2)
        screen.blit(play_button, play_button_pos)

        # Afficher le score si le joueur a perdu
        if loose_reason != "":
            score_text = pygame.font.Font(None, 50).render(
                f"Score : {int(score)}", True, (255, 255, 255))
            screen.blit(score_text, (SCREEN_WIDTH / 2 - score_text.get_width() / 2, SCREEN_HEIGHT / 2 - score_text.get_height() / 2 - 50))

    # Afficher le bouton pour quitter le jeu en haut à gauche avec une marge de 10px
    screen.blit(quit_button, (10, 10))

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

        # Si l'évènement est un clic de souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Si le clic est sur le bouton pour quitter le jeu
            if event.pos[0] >= 10 and event.pos[0] <= 10 + quit_button.get_width() and event.pos[1] >= 10 and event.pos[1] <= 10 + quit_button.get_height():
                game_running = False
                pygame.quit()
            # Si le clic est sur le bouton pour lancer le jeu
            elif event.pos[0] >= play_button_pos[0] and event.pos[0] <= play_button_pos[0] + play_button.get_width() and event.pos[1] >= play_button_pos[1] and event.pos[1] <= play_button_pos[1] + play_button.get_height():
                game_loosed = False
                score = 0
                game_player = player.Player(SCREEN_HEIGHT)
                wastes_generator = WastesGenerator(SCREEN_HEIGHT)
                obstacles_generator = ObstaclesGenerator(SCREEN_HEIGHT)
                collided_wastes = []
                loose_reason = ""
                player_speed = 10

    # Fixer le nombre de FPS
    clock.tick(FPS)
