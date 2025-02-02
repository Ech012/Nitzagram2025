import pygame
from helpers import screen, read_comment_from_user
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, GREY
import classes.Post
import  classes.TextPost
import classes.Comment
# Import the Post class

def main():
    # Set up the game display, clock and headline
    pygame.init()
    # Change the title of the window
    pygame.display.set_caption('Nitzagram')
    clock = pygame.time.Clock()
    # Set up background image
    background = pygame.image.load('Images/background.png')
    
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # Create a Post object with the Noa Kirel image
    path = "C:\\Users\\User\Desktop\\פרוייקט ניצנים\\Nitzagram2025\\Images\\noa_kirel.jpg"
    #do it with a red background
    commect_list = [classes.Comment.Comment("Nice!")]
    post = classes.TextPost.TextPost("Noa Kirel", "Tel Aviv", "Shabbat Shalom", 100, "Shabbat Shalom", (0, 0, 0), (GREY), commect_list)

    

    running = True
    while running:
        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))
        
        # Display the post
        post.display()
        
        # Display the comments
        read_comment_from_user()
        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()

main()
