# BLISEEN 
The main purpose of this project is to provide an aiding tool for the blind and visually impaired people. The tool will help them connect to their surrounding environment. A mobile app will be built that captures photos of the person's surroundings, performs image analysis to provide a scene description in text. In a later stage, the text is converted into audible speech, to allow the user to hear it.

 A scene description mobile application using machine learning’s semantic segmentation algorithm applying it with FCN16 and finetuned VGG16 (keras on TensorFlow) with python as backend and deployed with flask
 
The chosen neural network is a fully convolution neural network(FCN) a fine-tuneded VGG16 as backbone
 
The model was a fine-tuned VGG16 where the fully connected layers were removed where the first part uses a similar architecture of the CNN architecture for the feature extraction and by removing the flatten layer or fully connected layers and reconstructing the image using skip connection the image is reconstructed again but in the a complete high-resolution image in which all the pixels are classified.

# Deployment
using flask framework to deploy the model to a flutter mobil application as the image needed processing and to exctracting the lables from it 

Dataset: cityscapes
