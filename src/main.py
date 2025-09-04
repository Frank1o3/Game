""" Test of the game engine """
import os
import sys

# add the Libs directory to the system path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), 'Libs'))

from Libs.engine import Engine
from Libs.entity import Entity
from Libs.shape import Circle, Rectangle
from Libs.vector import Vector2


def main():
    """ Main function to set up and run the physics engine simulation. """
    engine = Engine()

    # Create some entities with shapes and add them to the engine
    circle = Circle(center=Vector2(0, 10), radius=1)
    rectangle = Rectangle(position=Vector2(5, 15), width=2, height=3, static=True)

    entity1 = Entity(shape=circle, mass=3.0)
    entity2 = Entity(shape=rectangle, mass=3.0)

    engine.add_entity(entity1)
    engine.add_entity(entity2)

    # Run the engine (this will run indefinitely until interrupted)
    engine.run()

if __name__ == "__main__":
    main()
