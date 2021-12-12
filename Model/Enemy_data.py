from Model.Figure_data import FigureData


class EnemyData(FigureData):
    def __init__(self, index, name, health, speed, image_url,worth_money):
        super(EnemyData, self).__init__(index, name, image_url)
        self.health = health
        self.speed = speed
        self.worth_money = worth_money
