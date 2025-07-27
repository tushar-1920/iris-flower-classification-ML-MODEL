# Iris Flower Classification using Naive Bayes

This project implements a simple **Naive Bayes Classifier** to predict the species of Iris flowers based on sepal and petal measurements. The model is trained using the famous **Iris dataset** and built with Python and scikit-learn.

## 📊 Dataset

The dataset used is a version of the Iris dataset in Excel format (`iris-train.xlsx`), which includes:

- Sepal length (cm)
- Sepal width (cm)
- Petal length (cm)
- Petal width (cm)
- Species (target label)

## 🧠 Model

The model is trained using the **Gaussian Naive Bayes** algorithm from the `sklearn.naive_bayes` module.

### Sample Prediction:
```python
model.predict([[5.4, 3.0, 4.5, 1.5]])
