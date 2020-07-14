import pygame
import random
pygame.init()

screen_info=pygame.display.Info()
print(screen_info)
size=(width,height)=(screen_info.current_w,screen_info.current_h)
clock=pygame.time.Clock()
screen=pygame.display.set_mode(size)
color= (0,127,255)
fish_image=pygame.image.load('fish.png')
fish_image=pygame.transform.smoothscale(fish_image,(80,100))

fish_rect=fish_image.get_rect()
fish_rect.center=(400,300)
speed=pygame.math.Vector2(20,-20)
def move_fish():
  global fish_image
  global fish_rect
  fish_rect.move_ip(speed)
  if fish_rect.top<0 or fish_rect.top> height:
    speed[1]*=-1
    fish_image=pygame.transform.flip(fish_image,False,True)
    fish_rect=pygame.transform.flip(fish_rect,False,True)

    
  if fish_rect.right>width:
    speed[0]*=-1
  if fish_rect.left<0:
    speed[0]*=-1
  


def main():
  while True:
    clock.tick(60)
    screen.fill(color)
    screen.blit(fish_image,fish_rect)
    move_fish()
    pygame.display.flip()
if __name__=='__main__':
  main()