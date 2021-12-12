from Utils.Conts import EXPLOSION_SIZE
from Views.Sprites.Animated_sprite_one_time import AnimatedSpriteOneTime


class ExplosionSprite(AnimatedSpriteOneTime):
    def __init__(self, position, path):
        images = self.get_images_with_path(path,with_resize=True,resize=EXPLOSION_SIZE)
        super(ExplosionSprite, self).__init__(position, images)