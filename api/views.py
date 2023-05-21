import json
import os
import subprocess
from django.http import HttpResponse
from . import cv
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


@csrf_exempt
def process_img(request):  # post /api/process
    if request.method != 'POST':
        data = {'res': 'Only POST requests allowed!'}
        res = HttpResponse(content=json.dumps(
            data), content_type='application/json')
        return res
    file = request.FILES['image']
    if 'darknet' not in os.getcwd():
        os.chdir('./darknet')
    default_storage.save('data/' + file.name, ContentFile(file.read()))
    command = './darknet detector test cfg/coco.data cfg/yolov4.cfg yolov4.weights data/' + file.name
    subprocess.run([command])
    newPath = cv.saveImg('predictions.jpg')
    file = None
    with open(newPath, "r") as f:
        file = f.read()
    data = {'res', file}
    res = HttpResponse(content=json.dumps(
        data), content_type='application/json')
    file.delete()
    return res
