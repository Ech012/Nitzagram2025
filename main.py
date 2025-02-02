import pygame
from helpers import screen
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK
from classes.ImagePost import ImagePost
from classes.Comment import Comment
def main():
    # Set up the game display, clock and headline
    pygame.init()
    #ksdfjlsg;lsjdgsdfkj
    # Change the title of the window
    pygame.display.set_caption('Nitzagram')
    clock = pygame.time.Clock()
    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,
                                        (WINDOW_WIDTH, WINDOW_HEIGHT))

    # TODO: add a post here
    run_img = ImagePost("Harel", "sdf", "Sdf", 17, "Images\\noa_kirel.jpg", [Comment("hiajj"), Comment("sakmdsa")])
    print(run_img)
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
        run_img.display()

        # Update display - without input update everything
        pygame.display.update()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)
    pygame.quit()
    quit()


main()
sdf
sdf
sdf
sdf
sd
fsd
fs
df
sdf
sdf
sdf
sdf
sd
from sdf
sdf
sdf
sdf
sd
f
