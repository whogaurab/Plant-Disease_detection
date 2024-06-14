
from PlantDiseaseDetection.pipeline.training_pipeline import TrainPipeline

obj =TrainPipeline()
obj.run_pipeline()



# import sys,os
# import subprocess
# from PlantDiseaseDetection.pipeline.training_pipeline import TrainPipeline
# from PlantDiseaseDetection.utils.main_utils import decodeImage, encodeImageIntoBase64
# from flask import Flask, request, jsonify, render_template,Response
# from flask_cors import CORS, cross_origin
# from PlantDiseaseDetection.constant.application import APP_HOST, APP_PORT


# app = Flask(__name__)
# CORS(app)

# class ClientApp:
#     def __init__(self):
#         self.filename = "inputImage.jpg"



# @app.route("/train")
# def trainRoute():
#     obj = TrainPipeline()
#     obj.run_pipeline()
#     return "Training Successfull!!" 

# @app.route("/")
# def home():
#     return render_template("index.html")


# @app.route("/predict", methods=['POST','GET'])
# @cross_origin()
# def predictRoute():
#     try:
#         image = request.json['image']
#         decodeImage(image, clApp.filename)

#         # os.system("cd yolov9/ && python detect.py --weights my_model.pt --img 640 --conf 0.5 --source ../data/inputImage.jpg")
#         subprocess.run([


#                 "--batch", "16",
#                 "--epochs", "100",
#                 "--img", "640",
#                 "--device", "0",
#                 "--min-items", "0",
#                 "--close-mosaic", "15",
#                 "--data", "../data.yaml",
#                 "--weights", "/yolov9/weights/gelan-c.pt",
#                 "--cfg", "/yolov9/models/detect/gelan-c.yaml",
#                 "--hyp", "/yolov9/data/hyps/hyp.scratch-high.yaml"
#                 ], cwd="yolov9/")
        
#         opencodedbase64 = encodeImageIntoBase64("yolov9/runs/detect/exp/inputImage.jpg")
#         result = {"image": opencodedbase64.decode('utf-8')}

#         remove_run = "yolov9/runs"
#         os.remove(remove_run)

#         # os.system("rm -rf yolov9/runs")

#     except ValueError as val:
#         print(val)
#         return Response("Value not found inside  json data")
#     except KeyError:
#         return Response("Key value error incorrect key passed")
#     except Exception as e:
#         print(e)
#         result = "Invalid input"

#     return jsonify(result)


# @app.route("/live", methods=['GET'])
# @cross_origin()
# def predictLive():
#     try:
#         os.system("cd yolov5/ && python detect.py --weights my_model.pt --img 416 --conf 0.5 --source 0")
#         os.system("rm -rf yolov5/runs")
#         return "Camera starting!!" 

#     except ValueError as val:
#         print(val)
#         return Response("Value not found inside  json data")
    



# if __name__ == "__main__":
#     clApp = ClientApp()
#     app.run(host=APP_HOST, port=APP_PORT)
