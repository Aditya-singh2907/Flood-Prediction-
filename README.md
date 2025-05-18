# Flood Prediction Website

A machine learning-powered web application that predicts the likelihood of a flood in a specific city based on real-time weather data. Designed with simplicity and accuracy in mind, this tool helps users, authorities, and organizations take precautionary measures during uncertain weather conditions.



## 🌍 About the Project

Floods are one of the most frequent and devastating natural disasters, especially in regions with erratic weather patterns and inadequate infrastructure. This project aims to serve as a predictive early-warning tool by utilizing weather data to forecast flood risk using a trained machine learning model.

The goal is to build a lightweight and user-friendly platform that can:
- Monitor real-time weather conditions
- Analyze critical meteorological factors
- Predict flood risks with high accuracy
- Provide actionable insights to users in affected regions

This project is ideal for academic research, smart city applications, and early disaster warning systems.



## 🌟 Features

- **High-Accuracy Predictions**  
  Trained on a balanced dataset with over 5,000 records, achieving a 99% accuracy rate on test data using a Random Forest Classifier.

- **Live Weather Integration**  
  Integrates with the [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api) to pull current temperature, humidity, wind speed, precipitation, and more.

- **Clean UI**  
  Responsive, intuitive frontend designed with basic HTML, CSS, and JS for a fast and accessible user experience.

- **200+ City Search Capability**  
  Users can input a city name, which is matched to a built-in dataset of over 200 city coordinates for live weather prediction.

- **Result Transparency**  
  Shows both the prediction label ("Flood" or "No Flood") and the model’s confidence as a percentage.



## 🛠️ Technical Details

### Machine Learning Model:

- **Algorithm**: Random Forest Classifier  
- **Training Dataset Size**: 5,000+ samples  
- **Important Features**:
  - Temperature  
  - Max Temperature  
  - Wind Speed  
  - Cloud Cover  
  - Precipitation  
  - Humidity  
- **Performance**:
  - Training Accuracy: 98.61%  
  - Testing Accuracy: 99%

### Backend & Logic:

- Built using **Flask** to create REST endpoints for prediction and API communication.
- Uses **joblib** to load the trained ML model.
- Handles API calls to fetch weather data dynamically based on user input.

### Libraries & Dependencies:

- `pandas==2.2.3`  
- `numpy==2.2.6`  
- `matplotlib==3.7.2`  
- `seaborn==0.12.2`  
- `scikit-learn==1.6.1`  
- `imbalanced-learn==0.10.1`  
- `joblib==1.3.2`  
- `flask==3.1.1`
  



## ⚙️ How It Works

1. User enters the name of a city.
2. The system fetches real-time weather data using the Visual Crossing API.
3. Selected weather parameters are passed into the pre-trained Random Forest model.
4. The model predicts the probability of a flood.
5. The result is displayed to the user along with a confidence score.



## 📜 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute it for personal or commercial purposes. See the `LICENSE` file for more information.



## ❤️ Acknowledgements

- [Visual Crossing Weather API](https://www.visualcrossing.com/weather-api) for real-time weather data  
- Open-source community for supporting the ML tools and libraries used  
- Academic mentors and peers who provided feedback during development

