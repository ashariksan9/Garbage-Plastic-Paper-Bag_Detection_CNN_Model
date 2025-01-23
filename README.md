# 🛍️ Bags Classification Project

## 📚 Objective

This project aims to create a machine learning model using **computer vision** to classify images of:
- 🛍️ Plastic bags
- 📦 Paper bags
- 🗑️ Garbage bags

The goal is to help improve waste segregation in society, addressing low recycling rates and reducing the environmental impact of mixed waste disposal.

---

## 🚨 The Problem

🔍 **Why is this important?**
- Jakarta faces a **waste emergency** with most trash ending up in landfills, causing environmental pollution and health risks.
- Proper waste segregation could significantly reduce landfill contributions and promote recycling.

🌍 **References:**
- [Darurat Sampah Jakarta](https://megapolitan.kompas.com/read/2024/03/31/10584731/jakarta-darurat-sampah-pengamat-minta-pembangunan-itf-sunter-dilanjut)
- [Pentingnya Daur Ulang Sampah](https://communication.binus.ac.id/2023/12/13/pentingnya-daur-ulang-sampah-bagi-masa-depan-lingkungan-yang-lebih-baik/)
- [Plastic and Pollution](https://repurpose-global.translate.goog/blog/post/how-does-plastic-cause-air-pollution?_x_tr_sl=en&_x_tr_tl=id&_x_tr_hl=id&_x_tr_pto=tc)

---

## 🎯 Project Highlights

### 🔍 Exploratory Data Analysis (EDA)
- Dataset contains **1,500 images** evenly distributed across 3 classes.
- **Characteristics**:
  - Plastic bags: Varied colors, always have 2 handles.
  - Paper bags: Brown, rectangular.
  - Garbage bags: Black, semi-oval shapes.
- Dataset format: **RGB colorspace**.

### 🧠 Model Performance
1. Initial model:
   - Achieved **85% accuracy** on the test set.
2. Improvement using **VGG16 (Transfer Learning)**:
   - Accuracy increased to **93%**.

---

## 🔢 Dataset
- **Name**: Bags Dataset
- **Source**: Custom (scraped or open dataset)
- **Structure**:
  - Plastic bags: 500 images
  - Paper bags: 500 images
  - Garbage bags: 500 images

---

## ⚙️ Methodology
1. **Model Architecture**:
   - Baseline: Custom ANN model.
   - Improved: Transfer Learning with VGG16.
2. **Training**:
   - Augmented data to improve generalization.
   - Tested multiple hyperparameters for optimization.
3. **Evaluation**:
   - Used metrics like **accuracy** and visualized model performance.

---

## 🛠️ Tech Stack
- **Framework**: TensorFlow
- **Languages**: Python
- **Libraries**: Matplotlib, Seaborn, OpenCV

---

## 📁 File Descriptions
- `P2G7_<name>.ipynb`: Main notebook for model training and evaluation.
- `P2G7_<name>_inference.ipynb`: Notebook for inference on new data.
- `deployment/`: Contains deployment-related files.
  - `app.py`: Main application.
  - `requirements.txt`: Dependencies.
- `url.txt`: Links to dataset, model, and deployment.

---

## 🌟 Strengths & Weaknesses

### ✅ Strengths
- Balanced dataset ensures fair training.
- High accuracy (93%) using transfer learning.
- Clear class characteristics improve interpretability.

### ❌ Weaknesses
- Dataset images are synthetic, risking overfitting.
- Limited dataset size; adding real images could enhance performance.

---

## 🔗 Useful Links
- **Dataset**: https://www.kaggle.com/datasets/vencerlanz09/plastic-paper-garbage-bag-synthetic-images
- **Deployment**: https://huggingface.co/spaces/ashariksan9/model_cnn_deteksi_bags 

---

## ✨ Conclusion

Key takeaways:
- Transfer Learning significantly improved performance.
- Augmentation helped model generalize better.
- Further improvements could involve expanding the dataset with real-world images and fine-tuning hyperparameters.

---

## 📬 Get in Touch

Feel free to reach out!
- 💼 Linkedin: www.linkedin.com/in/muhammadasharihsan
- 📧 Email: ashar4iksan@gmail.com
