import pygame

from constants import *
from helpers import screen

import classes.Comment

class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__( self,username, location, desc, likes, comments = None):
        self.username = username
        self.location = location
        self.desc = desc
        self.likes = likes
        self.comments_display_index = 2
        if comments is None:
            self.comments = []
        else:
            self.comments = comments


    def add_like(self):
        self.likes += 1

    

    def display(self):
        """
        Display the Post image or textText, description, location, likes and comments
        on screen

        :return: None
        """

        # Display the post
        #display the description
        description_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        description = description_font.render(self.desc, True, BLACK)
        screen.blit(description, (DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS))
        #display the location
        location_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        location = location_font.render(self.location, True, BLACK)
        screen.blit(location, (LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS))
        #display the likes
        likes_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        likes = likes_font.render(str(self.likes), True, BLACK)
        screen.blit(likes, (LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS))
        #display the username
        username_font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        username = username_font.render(self.username, True, BLACK)
        screen.blit(username, (USER_NAME_X_POS, USER_NAME_Y_POS))

        self.display_comments()

        


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



