import pygame


class ThirdLayer(pygame.sprite.Sprite):

    def __init__(self, surfaces: list[pygame.Surface], speed: int, pos: int) -> None:
        super().__init__()
        self.origin_images: list[pygame.Surface] = [pygame.transform.smoothscale(
            surfaces[x], (surfaces[x].get_width(), surfaces[x].get_height())).convert_alpha() for x in range(len(surfaces))]
        # Check if all images have the same size
        for x in range(len(self.origin_images)):
            if self.origin_images[x].get_width() != self.origin_images[0].get_width() or self.origin_images[x].get_height() != self.origin_images[0].get_height():
                raise Exception(
                    "All images must have the same size in the third layer")
        self.width: int = surfaces[0].get_width()
        self.height: int = surfaces[0].get_height()
        self.image = self.origin_images[0]
        self.current_image: int = 0
        self.rect = self.image.get_rect()
        self.rect.x: int = pos
        self.rect.y: int = 0
        self.speed: int = speed

    def update(self, player_speed: int) -> None:
        self.rect.x -= (self.speed * player_speed)
        if self.rect.x <= -self.width:
            self.rect.x += self.width * 2
        self.current_image += 1
        if self.current_image >= len(self.origin_images):
            self.current_image = 0
        self.image = self.origin_images[self.current_image]
