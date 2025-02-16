from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, playar_x, playar_y, playar_speed, width=55, height=55):
      super().__init__()
      self.image = transform.scale(image.load(player_image), (width, height))
      self.speed = playar_speed
      self.rect = self.image.get_rect()
      self.rect.x = playar_x
      self.rect.y = playar_y

window=display.set_mode((700, 500))
display.set_caption("Dogonialki")
background = transform.scale(image.load("background.png"), (700, 500))
window.blit(background, (0, 0))

x1 = 100
y1 = 300

x2 = 300
y2 = 300

sprite1 = transform.scale(image.load("sprite2.png"), (100, 100))
sprite2 = transform.scale(image.load("sprite1.png"), (100, 100))

game = True
clock = time.Clock()
FPS = 60
speed = 10

mixer.init()
mixer.music.load("fon.mp3")
mixer.music.play()

mixer_sound = mixer.Sound("final_point.mp3")
klick_sound = mixer.Sound("voice.mp3")
gun_sound = mixer.Sound("piupiu.mp3")
voice_sound = mixer.Sound("voice.mp3")

while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2, (x2, y2))

    for e in event.get():
        if e.type == QUIT:
            game = False

    keys_pressed = key.get_pressed()

    if keys_pressed[K_LEFT] and x1 > 5:
       x1 -= speed
    if keys_pressed[K_RIGHT] and x1 < 595:
       x1 += speed
    if keys_pressed[K_UP] and y1 > 5:
       y1 -= speed
    if keys_pressed[K_DOWN] and y1 < 395:
       y1 += speed
 
    if keys_pressed[K_a] and x2 > 5:
       x2 -= speed
    if keys_pressed[K_d] and x2 < 595:
       x2 += speed
    if keys_pressed[K_w] and y2 > 5:
       y2 -= speed
    if keys_pressed[K_s] and y2 < 395:
       y2 += speed
    
    display.update()
    clock.tick(FPS)