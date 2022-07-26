"""
File: 03_scene.py
Author: Leah Tajon

Purpose: Prove that you can write functions with parameters
and call those functions multiple times with arguments.

"""

# Import the functions from the Draw 2-D library
# so that they can be used in this program.
# Import random to call random numbers
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_grid(canvas, scene_width, scene_height, 20)
    draw_sky(canvas, scene_width, scene_height)
    draw_clouds(canvas, scene_width, scene_height)
    draw_skyscrapers(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_road(canvas, scene_width, scene_height)

    # Draw pine trees on the ground
    for x in range(15):
        tree_center_x = random.randint(100, 700)
        tree_bottom = random.randint(120, 200)
        tree_height = random.randint(80, 180)

        draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)
        x += 1

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Define your functions such as
# draw_sky and draw_ground here.

def draw_grid(canvas, width, height, interval):
    # Draw vertical lines at every x interval
    label_y = 20
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f'{x}')

    # Draw horizontal lines at every y interval
    label_x = 20
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f'{y}')

def draw_sky(canvas, width, height):
    # Draw the sky
    draw_rectangle(canvas, 0, height / 2, width, height, width=0, fill="deepSkyBlue2")

def draw_clouds(canvas, width, height):
    # Draw clouds that randomly change shape
    min_diam = 50
    max_diam = 100

    for i in range(80):
        x = random.randint(0, width - max_diam)
        y = random.randint(0, height)
        diameter = random.randint(min_diam, max_diam)

        draw_oval(canvas, x, y, x + diameter, y + diameter, width=0, fill='lightCyan1')
    pass

def draw_skyscrapers(canvas, width, height):
    # Draw skyscrapers that randomly change in shape
    x = 20
    y = 250

    n = 30
    m = 300

    for i in range(80):
        diameter1 = random.randint(50, 100)
        diameter2 = random.randint(80, 180)
        
        draw_rectangle(canvas, x, y, x + diameter1, y + diameter2, width=0, fill='dodgerBlue4')

        x += random.randint(40, 120)
    pass

def draw_ground(canvas, width, height):
    # Draw the ground and all the objects in the ground.

    draw_rectangle(canvas, 0, 100, width, height / 2, width=0, fill='forestGreen')

    diameter = 12
    space = 2
    interval = diameter + space

    # Draw a row of flowers
    x = 10
    y = 102

    for i in range(56):
        draw_oval(canvas, x, y, x + diameter, y + diameter, outline="orangeRed1", width=3, fill="yellow")
        x += interval

def draw_pine_tree(canvas, center_x, bottom, height):
    # Draw random pine trees on the ground
    
    trunk_width = height / 30
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    # Draw the trunk of the flower
    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, outline="gray20", 
        width=2, fill="tan3")

    # Draw the skirt
    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height
    
    draw_polygon(canvas,center_x, skirt_top, skirt_right, trunk_top, skirt_left, trunk_top,
        outline="darkGreen", width=2, fill="green1")

def draw_road(canvas, width, height):
    # Draw the road and all the objects in the road.
    draw_rectangle(canvas, 0, 0, width, height / 5, outline="lightBlue4", width=2, fill='gray25')

    # Draw center line
    x = 20
    y = 40
    for i in range(5):
        draw_rectangle(canvas, x, y, x + 100, y + 20, outline="lightBlue4", width=2, fill='azure')
        x += 160

# Call the main function so that
# this program will start executing.
main()