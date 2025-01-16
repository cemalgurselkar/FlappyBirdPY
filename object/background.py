from typing import Any
from pygame.sprite import Sprite
import assets
import configs
from layer import Layer

configs = configs.Config()
class Background(Sprite):
    def __init__(self, index,*groups):
        self._layer = Layer.BACKGROUND
        self.image = assets.get_sprite("background")
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH*index,0))
        
        super().__init__(*groups)
    
    def update(self):
        self.rect.x -= 2 
        if self.rect.right <=0:
            self.rect.x = configs.SCREEN_WIDTH