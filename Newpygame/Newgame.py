# import pygame module in this program 
import pygame
import math  
# activate the pygame library .  
# initiate pygame and give permission  
# to use pygame's functionality.  
pygame.init()

#Screen resolution
infos = pygame.display.Info()
screen_size = (infos.current_w, infos.current_h)
res = screen_size  
# create the display surface object  
# of specific dimension..e(500, 500).  
win = pygame.display.set_mode(res)
  
# set the pygame window name 
pygame.display.set_caption("Moving rectangle")

#get width and height of screen
Swidth = win.get_width()
Sheight = win.get_height()

# object current co-ordinates 
x = 200
y = 200
x2 = 0
y2 = 0
mx = 0
my = 0
cx = 0
cy = 0
# dimensions of the object 
width = 20
height = 20 
  
# velocity / speed of movement
vel = 10
#Tick timer
FPS = 60
fpsclock = pygame.time.Clock()

# Indicates pygame is running
run = True

#colors
color = (0,0,255)
color2 =(250,0,0)
#variables
ballq=[]

#functions
#classes
class player():
   width = width
   height = height
   screen_location = [x2,y2]
   def __init__(self): 
    self.image = pygame.Surface((width,height))
    self.image.fill(color)
    self.rect = self.image.get_rect()
    self.vel = [0,0]

   def update(self):
    self.rect.move_ip(*self.vel)
   
  
    
class ball():
 status = False
 def __init__(self):
   self.image = pygame.Surface((10,10))
   #pygame.draw.circle(self.image,(color),(cx,cy),5)
   self.image.fill(color)
   self.rect = self.image.get_rect()
   self.vel = [0,0]
 def move(self,cx,cy):
   vel=[cx,cy]
   self.rect.move_ip(*self.vel)
 def shoot(self,mx,mc,cx,cy):
    #mouse position down and to the right of a rect: Does not work goes in one direction forever crashing game
       if mx > cx and my > cy:
          rx = mx - cx
          ry = my - cy
          angle = math.atan2(ry,rx)
          vx = math.cos(angle)
          vy = math.sin(angle)
          print("Worked!")
          if cx < Swidth and cy < Sheight:
           cx = vx * dt
           cy = vy * dt
           print("Worked 2!")
           self.move(cx,cy)

       # mouse position is up and to the left of a rect: Works
       elif cx > mx and cy > my:
          rx = cx - mx
          ry = cy - my
          angle = math.atan2(ry,rx)
          vx = math.cos(angle)
          vy = math.sin(angle)
          print("Worked 3!")
          if cx > 0 and cy > 0:
           ''' 
           while cx != mx and cy != my and cx > 0 and cy > 0:
            pygame.draw.circle(win,(color), (cx,cy), 5)
            pygame.display.update()
            win.fill((0, 0, 0))
            win.blit(player1.image, player1.rect)
            '''
           cx = dt*vx
           cy = dt*vy
           print("Worked 4!")
           self.move(cx,cy)
       # mouse position is down and to the left of a rect: Works Causes bounce?
       elif mx > cx  and cy > my: 
          rx = mx - cx
          ry = cy - my
          angle = math.atan2(ry,rx)
          vx = math.cos(angle)
          vy = math.sin(angle)
          print("Worked 5!")
          if cx < Swidth and cy > 0:
           '''
          while cx != mx and cy != my and cx < Swidth and cy > 0:
            pygame.draw.circle(win,(color), (cx,cy), 5)
            pygame.display.update()
            win.fill((0, 0, 0))
            win.blit(player1.image, player1.rect)
           '''
           cx = dt*vx
           cy = dt*vy
           print("Worked 6!")
           self.move(cx,cy)
       # mouse position is up and to the right of a rect: kind of works Causes bounce?
       elif cx > mx  and my > cy:
          rx = cx - mx
          ry = my - cy
          angle = math.atan2(ry,rx)
          vx = math.cos(angle)
          vy = math.sin(angle)
          print("Worked 7!")
          if cx > 0 and cy < Sheight:
           '''
          while cx != mx and cy != my and cx > 0 and cy < Sheight:
            pygame.draw.circle(win,(color), (cx,cy), 5)
            pygame.display.update()
            win.fill((0, 0, 0))
            win.blit(player1.image, player1.rect)
            '''
           cx = dt*vx
           cy = dt*vy
           print("Worked 8!")
           self.move(cx,cy)
       else:
         status = True
       # mouse position is below the rect: Works
       if mx == cx and my > cy:
          ry = my - cy
          cx = 0
          print("Worked 9!")
          if cy != my:
           '''
           while cy != my:
            pygame.draw.circle(win,(color), (cx,cy), 5)
            pygame.display.update()
            win.fill((0, 0, 0))
            screen.blit(player1.image, player1.rect)
            '''
           cy = dt
           print("Worked 10!")
          self.move(cx,cy)
       # mouse position is above the rect: Works
       elif mx == cx and cy > my:
          ry = cy - my
          cx = 0
          print("Worked 11!")
          if cy != my:
           '''    
          while cy != my:
            pygame.draw.circle(win,(color), (cx,cy), 5)
            pygame.display.update()
            win.fill((0, 0, 0))
            screen.blit(player1.image, player1.rect)
          '''
           print("Worked 12!")
           cy = dt
           self.move(cx,cy)
       # mouse position is to the right of rect: Works
       elif mx > cx and my == cy:
          rx = mx - cx
          cy = 0
          print("Worked 13!")
          if cx != mx:
            '''  
            while cx != mx:
            pygame.draw.circle(win,(color), (cx,cy), 5)
            pygame.display.update()
            win.fill((0, 0, 0))
            screen.blit(player1.image, player1.rect)
            '''
            print("Worked 14!")
            cx = dt
            self.move(cx,cy)
       # mouse position is to the left of rect: Works
       elif cx > mx and my == cy: 
          rx = cx - mx
          cy = 0
          print("Worked 15!")
          if cx != mx:
           '''
           while cx != mx:
            pygame.draw.circle(win,(color), (cx,cy), 5)
            pygame.display.update()
            win.fill((0, 0, 0))
            screen.blit(player1.image, player1.rect)
            '''
           print("Worked 16!")
           cx = dt
           self.move(cx,cy)
       else:
         status = True
    
