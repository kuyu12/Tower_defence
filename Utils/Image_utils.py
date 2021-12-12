import pygame


class ImageUtils:
    @staticmethod
    def scale_image(image,scale_size):
        return pygame.transform.smoothscale(image,scale_size)

    @staticmethod
    def load_image(image_path):
        return pygame.image.load(image_path).convert_alpha()