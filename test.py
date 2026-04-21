from linvision import LinVision 
print("imported")

vision = LinVision()
vision.capture()
word = input("enter one word")

coords = vision.find_element(word)

print(coords)
