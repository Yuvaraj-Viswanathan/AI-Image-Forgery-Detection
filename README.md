# 🔍 AI Image Forgery Detection Tool (ELA + ResNet50)

This project detects manipulated or AI-generated images using **Error Level Analysis (ELA)** and a **Convolutional Neural Network (ResNet50)**. It includes a **Streamlit web app** that allows users to upload images and instantly check if they are real or fake.

> 📘  Independent AI Research Project | MIT Campus, Anna University  
> 🧑‍💻 Author: Yuvaraj V (2022504554)  
> 📄 [Download Full Report](./ai_forgery_report.pdf)

---

## 🧠 What is ELA?

**Error Level Analysis (ELA)** reveals tampered regions in an image by detecting differences in JPEG compression. Real images have uniform error levels. Manipulated parts stand out due to inconsistent compression artifacts.

---

## 🚀 Features

- 📤 Upload `.jpg`, `.jpeg`, or `.png` images
- 🔬 ELA preprocessing for manipulation detection
- 🧠 ResNet50-based deep learning model
- ✅ Real-time prediction with confidence score
- 🌐 Streamlit-powered web app

---

## 🖼️ How It Works

1. **User Uploads an Image**
2. **ELA Preprocessing** (via `resize_ela.py`)
3. **Model Prediction** (via trained `ela_model.h5`)
4. **Output**: Real or Fake + Confidence %

---

## 🛠️ Tech Stack

| Tool         | Purpose                          |
|--------------|----------------------------------|
| Python 3.10  | Main language                    |
| Streamlit    | Web interface                    |
| TensorFlow   | Model training + prediction      |
| ResNet50     | Feature extraction (transfer learning) |
| OpenCV, PIL  | Image processing                 |

---

## 📁 Project Structure
```
ai-image-forgery-detector/
├── app.py # Streamlit app
├── resize_ela.py # ELA conversion logic
├── train_model.py # Model training script
├── models/
│ └── ela_model.h5 # Trained model
├── images/
│ ├── real1.jpg, fake1.jpg # Sample images
├── ela_images/
│ └── real_1_ELA.jpg, fake_1_ELA.jpg # ELA outputs
├── ai_forgery_report.pdf # Final report
├── requirements.txt
└── README.md
```


---

## 🧪 How It Works

1. **ELA Conversion**  
   `resize_ela.py` simulates JPEG compression, finds the difference (error), and enhances contrast.

2. **Model Training**  
   `train_model.py` loads all ELA images, labels them based on filenames (`real` or `fake`), and trains a CNN using ResNet50.

3. **Prediction App**  
   `app.py` takes user-uploaded images, ELA-processes them, and makes predictions via the trained model.

---

## ⚙️ Technologies Used

- Python 3
- Streamlit
- TensorFlow / Keras
- PIL (Pillow)
- OpenCV
- ResNet50 (pretrained on ImageNet)

---

## ▶️ Run the App

```bash
# Install requirements
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
```
