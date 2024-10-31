import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image


def app():
    # title
    st.title('*Model CNN Deteksi Garbage, Plastic, Paper Bag*')

    # subheader
    st.subheader('Exploratory Data Analysis (EDA) dari Model')

    # add image
    image = Image.open('class_sampah.jpg')
    st.image(image, caption = 'Klasifikasi Sampah')

    st.markdown('----')

    # show dataframe
    img_df = pd.read_csv('img_df.csv')
    st.dataframe(img_df)
        
    # buat penjelasan dataset
    st.write('#### Penjelasan Dataset')
    st.write('''
    - **images**: merupakan file path dari gambar.
    - **Label**: Mewakili class gambar. Ada 3 kelas dalam kumpulan data ini: PlasticBag, PaperBag, dan GarbageBag.
    ''')

    st.markdown('----')

    # cek balance label
    st.write('#### Cek Jumlah Tiap Label')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(img_df['label'])
    plt.title('Label Count')
    plt.xlabel('Label')
    plt.ylabel('Count')
    st.pyplot(fig) 
    st.write('''
    - Diatas kita dapat melihat bahwa kelas-kelas tersebut balance. Hal ini bagus karena kita tidak perlu melakukan handling class balancing.
     ''')
    
    st.markdown('----')

    # cek karakteristik
    st.write('#### Cek Karakteristik Tiap Gambar')
    st.image('cek_gambar.png', caption='Karakteristik Gambar')
    st.write('''
    Dari gambar acak di atas, kita dapat melihat beberapa karakteristik gambar untuk setiap kelas:
    - PaperBag: Gambar sebagian besar berwarna cokelat dan berbentuk persegi panjang. Posisi gambar sangat acak. Beberapa gambar diputar dan beberapa tidak. Beberapa gambar juga dibalik secara horizontal dan vertikal.
    - PlasticBag: Gambar sebagian besar memiliki warna yang bervariasi (biru, putih, merah, dll.) dan juga berbentuk persegi panjang tetapi memiliki sedikit pegangan untuk dipegang. Posisi gambar sangat acak. Beberapa gambar diputar dan beberapa tidak. Beberapa gambar juga dibalik secara horizontal dan vertikal.
    - GarbageBag: Gambar sebagian besar berwarna hitam dan berbentuk lebih bulat dibandingkan dengan kelas lainnya. Posisi gambar sangat acak. Beberapa gambar diputar dan beberapa tidak. Beberapa gambar juga dibalik secara horizontal dan vertikal.
    ''')

    st.markdown('----')

    st.write('#### Cek Colorspace Gambar')
    st.image('rgb_cuy.png', caption='Cek Colorspace Gambar')
    st.write('''
    - Karena gambar berhasil menampilkan warna dengan benar sesuai dengan channel yang ditentukan, maka dapat disimpulkan bahwa colorspace gambar tersebut memang merupakan RGB.
    ''')


if __name__ == '__main__':
    app()


