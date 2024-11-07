from pygame_widgets.button import Button


class TDButton(Button):

    def update_text(self, text):
        self.text = self.font.render(
            text, True, self.textColour)
        self.textRect = self.text.get_rect()
        self.alignTextRect()
