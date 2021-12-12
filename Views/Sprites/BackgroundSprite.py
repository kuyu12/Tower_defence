from Utils.Paths import MAP_IMAGES_PATH
from Views.Sprites.AnimatedSprite import AnimatedSprite


class BackgroundSprite(AnimatedSprite):

    def __init__(self, background_name, use_full_path=False, is_image=False, location=(0, 0)):

        if is_image:
            self.images = [background_name]
        elif use_full_path:
            self.images = self.get_images_with_path(background_name)
        else:
            self.images = self.get_images_with_path(MAP_IMAGES_PATH + '/' + background_name)

        super(BackgroundSprite, self).__init__(location, self.images)
