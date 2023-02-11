import os
from typing import Dict

from fastapi import FastAPI, UploadFile
from PIL import Image
from imageai.Detection import ObjectDetection
from pydantic import BaseModel
from collections import defaultdict

app = FastAPI()
execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsTinyYOLOv3()
detector.setModelPath(os.path.join(execution_path, "tiny-yolov3.pt"))
detector.loadModel()

detector_retinanet = ObjectDetection()
detector_retinanet.setModelTypeAsRetinaNet()
detector_retinanet.setModelPath(os.path.join(execution_path, "retinanet_resnet50_fpn_coco-eeacb38b.pth"))
detector_retinanet.loadModel()


class Item(BaseModel):
    animals: Dict[str, int]


@app.post(
    "/animals",
    response_model=Item,
    response_description="Image contains objects:",
)
async def analyse_image(upload_file: UploadFile, precise_mode: bool):
    """
    Loads an animal image for analysis:

    The response contains json with the number and type of objects in the photo.
    Modes:
     1. Slow and precise, precise_mode=True;
     2. Fast and imprecise, precise_mode=False;
    """
    image_objects = defaultdict(int)

    with Image.open(upload_file.file) as input_image:

        if precise_mode:
            detection_objects = detector_retinanet.detectObjectsFromImage(
                input_image=input_image,
                # output_image_path=os.path.join(execution_path, "image_new.jpg"),
                # Save mode. If you need to see the image, you must uncomment the previous line
                minimum_percentage_probability=30
            )
        else:
            detection_objects = detector.detectObjectsFromImage(
                input_image=input_image,
                # output_image_path=os.path.join(execution_path, "image_new.jpg"),
                # Save mode. If you need to see the image, you must uncomment the previous line
                minimum_percentage_probability=30
            )

        for each_object in detection_objects:
            image_objects[each_object["name"]] += 1

        return {"animals": image_objects}
