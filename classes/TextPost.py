import pygame

from constants import *
from helpers import screen

from classes.Post import Post

class TextPost(Post):

    def __init__(self, username, location, desc, likes, text, text_color, background_color, comments=None):
        super().__init__(username, location, desc, likes, comments)
        self.text = text
        self.text_color = text_color
        self.background_color = background_color


    def display(self):
        super().display()

        # Display the text on the post
        text_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        text = text_font.render(self.text, True, self.text_color, self.background_color)
        screen.blit(text, (POST_X_POS, POST_Y_POS))

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        """
        pass