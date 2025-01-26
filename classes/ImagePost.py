from Post import Post
import pygame
from constants import *
class ImagePost(Post):
    def __init__(self, username, location, desc, likes, img):
        super().__init__(username, location, desc, likes)
        img = pygame.image.load(img)
        self.img = pygame.transform.scale(img,(POST_X_POS, POST_Y_POS))