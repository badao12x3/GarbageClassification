from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing import image


root = Tk()
root.geometry('700x500')
root.resizable(width=0, height=0)
root.title("Phân loại rác thải")

myLabel = Label(root, image=None)
myLabel.pack(pady=30)

myResult = Label(root, text=None, fg="#000", font=('Times', 16))
myResult.pack(side=BOTTOM, padx=20, pady=30)

resultPredict = ""

model=keras.models.load_model("vgg16.h5")
class_names = ["battery", "biological", "brown-glass", "cardboard", "clothes", "green-glass", "metal", "paper", "plastic", "shoes", "trash", "white-glass"]


def chooseImage():
    global myLabel
    global path
    path = filedialog.askopenfilename(
        filetypes=[("Image File", '.jpg', '.png')])
    if path:
        image = Image.open(path).resize([400, 300])
        tkimage = ImageTk.PhotoImage(image)
        myLabel.config(image=tkimage)
        myLabel.image = tkimage
    predict(path)


def resultImage(resultPredict):
    global myResult
    if path:
        myText = resultPredict
        myResult.config(text=myText, fg="blue")
        myResult.text = myText
    


def predict(path) :
    print(path)
    resultPredict = ""
    image2 = tf.keras.preprocessing.image.load_img(path)
    image1 = image2.resize([224,224])
    img_tensor = tf.keras.preprocessing.image.img_to_array(image1)
    img_tensor = np.array([img_tensor])     
    x=model.predict(img_tensor)
    if (int(100*np.max(x))) < 70 :
      sort_x= np.argsort(x)[::-1]
    #   print(x[0][sort_x[0][11]])
      resultPredict = resultPredict +"Predict: "+class_names[sort_x[0][11]]+" với tỉ lệ "+str(int(100*x[0][sort_x[0][11]]))+'%' +"\nPredict: "+class_names[sort_x[0][10]]+" với tỉ lệ "+str(int(100*x[0][sort_x[0][10]]))+'%'+"\nPredict: "+class_names[sort_x[0][9]]+" với tỉ lệ "+str(int(100*x[0][sort_x[0][9]]))+'%'
    else: resultPredict = resultPredict + "Predict: "+class_names[np.argmax(x)]+" Prob: "+str(int(100*np.max(x)))+'%' # so sánh kết quả  dự đoán và nhãn của ảnh
    # resultPredict = resultPredict + " Predict: "+class_names[np.argmax(x)]+" Prob: "+str(int(100*np.max(x)))+'%'
    resultImage(resultPredict)

chooseImageButton = Button(
    root, text="CHỌN ẢNH", command=chooseImage, pady=5, padx=30, borderwidth=4
).place(x=280, y=350)

root.mainloop()
