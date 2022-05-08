# Bomberman pygame application day 3

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start
- [Pygame primer](https://realpython.com/pygame-a-primer/#sprite-groups)
- [Pygame sprites and groups](https://kidscancode.org/blog/2016/08/pygame_1-2_working-with-sprites/)

You already have spiders, that chase the player, 
bombs, that can explode.
Now you have to implement such features:
1. Create an Enemy class hierarchy and add other types of enemies, for example:
   - Boar, that can drop rocks. All units cannot walk over the rocks, but
   rocks can be destroyed by bombs.
   - Bird, that doesn't chase the player, can fly over the obstacles, can
   drop bombs.
2. Create an Effect class hierarchy. After any enemy dies, it has a 
small chance for a random effect to be dropped. Effect changes the
characteristics of the player if the player picks it up. Create a few types
of effects, for example:
   - Effect, that heals the player for 20 health points.
   - Effect, that slows player for the two speed points.
   - Effect, that accelerates player for the two speed points.

It is the final stage of this project, be free to implement everything
that you want. 
- You can change existing logic, add more information
to the interface, add additional properties to the player and enemies
and manipulate with them, add an event to generate allies, that try
to help you overcome the enemies, add bombs, that can destroy walls,
add an effect that makes walls 
disappear for a few seconds (difficult one), etc. 

Use free 2D images
[Source 1](https://opengameart.org/), [Source 2](https://craftpix.net/).
It all depends on your imagination.

Example: 

![Example](https://user-images.githubusercontent.com/80070761/154242811-d5105c93-d899-4733-abcf-55449d382871.gif)"# bomberman" 
