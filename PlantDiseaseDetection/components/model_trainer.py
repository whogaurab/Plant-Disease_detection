import os,sys
import yaml
import zipfile
import subprocess
from PlantDiseaseDetection.utils.main_utils import read_yaml_file
from PlantDiseaseDetection.logger import logging
from PlantDiseaseDetection.exception import AppException
from PlantDiseaseDetection.entity.config_entity import ModelTrainerConfig
from PlantDiseaseDetection.entity.artifacts_entity import ModelTrainerArtifact



class ModelTrainer:
    def __init__(
        self,
        model_trainer_config: ModelTrainerConfig,
    ):
        self.model_trainer_config = model_trainer_config



# class ModelTrainer:
#     def initiate_model_trainer(self) -> ModelTrainerArtifact:
#         logging.info("Entered initiate_model_trainer method of ModelTrainer class")

#         try:
#             logging.info("Unzipping data")
#             with zipfile.ZipFile('data.zip', 'r') as zip_ref:
#                 zip_ref.extractall()

#             file_name = "data.zip"
#             try:
#                 os.remove(file_name)
#                 print(f"{file_name} removed successfully")
#                 logging.info("File removed successfully")
#             except Exception as e:
#                 raise AppException(e, sys)

#             with open('data.yaml', 'r') as stream:
#                 num_classes = str(yaml.safe_load(stream)['nc'])

#             model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
#             print(model_config_file_name)

#             config = read_yaml_file(f"yolov9/models/detect/{model_config_file_name}.yaml")
#             config['nc'] = int(num_classes)

#             with open(f'yolov9/models/detect/custom_{model_config_file_name}.yaml', 'w') as f:
#                 yaml.dump(config, f)

#             # Run YOLOv9 training using subprocess
#             subprocess.run([


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



#                 # "python", "train.py",
                
#                 # "--batch", str(self.model_trainer_config.batch_size),
#                 # "--epochs", str(self.model_trainer_config.no_epochs),
#                 # "--img", "640",
#                 # "--device 0",
#                 # "--min-items 0",
#                 # "--close-mosaic 15",
#                 # "--data", "../data.yaml",
#                 # "--weights", self.model_trainer_config.weight_name,
#                 # "--device", "0",
#                 # "--cfg", ".yolov9/models/detect/gelan-e.yaml",
#                 # "--hyp", "yolov9/data/hyps/hyp.scratch-high.yaml"
#             ], cwd="yolov9/")

#             # Copy best weights
#             subprocess.run(["cp", "yolov9/runs/train/weights/best.pt", "yolov9/"])
#             os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
#             subprocess.run(["cp", "yolov9/runs/train/weights/best.pt", f"{self.model_trainer_config.model_trainer_dir}/"])

#             # Clean up intermediate files
#             os.remove("yolov9/runs")
#             os.remove("train")
#             os.remove("valid")
#             os.remove("test")
#             os.remove("data.yaml")

#             model_trainer_artifact = ModelTrainerArtifact(
#                 trained_model_file_path="yolov9/best.pt",
#             )

#             logging.info("Exited initiate_model_trainer method of ModelTrainer class")
#             logging.info(f"Model trainer artifact: {model_trainer_artifact}")

#             return model_trainer_artifact

#         except Exception as e:
#             raise AppException(e, sys)



    def initiate_model_trainer(self,) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data")
            # os.system("unzip data.zip")
            # os.remove("data.zip")

            with zipfile.ZipFile("data.zip", 'r') as zip_ref:
                zip_ref.extractall()

            file_name="data.zip"
            try:
                os.remove(file_name)
                print(f"{file_name} removed sucessfully")
                logging.info("file removed sucessfully")

            except Exception as e:
                raise AppException(e, sys)


            with open("data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])

            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)

            config = read_yaml_file(f"yolov9/models/detect/{model_config_file_name}.yaml")

            config['nc'] = int(num_classes)


            with open(f'yolov9/models/detect/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)



# !python train_dual.py --workers 8 --batch 4  --img 640 --epochs 50 --data /mydrive/yolov9/yolov9/data.yaml --weights /mydrive/yolov9/yolov9-e.pt --device 0 --cfg /mydrive/yolov9/yolov9/models/detect/yolov9_custom.yaml --hyp /mydrive/yolov9/yolov9/data/hyps/hyp.scratch-high.yaml
     



            os.system(f"cd yolov9/ && python train.py --workers 8  --batch {self.model_trainer_config.batch_size} --img 640  --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --weights {self.model_trainer_config.weight_name} --device 0 --cfg .yolov9\models\detect\gelan-e.yaml  --hyp yolov9\data\hyps\hyp.scratch-high.yaml")
            os.system("cp yolov9/runs/train/weights/best.pt yolov9/")
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(f"cp yolov5/runs/train/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")
           
            os.remove("yolov9/runs")
            os.remove("train")
            os.remove("valid")
            os.remove("test")
            os.remove("data.yaml")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov9/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact


        except Exception as e:
            raise AppException(e, sys)




        
