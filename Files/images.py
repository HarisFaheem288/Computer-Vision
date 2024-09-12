import cv2
def load_and_show_image(image_path):
    image = cv2.imread(image_path)
    if image is not None:
        cv2.imshow('Loaded Image', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"Error: Could not load image at {image_path}")
load_and_show_image('uber.jpg')
load_and_show_image('a.jpg')


