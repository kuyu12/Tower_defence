import os
from math import cos, sin, atan2

import pygame
from enum import Enum
import re

from Utils.Image_utils import ImageUtils
from Utils.Math_utils import get_degrees


class Update_Type(Enum):
    TIME = 1
    FRAME = 2


class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, position, images,animation_time =0.3):
        super(AnimatedSprite, self).__init__()

        self.images = images
        self.index = 0
        self.current_degree = None
        self.image = images[self.index]  # 'image' is the current image of the animation.
        self.size = self.image.get_rect().size
        self.rect = self.image.get_rect()
        self.animation_time = animation_time
        self.current_time = 0

        self.animation_frames = len(images)
        self.current_frame = 0

        self.dt = 0.01

        self.rect.x = position[0]
        self.rect.y = position[1]

    def update_time_dependent(self, dt):
        if len(self.images) == 1:
            return

        self.current_time = self.current_time + dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
            self.frame_was_update()

    def update_frame_dependent(self):
        if len(self.images) == 1:
            return

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
            self.frame_was_update()

    def frame_was_update(self):
        pass

    def update(self, update_type=Update_Type.TIME):
        if update_type == Update_Type.TIME:
            self.update_time_dependent(self.dt)

        if update_type == Update_Type.FRAME:
            self.update_frame_dependent()

    def rotate_images(self, angle, image_to_rotate=None):
        if image_to_rotate:
            image, rect = self.rotate_center(image_to_rotate, self.rect, angle)
        else:
            image, rect = self.rotate_center(self.image, self.rect, angle)

        self.image = image
        self.rect = rect

    # Only if you override original_image
    def check_image_by_direction(self, pos, next_pos):
        degrees = round(get_degrees(pos, next_pos))
        if self.current_degree is None:
            self.current_degree = -degrees
            self.rotate_images(-degrees, self.original_image)
            return

        diff = (self.current_degree - degrees + 360) % 360
        degree_move = 1 if diff > 180 else -1 if diff < 180 else 0
        self.current_degree = self.current_degree + degree_move
        self.rotate_images(self.current_degree, self.original_image)

    def rotate_center(self, image, rect, angle):
        """Rotate a Surface, maintaining position."""
        rot_img = pygame.transform.rotate(image, angle)
        # Get a new rect and pass the center position of the old
        # rect, so that it rotates around the center.
        rect = rot_img.get_rect(center=rect.center)
        return rot_img, rect  # Return the new rect as well.

    @staticmethod
    def get_images_with_path(path, with_resize=False, resize=None):
        images = []

        if os.path.isdir(path):
            dirlist = sorted(os.listdir(path), key=lambda x: int(re.findall(r'[0-9]+', x)[-1]))
            for image in dirlist:
                image_load = ImageUtils.load_image(os.path.join(path, image))
                if with_resize:
                    image_load = ImageUtils.scale_image(image_load,resize)
                images.append(image_load)
        else:
            image = ImageUtils.load_image(path)
            if with_resize:
                image = ImageUtils.scale_image(image, resize)
            images.append(image)

        return images
