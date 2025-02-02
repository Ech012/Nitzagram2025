import pygame

from constants import *
from helpers import screen


class Comment:
    def __init__(self, text):
        self.text = text


    def display(self, i):

        # Display the comment
        comment_font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        comment = comment_font.render(self.text, True, BLACK)
        screen.blit(comment, (FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + i * COMMENT_LINE_HEIGHT))

        





    


    