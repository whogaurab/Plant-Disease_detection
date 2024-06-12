import sys
from PlantDiseasedetection.exception import AppException
try:
     a  = 3/"s"

except Exception as e:
     
     raise AppException(e, sys)