from Manager.Stage import Stage
from Screens.base_screen import BaseScreen

class GameScreen(BaseScreen):
    def __init__(self):
        self.stage = None
        pass

    def handel_event(self,event):
        if self.stage:
            self.stage.update_event(event)

    def draw_screen(self,screen):
        if self.stage:
            self.stage.draw(screen)
            self.stage.update()

    def start_stage(self,stageName):
        self.stage = Stage(stageName) # 'First_wave'