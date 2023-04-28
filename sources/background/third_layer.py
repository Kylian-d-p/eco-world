import pygame


class ThirdLayer(pygame.sprite.Sprite):

    def __init__(self, surfaces: list[pygame.Surface], speed: int, pos: int) -> None:
        """
        Constructeur du 3ème layer du background
        surfaces: liste des surfaces du layer
        speed: vitesse de déplacement du layer
        pos: position x du layer
        """
        super().__init__() # Appel du constructeur de la classe Sprite
        # Redimensionne les images
        self.origin_images: list[pygame.Surface] = [pygame.transform.smoothscale(
            surfaces[x], (surfaces[x].get_width(), surfaces[x].get_height())).convert_alpha() for x in range(len(surfaces))]
        # Vérifie que toutes les images ont la même taille
        for x in range(len(self.origin_images)): # Pour chaque image
            if self.origin_images[x].get_width() != self.origin_images[0].get_width() or self.origin_images[x].get_height() != self.origin_images[0].get_height(): # Si l'image n'a pas la même taille que la première
                raise Exception("Toutes les images doivent avoir la même taille") # On lève une exception
        self.width: int = surfaces[0].get_width() # Largeur du layer
        self.height: int = surfaces[0].get_height() # Hauteur du layer
        self.image = self.origin_images[0]  # Image du layer
        self.current_image: int = 0 # Image actuelle
        self.rect = self.image.get_rect() # Rectangle du layer
        self.rect.x: int = pos # Position x du layer 
        self.rect.y: int = 0 # Position y du layer
        self.speed: int = speed # Vitesse de déplacement du layer

    def update(self, player_speed: int) -> None:
        """
        Met à jour la position du layer
        player_speed: vitesse du joueur
        """
        self.rect.x -= (self.speed * player_speed) # Déplacement du layer
        if self.rect.x <= -self.width: # Si le layer sort de l'écran
            self.rect.x += self.width * 2 # On le replace à la fin du layer
        self.current_image += 1 # On passe à l'image suivante
        if self.current_image >= len(self.origin_images): # Si on a atteint la dernière image
            self.current_image = 0 # On revient à la première image
        self.image = self.origin_images[self.current_image] # On met à jour l'image
