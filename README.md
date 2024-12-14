# 🏠 House Price Prediction with Random Forest
![House Price Banner](https://github.com/user-attachments/assets/ec728e93-4e92-40e6-8b81-add3f0273004)

### 📋 **Project Overview**
Proyek ini bertujuan untuk memprediksi harga rumah berdasarkan data historis dan berbagai fitur penting. Prediksi ini diharapkan dapat membantu pengambilan keputusan dalam industri properti, seperti menentukan harga jual/beli rumah dengan lebih akurat.

**Dataset**: [Kaggle House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)

---

## 🚀 Workflow Overview

### 1️⃣ **Business Understanding**
Industri properti membutuhkan model prediksi yang akurat untuk:
- Menentukan harga rumah yang wajar sesuai pasar.
- Membantu pengembang dan agen properti membuat keputusan berbasis data.
- Mengidentifikasi fitur utama yang memengaruhi harga rumah.

**Objective**: Memprediksi harga rumah menggunakan dataset dan metode machine learning.

---

### 2️⃣ **Data Understanding**
**Dataset**: Dataset berisi 79 fitur deskriptif dan harga target (SalePrice) untuk 1.460 rumah. Beberapa kategori fitur meliputi:
- **Lokasi**: Neighborhood, LotArea.
- **Fitur fisik**: OverallQual, TotalBsmtSF, GarageArea.
- **Tahun konstruksi**: YearBuilt, YearRemodAdd.
  
**Eksplorasi Data**:
- Distribusi harga rumah (SalePrice).
- Korelasi antar fitur dengan target.
- Identifikasi missing values, outliers, dan distribusi data.

---

### 3️⃣ **Data Preparation**
**Langkah-langkah utama**:
- **Handling Missing Values**:
  - Mengisi nilai yang hilang berdasarkan median, modus, atau domain expertise.
- **Feature Engineering**:
  - Transformasi variabel kategorikal menggunakan One-Hot Encoding.
  - Membuat fitur baru seperti `TotalSF = TotalBsmtSF + 1stFlrSF + 2ndFlrSF`.
- **Data Normalization**:
  - Scaling fitur numerik agar setara.
- **Outlier Treatment**:
  - Menghapus atau membatasi nilai ekstrim pada fitur numerik.

---

### 4️⃣ **Modeling**
**Model**: Random Forest Regressor
- **Alasan Pemilihan**:
  - Mengurangi risiko overfitting dengan ensemble learning.
  - Menangani data kompleks dan non-linear.
  - Memberikan hasil robust meskipun terdapat variasi dalam data.

---

### 5️⃣ **Model Evaluation**
**Metode Evaluasi**:
- Mean Absolute Error (MAE): Mengukur rata-rata kesalahan absolut.
- Root Mean Squared Error (RMSE): Penalti lebih besar pada kesalahan besar.
- R² Score: Menunjukkan proporsi variasi target yang dapat dijelaskan oleh model.

Visualisasi evaluasi:
- **Feature Importance**: Menunjukkan fitur-fitur utama yang memengaruhi harga.
- **Actual vs Predicted**: Membandingkan nilai aktual dengan prediksi.

---

### **Deployment**

![WhatsApp Image 2024-12-14 at 10 52 07_47644e65](https://github.com/user-attachments/assets/9671c4b3-29d3-48ec-b4d7-9c9284ae8e4b)

Halaman web ini merupakan implementasi sistem Prediksi Harga Rumah yang memungkinkan pengguna untuk memperkirakan harga rumah berdasarkan detail yang dimasukkan. 
Pengguna diminta untuk mengisi sejumlah informasi seperti kualitas rumah (OverallQual), luas area tinggal (GrLivArea), jumlah mobil di garasi (GarageCars), luas basement (TotalBsmtSF), jumlah kamar mandi (FullBath), hingga tahun pembangunan dan renovasi. 
