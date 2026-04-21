from linvision import LinVision 
import subprocess

vision = LinVision()
word = input("enter one word\n")

coords = vision.find_element(word)

if coords:
    x, y = coords
    print(f"found: {x}, {y}")
    
    socket = "YDOTOOL_SOCKET=/tmp/.ydotool_socket"
    
    # Use '--' to separate options from positional arguments.
    # This prevents the argument parser from crashing.
    cmd = (
        f"sudo {socket} ydotool mousemove -a -- 0 0 && "
        f"sudo {socket} ydotool mousemove -- {x} {y} click 0xC0"
    )
    
    subprocess.run(cmd, shell=True)
    print("clicked")
else:
    print("none")
