from helpers import *
from constants import *
class Comment:
    def __init__(self, text):
        self.text = text



    def display(self, i):
        font = pygame.font.SysFont("Arial",COMMENT_TEXT_SIZE)
        text = font.render(self.text, True, (0,0,0))
        screen.blit(text, [FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + (i * COMMENT_LINE_HEIGHT)])

