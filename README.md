## About
This package is used for creating 2D Games.
It is not complete yet, this is just a demo for pyzeron.
As it is now it is almost complete!
I will release the version 1.0.0 this month or the next month.

---

## Pip Installation
If you dont have pip already all you have to do is download the **Python Installer** again on the [Python Website](https://www.python.org/).
After you download the python installer open it and click on **Modify**.
Then check the box of the pip and hit next and install.

---

## Pyzeron Installation
Please find which **Operating System** your using.

### Windows
If you want this version open your command prompt and type:
```
pip install pyzeron==1.0.0.dev3
```
Else type:
```
pip install pyzeron
```

### Mac
If you want this version open your Spotlight search bar and type **Terminal** after that type:
```
pip3 install pyzeron==1.0.0.dev3
```
Else type:
```
pip3 install pyzeron
```

### Linux
If you want this version open any **Terminal** and type:
```
sudo apt-get install python-pyzeron==1.0.0.dev3
```
Else type:
```
sudo apt-get install python-pyzeron
```

---

## Changelog
The changelog can be seen in [here](https://github.com/OmarShadowSpike/pyzeron/blob/main/CHANGELOG.txt)
But if you want the current version changelog here it is.

		Pyzeron 1.0.0.dev3
		- Added Button Class
		- Bug fixes
		- README Improvements
		- Line Class: Complete!

---

## Usage
This is how your suppose should use pyzeron.
Of course you can use it of how you want to use it.
You can use this package in any ways, but this is my recommendation.
```python
from pyzeron import *

# Creating the application.
app = App("My Window", 800, 600)

# Creating objects.
my_rect = Rect(10, 10, 100, 200)
my_circle = Circle(300, 500, 50, 20)

my_rect2 = Rect(10, 250, 50, 50)
my_circle2 = Circle(600, 400, 20, 20)
obj_list = [my_rect2, my_circle2]

# Setting the background.
app.set_background_color((20, 20, 20)) # it uses Red, Green, Blue (RGB), example: (255, 0, 0) will turn red.

# Showing or hiding the fps.
app.show_fps() # This just show the current fps.
app.hide_fps() # Hides the fps.

# The loop used for the app, you can name it what ever you want.
def loop():

	# This is how you draw an object or objects.
	app.draw(my_rect) # Draws my_rect.
	app.draw(my_circle) # Draws my_circle.

	app.draw_list(obj_list) # Drawing all objects at once by creating a list.

# Running the application.
app.run(fps=60, loop=loop)
```
