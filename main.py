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
    pause_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(1425, 925, 50, 50), text='||', manager=gui_man)

    clock = pygame.time.Clock()
    is_running = True

    world = World(SIM_SIZE)

    sex_setter = True

    #Add Creatures
    for i in range(50):
        world.add_creature(Plant(world))
        time.sleep(0.01)
    
    for i in range(15):
        world.add_creature(Herbivore(world, sex=sex_setter))
        time.sleep(0.01)
        world.add_creature(Carnivore(world, sex=sex_setter))
        time.sleep(0.01)
        sex_setter = not sex_setter

    paused = False
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            elif event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == pause_button:
                    paused = not paused
            gui_man.process_events(event)
        
        #Sim Loop
        sim_screen.fill((0,150,20))
        time_elapsed = clock.tick(60)
        time_elapsed = time_elapsed/1000
        gui_man.update(time_elapsed)

        world.process(time_elapsed)
        world.render(sim_screen)
        #gui_man.draw_ui(GUI_SIZE)
        gui_man.draw_ui(sim_screen)

        pygame.display.update()