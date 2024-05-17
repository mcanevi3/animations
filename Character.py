import pygame
import math

from config import *

class Sprite:
    width=0
    height=0
    pos=(0,0)
    frames=None
    template_img=None
    template_fname=""
    duration=0 # of frame
    i=0
    def __init__(self,fname,slice_width,duration=5):
        self.template_fname=fname
        self.width=slice_width
        self.duration=duration

    def getSurface(self,dt):
        
        if self.template_img is None:
            self.template_img=pygame.image.load(config.config("user_character_folder")+self.template_fname+".png").convert_alpha()
            full_width,self.height=self.template_img.get_size()
            self.frames=full_width/self.width

        surface=self.template_img.subsurface(pygame.Rect(math.floor(self.i)*self.width,0,self.width,self.height))
        self.i=(self.i+((1 * dt)/self.duration))%self.frames
        return surface


class Character:
    sprites={"_Idle":Sprite("_Idle",120),"_Attack":Sprite("_Attack",120),"_Run":Sprite("_Run",120),"_Roll":Sprite("_Roll",120)}
    state="_Run"
    
    def render(self,dt,screen,pos=(0,0)):
        self.pos=pos
        sprite=self.sprites[self.state]
        scaled=pygame.transform.scale_by(sprite.getSurface(dt),2.5)
        screen.blit(scaled,self.pos)
        return self

    def change_state(self,state):
        self.state=state
        return self
    
    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN:
                pass
            elif event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
            else:
                pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        return self
