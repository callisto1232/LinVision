import os
import subprocess
from paddleocr import PaddleOCR
from PIL import Image
import time

class LinVision:
    def __init__(self, debug_folder="data/temp"):
        self.debug_folder = debug_folder
        if not os.path.exists(self.debug_folder):
            os.makedirs(self.debug_folder)

        self.last_shot = os.path.join(self.debug_folder, "current_screen.png")
        if os.path.exists(self.last_shot):
            os.remove(self.last_shot)

        self.ocr = PaddleOCR(lang="en",
                             show_log=False,
                             use_ange_cls=True,
                             det_limit_side_len=960,
                             det_db_thresh=0.3,
                             det_db_box_thresh=0.5
        )

    def capture(self):
        try:
            subprocess.run(["spectacle", "-f", "-b", "-o", self.last_shot], check=True)
            time.sleep(2)
            return self.last_shot
        except Exception as e:
            print(f"Capture Error: {e}")
            return None

    def find_element(self, target_text):
        # Uses PaddleOCR to find the coordinates of a text on the screen
        if not os.path.exists(self.last_shot):
            self.capture()
        result = self.ocr.ocr(self.last_shot, cls=True)

        for line in result:
            for res in line:
                coords = res[0]
                text = res[1][0]

                if target_text.lower() in text.lower():
                    center_x = (coords[0][0] + coords[2][0]) / 2
                    center_y = (coords[0][1] + coords[2][1]) / 2
                    return(int(center_x), int(center_y))
        return None