player1 = player()
balls = ball()
# infinite loop 
while run:
    # creates time delay of 10ms 
    #pygame.time.delay(10)
    dt = fpsclock.tick(FPS) / 100 
    # iterate over the list of Event objects  
    # that was returned by pygame.event.get() method.  

    # if event object type is QUIT  
       # then quitting the pygame  
       # and program both.
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
              
            # it will make exit the while loop 
            run = False       
              
    # stores keys pressed 
    keys = pygame.key.get_pressed()
    
    #player2 = player() 
    # if a key is pressed
    if keys[pygame.K_a] and x>0:
          
        # decrement in x co-ordinate
        player1.vel[0] = -100 * dt
        x2 += -100*dt  
    # if d key is pressed
    if keys[pygame.K_d] and x<Swidth-width:
          
        # increment in x co-ordinate
         player1.vel[0] = 100 * dt
         x2 += 100*dt
    # if w key is pressed   
    if keys[pygame.K_w] and y>0:
          
        # decrement in y co-ordinate
        player1.vel[1] = -100 * dt
        y2 += -100 * dt  
    # if s key is pressed   
    if keys[pygame.K_s] and y<Sheight-height:
        # increment in y co-ordinate
        player1.vel[1] = 100 * dt
        y2 += 100 * dt
    if event.type == pygame.KEYUP:
            '''
            if event.key == pygame.K_w or event.key == pygame.K_s: #Can cause issue where if two buttons are pressed at the same time it would keep going
                player1.vel[1] = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                player1.vel[0] = 0
                '''
            player1.vel[0] = 0
            player1.vel[1] = 0

    
    if keys[pygame.K_ESCAPE]:
      # closes the pygame window 
      pygame.quit()

    cx = x2 + 10
    cy = y2 + 10
    if event.type == pygame.MOUSEBUTTONDOWN:
       (mx,my) = pygame.mouse.get_pos()
       balls.shoot(mx,my,cx,cy)
       win.blit(balls.image,balls.rect)    
          
    # completely fill the surface object  
    # with black colour  
    win.fill((0, 0, 0))
      
    # drawing object on screen which is rectangle here 
    #pygame.draw.rect(win, (color), (x, y, width, height))
    player1.update()
    win.blit(balls.image,balls.rect)   
    win.blit(player1.image, player1.rect)
    # it refreshes the window
    pygame.display.update()

    fpsclock.tick(FPS) 
  


