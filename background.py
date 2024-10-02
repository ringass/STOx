from simulator_interfaces import *
import pygame

class Background(Drawable):
    def draw(self, screen: Surface) -> None:
        win_size = screen.get_size()
        pygame.draw.rect(screen, (0,0,0), (0,0,win_size[0], win_size[1]))