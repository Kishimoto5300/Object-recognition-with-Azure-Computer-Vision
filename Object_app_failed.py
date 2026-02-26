#using Image Analysis 3.2
#tag_image()はインターネット上のURL用（remote）なのにローカルファイルのパスを渡したらだめ！！

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

import tkinter as tk   #added
import tkinter.filedialog as fd  #added


'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = os.environ["VISION_KEY"]
endpoint = os.environ["VISION_ENDPOINT"]

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
'''
END - Authenticate
'''

'''
Quickstart variables
These variables are shared by several examples
'''
# Images used for the examples: Describe an image, Categorize an image, Tag an image, 
# Detect faces, Detect adult or racy content, Detect the color scheme, 
# Detect domain-specific content, Detect image types, Detect objects
images_folder = os.path.join (os.path.dirname(os.path.abspath(__file__)), "images")

'''
END - Quickstart variables
'''


'''
Tag an Image - remote
This example returns a tag (key word) for each thing in the image.
'''
def Object_recognition (fpath):　　　　 #newly defined
    print("===== Tag an image - remote =====")
    # Call API with remote image
    tags_result_remote = computervision_client.tag_image(fpath)  #need to correct    remoteではURL(文字列)を与えるが、in_streamでは画像の中身を送る必要あり

    # Print results with confidence score
    print("Tags in the remote image: ")
    if (len(tags_result_remote.tags) == 0):
        print("No tags detected.")
    else:
        for tag in tags_result_remote.tags:
            print("'{}' with confidence {:.2f}%".format(tag.name, tag.confidence * 100))
    print()
    print("End of Computer Vision quickstart.")
'''
END - Tag an Image - remote
'''
    


#ファイルダイアログを開く
def openFile():
    fpath= fd.askopenfilename()
    if fpath:
        #画像分析
         Object_recognition(fpath)

#アプリのウィンドウを作る
root = tk.Tk() 
root.geometry("400x400")

btn = tk.Button(root, text="ファイルを開く", command = openFile)
imageLabel = tk.Label()

btn.pack()
imageLabel.pack()


