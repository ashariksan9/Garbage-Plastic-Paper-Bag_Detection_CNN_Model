import streamlit as st
from PIL import Image
import numpy as np
from keras.preprocessing.image import load_img, img_to_array 
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.vgg16 import preprocess_input

# load model
model = load_model('model_terbaiks.h5')

with open('classes.txt', 'r') as file:
    class_names = [line.strip() for line in file]

def app():
    # deskripsi model
    st.write('''
    # **Model CNN Deteksi Garbage, Plastic, Paper Bag**
    - Model ini digunakan untuk melihat klasifikasi antara Garbage Bag, Plastic Bag, Paper Bag.
    - Model ini menggunakan VGG16 untuk improve hasil akurasi dari model.
    - Model ini mendapatkan accuracy score hingga 0.93 pada test set dalam mendeteksi Garbage Bag, Plastic Bag, Paper Bag.
    ''')
    
    st.divider()
    
    # upload file
    input_file = st.file_uploader("Upload gambar yang ingin dianalisa!", type=["jpg", "jpeg", "png"])

    # display gambar
    if input_file is not None:
        image = Image.open(input_file) 
        image = image.resize((224, 224))  
        st.image(image, caption='Gambar yang di Upload', use_column_width=True)
    else:
        st.write("Upload gambar dulu bro.")

    st.divider()

    # predict
    if st.button("Classify Gambar"):
        if input_file is not None:
            # Read dan preprocess image
            img = load_img(input_file, target_size=(224, 224)) 
            img_array = img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)

            # masukkan image ke  model
            classes = model.predict(img_array)
            class_idx = np.argmax(classes, axis=-1)

            # display result di center
            st.write('<h1 style="text-align: center"> Predicted Class:<br> {}'.format(class_names[class_idx[0]]), unsafe_allow_html=True)  
    
        else:
            st.error("Silahkan Upload Gambar Dahulu.")
        
if __name__ == '__main__':
  app()
