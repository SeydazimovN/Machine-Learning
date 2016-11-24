import Image

# Apple = Image.open("apple.jpg")    
# Apple.show()
# instead of using .open and .show(), 
# save the image to show it with the webbrowser module

filename = "bear.png"
import webbrowser
webbrowser.open(filename)
