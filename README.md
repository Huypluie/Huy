# Huy - DR - blindness detection
DR - blindness detection (Bệnh Võng Mạc Tiểu Đường)
<img width="703" height="190" alt="image" src="https://github.com/user-attachments/assets/675ced4b-492f-48b5-b2dd-fc95073d2e61" />  
Dataset APTOS2019: https://www.kaggle.com/competitions/aptos2019-blindness-detection/data  
Preprocess: GaussianBlur + CLAHE G (299,299)  
Model: Resnet50+CBAM block  
### Objective

The goal of this project is to **classify diabetic retinopathy into 5 severity levels** based on retinal fundus images:

- **0** → No DR  
- **1** → Mild DR  
- **2** → Moderate DR  
- **3** → Severe DR  
- **4** → Proliferative DR  

### Evaluation Metric

The performance of the model is evaluated using **Quadratic Weighted Kappa (QWK)**.  

QWK is a statistical measure of agreement between predicted labels and ground-truth labels, adjusted for the possibility of agreement occurring by chance.  
Unlike simple accuracy, QWK considers the **ordinal relationship** between classes, meaning that misclassifying a sample into a far-away class (e.g., predicting 0 → 4) is penalized more heavily than misclassifying into a nearby class (e.g., 2 → 3).  

This makes QWK a more suitable metric for **diabetic retinopathy detection**, where the disease stages are ordered and the severity of misclassification matters.
## Results

The model was trained on the APTOS2019 dataset and evaluated using **Quadratic Weighted Kappa (QWK)**, the official competition metric.  

### Validation Set Performance
- **Optimized QWK:** `0.8804`  
- **Accuracy:** `0.70`

### Test Set Performance (APTOS2019 official test split)
- **Optimized QWK:** `0.8518`  
- **Accuracy:** `0.69`  
---

📌 **Observation:**  
- The model achieves strong performance on **Normal** and **Moderate** classes.  
- Performance drops for **Severe** and **Proliferative** classes due to **class imbalance**.  
- Overall, the QWK score shows the model aligns well with clinical grading trends.
