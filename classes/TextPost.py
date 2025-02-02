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
        text_arr = from_text_to_array(self.text)
        
        #diplay a rectangle with the background color
        pygame.draw.rect(screen, self.background_color, (POST_X_POS, POST_Y_POS, POST_WIDTH, POST_HEIGHT))
        for i in range(len(text_arr)):
            text_font = pygame.font.SysFont('chalkduster.ttf', TEXT_POST_FONT_SIZE)
            text = text_font.render(text_arr[i], True, self.text_color)
            screen.blit(text, (center_text(len(text_arr), text, i)))

