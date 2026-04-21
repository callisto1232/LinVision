import os
import cv2
import numpy as np
from paddleocr import PaddleOCR

def setup_linvision():
    print("--- Initializing LinVision Engine ---")
    
    # This line triggers the download of models (~150MB total)
    # use_gpu=False is mandatory for your i3 setup
    try:
        ocr = PaddleOCR(
            lang='en', 
            use_gpu=False, 
            show_log=True,
            use_angle_cls=True
        )
        print("\n✅ OCR Models downloaded and loaded successfully.")
    except Exception as e:
        print(f"\n❌ Error initializing OCR: {e}")
        return

    print("\n--- Testing OpenCV & Image Processing ---")
    try:
        # Create a dummy image (black square) to test OpenCV
        blank_image = np.zeros((100, 100, 3), dtype=np.uint8)
        cv2.putText(blank_image, 'Test', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        # Test if OCR can process the dummy image
        result = ocr.ocr(blank_image, cls=True)
        print("✅ OpenCV and OCR pipeline verified.")
        
    except Exception as e:
        print(f"❌ Image processing test failed: {e}")

if __name__ == "__main__":
    # Disable the model source check to speed things up
    os.environ['PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK'] = 'True'
    setup_linvision()
