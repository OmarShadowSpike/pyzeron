## About
This package is used for creating 2D Games.
It is not complete yet, this is just a demo for pyzeron.

## Installation
Just type the following to install this package.
```python
pip install pyzeron
```

## Usage
```python
from pyzeron import App, Rect, Circle

# Creating the application.
app = App("My Window", 800, 600)

# Creating objects.
myRect = Rect(10, 10, 100, 200)
myCircle = Circle(300, 500, 50, 20)

myRect2 = Rect(10, 250, 50, 50)
myCircle2 = Circle(600, 400, 20, 20)
objList = [myRect2, myCircle2]

# Setting the background.
app.setBackgroundColor((20, 20, 20)) # it uses Red, Green, Blue (RGB), example: (255, 0, 0) will turn red.

# Showing or hiding the fps.
app.showFps() # This just show the current fps.
app.hideFps() # Hides the fps.

# The loop used for the app, you can name it what ever you want.
def loop():
	
	# This is how you draw an object or objects.
	app.draw(myRect) # Draws myRect.
	app.draw(myCircle) # Draws myCircle.

	app.drawList(objList) # Drawing all objects at once by creating a list.

# Running the application.
app.run(fps=60, inLoop=loop)

```
