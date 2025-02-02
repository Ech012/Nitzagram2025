import pygame

from constants import *
from helpers import *

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
        self.text_font = from_text_to_array(self.text)

        text_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        text = text_font.render(self.text, True, self.text_color, self.background_color)
        for i in self.text:
            screen.blit(self.text_font[i], (center_text(2, self.text[i], i)))

