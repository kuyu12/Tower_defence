from Views.Sprites.AnimatedSprite import AnimatedSprite, Update_Type


class AnimatedSpriteOneTime(AnimatedSprite):

    def __init__(self, position, images):
        super(AnimatedSpriteOneTime, self).__init__(position, images)
        self.numbers_of_image = self.animation_frames
        self.images_show_counter = 0

    def update(self, update_type=Update_Type.TIME):
        if self.images_show_counter == self.numbers_of_image:
            self.kill()
            return

        super().update(update_type)


    def frame_was_update(self):
        self.images_show_counter += 1;