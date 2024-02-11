import cv2
from cv2 import dnn_superres

class ImageSuperResolution:
    def __init__(self):
        self.sr = dnn_superres.DnnSuperResImpl_create()
        self.modelPath = "models/LapSRN_x2.pb"
        self.modelName = "lapsrn"
        #"/model/LapSRN_x8.pb"
        #"/model/LapSRN_x.pb"
        #"/model/LapSRN_x8.pb"


    def read_model(self, model_path, model_name, scale):
        self.sr.readModel(model_path)
        self.sr.setModel(model_name, scale)

    def upscale(self, image_path):
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Image at {image_path} could not be read.")
        return self.sr.upsample(image)

    def save_image(self, image, output_path):
        cv2.imwrite(output_path, image)

    def process_image(self, scale, image_path, output_path):
        self.read_model(self.modelPath, self.modelName, scale)
        result = self.upscale(image_path)
        self.save_image(result, output_path)


if __name__ == "__main__":
    model_path = "/path/to/your/model/LapSRN_x2.pb"
    model_name = "lapsrn"
    scale = 2
    image_path = "ImageFiles/1695767957-0.png"
    output_path = "UpscaledImages/upscaled3.png"
    
    isr = ImageSuperResolution()
    isr.process_image(scale, image_path, output_path)



