import configs
import assets
import pygame
from object.background import Background
from object.floor import Floor
from object.column import Column
from object.bird import Bird
from object.gamestart_message import GameStartMessage
from object.gameover_message import GameOverMessage
from object.score import Score


pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH,configs.SCREEN_HEIGHT))
clock = pygame.time.Clock()
column_create_event = pygame.USEREVENT
running = True
gameover = False
gamestarted = False


assets.load_sprites()

sprites = pygame.sprite.LayeredUpdates() 

def create_sprites():
    Background(0,sprites)
    Background(1,sprites)
    Floor(0,sprites)
    Floor(1,sprites)

    return Bird(sprites), GameStartMessage(sprites), Score(sprites)

bird, game_start_message, score = create_sprites()

#pygame.time.set_timer(column_create_event,1500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == column_create_event:
            Column(sprites)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not gamestarted and not gameover:
                gamestarted = True
                game_start_message.kill()
                pygame.time.set_timer(column_create_event,1500)
            if event.key == pygame.K_SPACE and gameover:
                gameover = False
                gamestarted = False
                sprites.empty()
                bird, game_start_message, score = create_sprites()
        
        bird.handle_event(event)

    screen.fill(0)
    sprites.draw(screen)
    
    if gamestarted and not gameover:
        sprites.update()

    if bird.check_collison(sprites):
        gameover = True
        gamestarted = False
        GameOverMessage(sprites)
        pygame.time.set_timer(column_create_event,1500)

    for sprite in sprites:
        if type(sprite) is Column and sprite.is_passed():
            score.value += 1

    pygame.display.flip()
    clock.tick(configs.FPS)

pygame.quit() 