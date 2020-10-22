import sys
import os
if not os.path.exists('/content/MyDrive/'):
  os.mkdir('/content/MyDrive/')
print("happy") 
os.system('mount --bind /content/drive/My\ Drive /content/MyDrive')

os.system("cd /content/MyDrive")

print("hello")
# import os
# try:
#   os.mkdir('/content/MyDrive/')
# except:
#   pass
# !mount --bind /content/drive/My\ Drive /content/MyDrive
# %cd /content/MyDrive

#Fill this very Carefully

your_folder_name = 'Test_Ehsan'
profile_name_A = 'y.hiiiina'
profile_name_B = 'n_coco.y'

# Define Path

data_path = '/content/MyDrive/data/'
own_path = '/content/MyDrive/'+your_folder_name+'/'

# Make Folder in your Drive

import os
if not os.path.exists('/content/MyDrive/'+your_folder_name):
  try:
    os.mkdir('/content/MyDrive/'+your_folder_name)
  except:
    pass

print(own_path)
# os.system("cd own_path")

# Git clone 

# pip install git

if not os.path.exists('/content/MyDrive/'+your_folder_name+'/faceswap'):
   clone = "git clone https://github.com/t-qureshi/faceswap.git"
   os.system(clone) # Cloning
faceswap_path = own_path + 'faceswap'

# os.system("cd faceswap_path")
print(faceswap_path)
os.chdir(faceswap_path)

#Install Setups

# sudo apt install python3.7
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python3.7 get-pip.py
# python3.7 -m pip install -r requirements_nvidia.txt
# python3.7 -m pip install -r_requirements_base.txt
# python3.7 -m pip install face-recognition
# python3.7 setup.py
# import subprocess
# subprocess.call(['sh', '/Requirments.sh'])
os.system('bash ./Requirments.sh')

# Define paths
folder_a = data_path+profile_name_A
folder_b = data_path+profile_name_B

folder_a_faces = own_path+profile_name_A+'AND'+profile_name_B+'/Faces_of_'+profile_name_A
folder_b_faces = own_path+profile_name_A+'AND'+profile_name_B+'/Faces_of_'+profile_name_B

##Alignments
folder_a_faces_alignments = own_path+profile_name_A+'AND'+profile_name_B+'/Faces_of_'+profile_name_A+'/alignments.fsa'
folder_b_faces_alignments = own_path+profile_name_A+'AND'+profile_name_B+'/Faces_of_'+profile_name_B+'/alignments.fsa'

##Model Direcotory
model_path = own_path+profile_name_A+'AND'+profile_name_B+'/Model'



print (folder_a)
print (folder_b)
print (folder_a_faces)
print (folder_b_faces)
print (folder_a_faces_alignments)
print (folder_b_faces_alignments)
print (model_path)


if not os.path.exists(folder_a_faces_alignments):
  pass
  #python3 faceswap.py extract -i $folder_a -o $folder_a_faces -al $folder_a_faces_alignments

if not os.path.exists(folder_b_faces_alignments):
  pass
  #python3 faceswap.py extract -i $folder_b -o $folder_b_faces -al $folder_b_faces_alignments

if not os.path.exists(model_path):
  os.mkdir(model_path) 



#!python3.7 faceswap.py train \
#--input-A $folder_a_faces \
#--input-B $folder_b_faces \
#--model-dir $model_path











