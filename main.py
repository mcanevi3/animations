import pygame
import time

from Character import *

class App:
    FPS=60
    prev_time=time.time()
    TARGET_FPS=60
    dt=0

    char1=Character()
    def __init__(self):
        self.running = True
        self.screen = None
        self.clock=pygame.time.Clock()

    def on_init(self):
        self.running = True
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF,display=1)
        self.size = self.width, self.height = pygame.display.get_window_size()
        print(f"Screen size is {self.width}x{self.height}")
        
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
        
        self.char1.on_event(event)

    def on_loop(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now
        self.clock.tick(self.FPS)

    def on_render(self):
        deltaTime = self.dt * self.TARGET_FPS
        
        surface=pygame.Surface((self.width,self.height))
        surface.fill((0,0,0))
        self.screen.blit(surface,(0,0))

        self.char1.render(deltaTime,self.screen)
        pygame.display.flip()
                                       
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self.running = False

        while( self.running ):
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()