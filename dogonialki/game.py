from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, playar_x, playar_y, playar_speed, width=55, height=55):
      super().__init__()
      self.image = transform.scale(image.load(player_image), (width, height))
      self.speed = playar_speed
      self.rect = self.image.get_rect()
      self.rect.x = playar_x
      self.rect.y = playar_y
# Ворог
class Enemy(GameSprite):
    side = "left"
    
    def __init__(self, enemy_image, x, y, speed):
        super().__init__(enemy_image, x, y, speed, 65, 65)
        self.alive = True
        

    def update(self):
        if self.rect.x <= 470:
            self.side = "right"
        if self.rect.x >= win_width - 85:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
            
    """Вбивство монстра."""
    def die(self):
        self.kill()
        self.alive = False

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__(player_image, player_x, player_y, player_speed)
        self.last_direction = "up"

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
            self.last_direction = "left"
        if keys[K_RIGHT] and self.rect.x < win_width - 60:
            self.rect.x += self.speed
            self.last_direction = "right"
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
            self.last_direction = "up"
        if keys[K_DOWN] and self.rect.y < win_height - 60:
            self.rect.y += self.speed
            self.last_direction = "down"

    def fire(self):
        if not finish:
            bullet = Bullet('bullet.png', self.rect.centerx, self.rect.centery, 8, self.last_direction)
            bullets.add(bullet)
            gun_sound.play()

class Bullet(GameSprite):

   def __init__(self, image, x, y, speed, direction):
      super().__init__(image, x, y, speed, 15, 15)
      self.direction = direction
      
   def update(self):
      if self.direction == 'up':
         self.rect.y -= self.speed
      elif self.direction == "down":
         self.rect.y += self.speed
      elif self.direction == "left":
         self.rect.x -= self.speed
      elif self.direction == "right":
         self.rect.x += self.speed
         
   if self.rect.y < 0 or self.rect.y > win_height or self.rect.x < 0 or self.rect.x > win_width:
      self.kill()

class Wall(sprite.Sprite):
   def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
      super().__init__()
      self.color_1 = color_1
      self.color_2 = color_2
      self.color_3 = color_3
      self.wight = wall_width
      self.height = wall_height

      self.image = Surface((self.wight, self.height))
      self.image.fill((color_1, color_2, color_3))

      self.rect = self.image.get_rect()
      self.rect.x = wall_x
      self.rect.y = wall_y

# Функція для запуску гри
def start_game():
    global pacman, monster, final_point, walls, bullets, finish, start_time
    
    pacman = Player('hero.png', 5, win_height - 80, 4)
    monster = Enemy('monster.png', win_width - 80, 280, 2)
    final_point = GameSprite('final_point.png', win_width - 120, win_height - 80, 0)
    
    # Група стіни
    walls = sprite.Group(
        Wall(154, 205, 50, 100, 0, 10, 380),
        Wall(154, 205, 50, 200, 130, 10, 380),
        Wall(154, 205, 50, 450, 130, 10, 380),
        Wall(154, 205, 50, 300, 0, 10, 350),
        Wall(154, 205, 50, 390, 120, 130, 10)
    )
    # Група патрони
    bullets = sprite.Group()
    # Статус гри
    finish = False
    # Час для статистики
    start_time = time.get_ticks()
    


win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Лабіринт")

# Завантаження фону
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
win_bg = transform.scale(image.load("win_bg.png"), (win_width, win_height))
lose_bg = transform.scale(image.load("lose_bg.png"), (win_width, win_height))

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

game = True
finish = False
start_game()

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
