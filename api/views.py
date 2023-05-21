import json
import os
import subprocess
from django.http import HttpResponse
from . import cv
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def process_img(request): #post /api/process
      if request.method != 'POST':
            data = {'res': 'Only POST requests allowed!'}
            res = HttpResponse(content=json.dumps(data), content_type='application/json')
            return res
      file_name = request.FILES['image']
      #file_content = file_name.read()
      current_directory = os.getcwd()
      darknet_directory = os.path.join(current_directory, "darknet")

      if os.getcwd() != darknet_directory:
            os.chdir(darknet_directory)
      command = './darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights ' + file_name.path
      subprocess.run([command])
      newPath = cv.saveImg('predictions.jpg')
      file = None
      with open(newPath, "r") as f:
            file = f.read()
      data = {'res', file}
      res = HttpResponse(content=json.dumps(data), content_type='application/json')
      return res