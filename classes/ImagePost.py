from classes.Post import Post
import pygame
from constants import *
from helpers import *
class ImagePost(Post):
    def __init__(self, username, location, desc, likes, img, comments = None):
        super().__init__(username, location, desc, likes, comments)
        img = pygame.image.load(img)
        self.img = pygame.transform.scale(img,(POST_WIDTH, POST_HEIGHT))

    def display(self):
        super().display()
        screen.blit(self.img, (POST_X_POS, POST_Y_POS))
