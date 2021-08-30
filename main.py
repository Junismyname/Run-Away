# This code is for a pygame that is based off of games like Flappy Bird, where the background and player can move and must avoid objects that appear within the window of vision
import pygame
import os
import random

#Minigame stuff

# multiplayer 8pool

  # background

  # 2 Sticks

  # Balls

    # Black Ball

    # Stripes

    # Non_stripes
# Something like jetpack joyride, but with doodle jump kind of background

  # simple background
  
  # starting background

# This class is for creating the object Background which is comprised of the image for the background of the game and the starting screen that players first encounter
class Background:
    # This function provides the information for the classs to create the background and access the background image
  def __init__(self,width,height):
    self.bg_pic = pygame.image.load(os.path.join("assets", "dot_grid.jpg")).convert()
    self.bg = pygame.Rect(0,0,width,360)
    self.width = width
    self.x_axis1 = 0
    self.x_axis2 = self.width
  
  #
  def updating(self):
    self.x_axis1 -= 2 
    self.x_axis2 -= 2
    if self.x_axis1 < self.width * -1: 
      self.x_axis1 = self.width
    if self.x_axis2 < self.width * -1:
      self.x_axis2 = self.width

 # This function tells the code where to place the background picture
  def rendering(self):
    screen.blit(self.bg_pic, (self.x_axis1, 0))
    screen.blit(self.bg_pic, (self.x_axis2, 0))

  # This function holds the text, text size and color, and background color for the starting screen
  def startscreen(self):
    screen.fill((101, 141, 209))
    pygame.font.init()
    title = pygame.font.Font('Pangolin-Regular.ttf', 42)
    self.text = title.render("[Title]", True, (0,0,0))
    subtext = pygame.font.Font('Pangolin-Regular.ttf', 22)
    self.text2 = subtext.render("Press any key to begin", True, (0,0,0))

 # This function has the information to print and orient the text on the starting screen
  def startscreen_render(self):
      self.textx = 270
      self.texty = 150     
      screen.blit(self.text, (self.textx,self.texty))
      screen.blit(self.text2, (self.textx-15, self.texty+50))

   
# This class, player, is used to create the object player which is what the user controls in the game
class player:
    #
  def __init__(self, x = 50, y = 160):

    self.player_flying = pygame.transform.scale(pygame.image.load(os.path.join("assets","sprite1flight.png")),(20,20)).convert()
    self.player_notflying = pygame.transform.scale(pygame.image.load(os.path.join("assets","sprite1.png")),(20,20)).convert()
    self.player_pic = self.player_notflying

    # This aspect of the code globalizes the variable player and also sets the size and initial location of the character
    global player
    self.player = player = pygame.Rect(50, 160, 20, 20)
  # This movement function tells the code how far to move left or right and how high to jump when the variable jump is called
  def move(self):
    stepsize = 12
    jumping = -22

    self.player.move_ip(0, 12)
    #
    keys = pygame.key.get_pressed()
    if self.player.top > 10:
      if keys[pygame.K_UP]:
        self.player_pic = self.player_flying
        self.player.move_ip(0,jumping)
      else:
        self.player_pic = self.player_notflying
    elif self.player.top > 0:
      if keys[pygame.K_UP]:
        jumping = -self.player.top
    if self.player.left > 12:
      if keys[pygame.K_LEFT]:
        self.player.move_ip(-stepsize,0)
    elif self.player.left > 0:
      if keys[pygame.K_LEFT]:
        stepsize = -self.player.left
    if self.player.right < 708:  
      if keys[pygame.K_RIGHT]:
        self.player.move_ip(stepsize, 0)
    elif self.player.right < 720:
      if keys[pygame.K_RIGHT]:
        stepsize = 760 - self.player.right
  
   # 
  def rendering(self):
    screen.blit(self.player_pic, self.player)

# Objects
    # Monsters

    # Real obstacles
class Object:
  def __init__(self):
    self.Barricade = []
    ground  = pygame.Rect(0,360, 720, 20)    
    self.Barricade.append(ground)

  def monsters(self,monster):
      monster_list = [pygame.Rect(random.randint(73,78)*10, random.randint(0,8)*40,40,40),pygame.Rect(random.randint(0,1)*40,random.randint(-10,-1)*10,40,40),pygame.Rect(random.randint(0,17)*40,random.randint(37,42)*10,40,40)]
      return monster_list[random.randint(0,2)]

  def blocks(self):
    for Barricade in self.Barricade:
      pygame.draw.rect(screen, (0,0,0), Barricade)
  
  def collision(self):
    index = player.collidelist(self.Barricade)
    if index != -1:
      player.bottom = self.Barricade[index].top 


screen = pygame.display.set_mode((720, 360))

example = Background(720,360)
character = player()
example.startscreen()
objects = Object()
clock = pygame.time.Clock()
checker = True
off_screen = True
monster_event = True
right_jumping = 10
bottom_jumping = 10
top_jumping = 10
Monsters_right = []
Monsters_bottom = []
Monsters_top = []
monster_normal = pygame.transform.scale(pygame.image.load(os.path.join("assets","monster1.png")),(40,40)).convert()
for Monster in range(15):
  monster = objects.monsters(Monster)
  if monster.x in range(730,781) and monster.y in range(0,361):
    Monsters_right.append(monster)
  elif monster.x in range(0,721) and monster.y in range(-10,-101):
    Monsters_top.append(monster)
  elif monster.x in range(0,721) and monster.y in range(370, 420):
    Monsters_bottom.append(monster)
print(Monsters_right,"\n", Monsters_top, "\n", Monsters_bottom)

while True:
  clock.tick(10)

  if checker == True:
    example.startscreen_render()
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN: 
        checker = False
        print(checker)
        
  else:
    pygame.event.get()
    character.move()
    for Monster in Monsters_right:
      if Monster.x >= 730: 
          right_jumping = -10
      if Monster.x <= 650:
          right_jumping = 10  
      Monster.move_ip(right_jumping, 0)
    for Monster in Monsters_top:
      if Monster.y <= -50:
        top_jumping = 10
      if Monster.y >= 20:
        top_jumping = -10
      Monster.move_ip(0, top_jumping)
    for Monster in Monsters_bottom:
      if Monster.y >= 370:
        bottom_jumping = -10
      if Monster.y <= 290:
        bottom_jumping  = 10
      Monster.move_ip(0, bottom_jumping)
    objects.collision()
    example.updating()
    
    example.rendering()
    for Monster in Monsters_right:
      screen.blit(monster_normal, Monster)
    for Monster in Monsters_bottom:
      screen.blit(monster_normal, Monster)
    for Monster in Monsters_top:
      screen.blit(monster_normal, Monster)      
    
    character.rendering()
    objects.blocks()
  pygame.display.update()



pygame.quit()

  # items?

  # scorebar

  # game ending text
'''finaltext = pygame.font.Font('Pangolin-Regular.ttf', 42)
self.text3= finaltext.render("Game Over!", True, (0,0,0))'''
