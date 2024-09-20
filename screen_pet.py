# on-screen pet design with differing expressions according to user input

# import necessary tools from tkinter library
from tkinter import HIDDEN, NORMAL, Tk, Canvas
import random


def toggle_eyes():
    """" This function makes the eyes look closed by
        hiding the pupils and filling the eyes with
        the same color as the body"""
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)


def blink():
    """
    blinks the eye every 3seconds for 250milliseconds
    """
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)


def toggle_left_eye():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)


def wink(event):
    toggle_left_eye()
    root.after(250, toggle_left_eye)


def toggle_pupils():
    """
    switches pet's pupil between pointing inwards and looking normal
    """
    if not c.eyes_crossed:  # checks if eyes are crossed already
        # moves the pupils if eyes not crossed
        c.move(pupil_left, 10, -5)
        c.move(pupil_right, -10, -5)
        c.eyes_crossed = True  # sets flag variable that eyes are crossed
    else:
        c.move(pupil_left, -10, 5)
        c.move(pupil_right, 10, 5)
        c.eyes_crossed = False  # sets flag variable that eyes are not crossed


def toggle_tongue():
    """
    toggles pet's tongue between being out or in
    """
    if not c.tongue_out:  # checks if tongue is already out
        # tongues become visible if not previously out
        c.itemconfigure(tongue_tip, state=NORMAL)
        c.itemconfigure(tongue_main, state=NORMAL)
        c.tongue_out = True  # sets a flag variable indicating tongue is out
    else:  # but if tongue is already out
        # tongues are hidden if out
        c.itemconfigure(tongue_tip, state=HIDDEN)
        c.itemconfigure(tongue_main, state=HIDDEN)
        c.tongue_out = False  # sets a flag variable indicating tongue isn't out


def cheeky(event):
    """
    pet sticks its tongue out and cross its eyes at the same time
    """
    toggle_tongue()  # tongue out
    toggle_pupils()  # eyes crossed
    hide_happy(event)  # hides happy face
    root.after(1000, toggle_tongue)  # tongue in after 1000 milliseconds
    root.after(1000, toggle_pupils)  # eyes uncrossed after 1000 milliseconds
    return


def show_happy(event):
    """
    show happy expression when mouse pointer
    hovers over the screen pet as if stroking it
    """
    if (20 <= event.x <= 350) and (20 <= event.y <= 350):  # checks if mouse pointer is over the pet
        # show the pink cheeks
        c.itemconfigure(cheek_left, state=NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL)
        c.itemconfigure(mouth_happy, state=NORMAL)  # show the happy mouth
        c.itemconfigure(mouth_normal, state=HIDDEN)  # hide the normal mouth
        c.itemconfigure(mouth_sad, state=HIDDEN)  # hide the sad mouth
        c.happy_level = 10
    return


def hide_happy(event):
    """
    set screen pet's expression back to normal
    """
    # hide the pink cheeks
    c.itemconfigure(cheek_left, state=HIDDEN)
    c.itemconfigure(cheek_right, state=HIDDEN)
    c.itemconfigure(mouth_happy, state=HIDDEN)  # hide the happy mouth
    c.itemconfigure(mouth_normal, state=NORMAL)  # show the normal mouth
    c.itemconfigure(mouth_sad, state=HIDDEN)  # hide the sad mouth


def sad():
    """
    change's pet's expression to sad
    """
    if c.happy_level == 0:  # checks if happy_level value is zero
        # changes expressions from happy and normal to sad
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=NORMAL)
    else:  # happy_level is greater than one
        c.happy_level -= 1  # subtracts 1 from happy_level value
    root.after(5000, sad)  # sad fn calls itself recursively after 5 seconds until stroked


def change_color():
    """
    changes the pet's color by selecting randomly from a list of
    given colors at intervals of 5 seconds
    """
    pet_colors = ['SkyBlue1', 'tomato', 'yellow', 'purple', 'green', 'orange']
    # sets pet's body, ears and feet to new color
    c.body_color = random.choice(pet_colors)
    c.itemconfigure(body, outline=c.body_color, fill=c.body_color)
    c.itemconfigure(ear_left, outline=c.body_color, fill=c.body_color)
    c.itemconfigure(ear_right, outline=c.body_color, fill=c.body_color)
    c.itemconfigure(foot_left, outline=c.body_color, fill=c.body_color)
    c.itemconfigure(foot_right, outline=c.body_color, fill=c.body_color)
    root.after(5000, change_color)


root = Tk()
# set canvas, background color and pet color
c = Canvas(root, width=400, height=400)
c.configure(bg='dark blue', highlightthickness=0)
c.body_color = 'SkyBlue1'
# pet body part configuration
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
# ears
ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)
# feet
foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill=c.body_color)
# eyes and pupils
eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')
# mouth
mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
# changing mood to create a happy mouth
mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
# create a sad mouth
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)
# create tongue
tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)
# create pink a blushing cheeks
cheek_left = c.create_oval(70, 180, 120, 230, outline='pink', fill='pink', state=HIDDEN)
cheek_right = c.create_oval(280, 180, 330, 230, outline='pink', fill='pink', state=HIDDEN)

c.pack()

c.bind('<Motion>', show_happy)  # links the moving mouse pointer to the happy face
c.bind('<Leave>', hide_happy)  # calls hide_happy fn when mouse pointer leaves the pet
# c.bind('<Double-1>', cheeky)  # calls cheeky fn after a double mouse clicks
c.bind('<Double-1>', wink)  # calls wink fn after a double mouse clicks

c.happy_level = 10
c.eyes_crossed = False
c.tongue_out = False
root.after(1000, blink)
root.after(5000, sad)
root.after(5000, change_color)
root.mainloop()
