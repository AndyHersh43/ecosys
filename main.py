#Main simulation loop

import pygame, pygame_gui
from lib.creatures import Plant, Herbivore, Carnivore
from lib.world import World
import sys
import time

if __name__ == '__main__':
    pygame.init()

    SIM_WIDTH = 1500
    SIM_HEIGHT = 1000

    #TODO implement these somehow
    #GUI_WIDTH = 1920
    #GUI_HEIGHT = 1080

    SIM_SIZE = (SIM_WIDTH, SIM_HEIGHT)
    sim_screen = pygame.display.set_mode(SIM_SIZE, 0, 32)

    #GUI_SIZE = (GUI_WIDTH, GUI_HEIGHT)
    #gui_man = pygame_gui.UIManager(GUI_SIZE)
    gui_man = pygame_gui.UIManager(SIM_SIZE)
    pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(SIM_WIDTH-75, SIM_HEIGHT-75, 50, 50), text='||', manager=gui_man)
    play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(SIM_WIDTH-125, SIM_HEIGHT-75, 50, 50), text='>', manager=gui_man)
    ffw_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(SIM_WIDTH-175, SIM_HEIGHT-75, 50, 50), text='>>', manager=gui_man)

    clock = pygame.time.Clock()
    is_running = True

    world = World(SIM_SIZE)


    #Add Creatures to world
    for i in range(50):
        world.add_creature(Plant(world))
        time.sleep(0.01)
    
    sex_setter = True
    for i in range(15):
        world.add_creature(Herbivore(world, sex=sex_setter))
        time.sleep(0.01)
        world.add_creature(Carnivore(world, sex=sex_setter))
        time.sleep(0.01)
        sex_setter = not sex_setter
    
    #################################
    #### Main sim loop and logic ####
    #################################
    paused = False
    speed_mult = 1000
    tick_speed = 60
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                sys.exit()
            #UI button Listener
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                #check for pause via UI
                if event.ui_element == pause_button:
                    paused = not paused
                #check for time speed up via UI
                if event.ui_element == ffw_button:
                    speed_mult = 300
                #check for time speed up via UI
                if event.ui_element == play_button:
                    speed_mult = 1000
            #Keyboard button listener
            elif event.type == pygame.KEYDOWN:
                #check for pause via spacebar
                if event.key == pygame.K_SPACE:
                    paused = not paused
                #check for speed update via 1 key
                if event.key == pygame.K_1:
                    speed_mult = 1000
                #check for speed update via 2 key
                if event.key == pygame.K_2:
                    speed_mult = 300

            gui_man.process_events(event)
        
        time_elapsed = clock.tick(tick_speed)
        time_elapsed = time_elapsed/speed_mult
        
        if paused == False:
            sim_screen.fill((0,150,20))
            world.process(time_elapsed)
            world.render(sim_screen)
            #gui_man.draw_ui(GUI_SIZE)
            gui_man.draw_ui(sim_screen)

        pygame.display.update()
        gui_man.update(time_elapsed)