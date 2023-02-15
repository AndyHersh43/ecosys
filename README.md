# ecosys
A little ecosystem simulator. Uses Abstract Base Classes in Python to generate: Predators (carnivores), Prey (herbivores) and Plants which are all based on a "Creature" base class. Uses pygame to render the interactions.

Relies on pygame and pygame_gui. 

To run the sim:
1. Install Python
https://www.python.org/downloads/

3. Install pygame via pip 
```
pip install pygame
```

3. Install pygame_gui via pip 
```
pip install pygame_gui
```

5. CD into the directory of the clone and type "python main.py" into the terminal at the root of the project

As of right now any changes to the simulation attributes will require a code change as there are no user input modifications possible besides altering the speed of the simulation.

TODO:
1. Add a way to speed the sim up as well as pause it ✅
2. Implement a live statistical readout of the current state of the simulation world (how many carnivores, herbivores... how many females/males) 
3. Implement a statistics screen for specific entities that is toggled by clicking the entity
4. TBD
