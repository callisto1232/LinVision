import subprocess
import os
import time
from paddleocr import PaddleOCR

class LinVision:
    def __init__(self):
        # Initialize OCR once to keep it in memory
        self.ocr = PaddleOCR(lang='en', use_gpu=False, show_log=False)
        self.temp_img = "/tmp/linvision_capture.png"

    def take_screenshot(self):
        """Uses spectacle to grab the screen on KDE/Wayland."""
        try:
            # -b: background, -n: non-interactive, -o: output path
            subprocess.run(["spectacle", "-b", "-n", "-o", self.temp_img], check=True)
            return True
        except Exception as e:
            print(f"Screenshot failed: {e}")
            return False

    def find_text_on_screen(self, target_text):
        """Captures screen and returns coordinates of target text."""
        if not self.take_screenshot():
            return None
            
        results = self.ocr.ocr(self.temp_img, cls=True)
        
        if not results or not results[0]:
            return None

        for line in results[0]:
            detected_text = line[1][0]
            if target_text.lower() in detected_text.lower():
                # Box format: [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]
                box = line[0]
                center_x = (box[0][0] + box[2][0]) / 2
                center_y = (box[0][1] + box[2][1]) / 2
                return int(center_x), int(center_y)
        
        return None

if __name__ == "__main__":
    vision = LinVision()
    print("Searching for 'Activities' or 'Application' on your panel...")
    # Change 'Application' to something you currently see on your screen
    coords = vision.find_text_on_screen("Application")
    
    if coords:
        print(f"Found it at: {coords}")
    else:
        print("Text not found on screen.")
