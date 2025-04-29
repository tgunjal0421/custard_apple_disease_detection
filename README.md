
# 🍏 Custard Apple Disease Detection

This project is a **web-based application using Django** that predicts diseases in custard apple leaves using a trained deep learning model. The goal is to help farmers and agricultural enthusiasts detect diseases early and take corrective action.


## 🚀 Features

- **Upload Image:** Users can upload images of custard apple leaves for disease detection.
- **Disease Prediction:** Identifies diseases such as Anthracnose, Diplodia Rot, and more.
- **Prediction Confidence:** Displays the model’s confidence percentage for each prediction.
- **Prediction History:** Stores uploaded images along with predictions for user reference.
- **User Authentication:** Enables secure access with login and signup functionality.
- **Interactive Frontend:** Built with Bootstrap for responsive design and a great user experience.


## 🖥️ Technologies Used

- **Frontend:** HTML, CSS, Bootstrap  
- **Backend:** Django Framework  
- **Deep Learning:** TensorFlow/Keras  
- **Database:** SQLite  
- **Version Control:** GitHub  


## 📸 Screenshots  
 ![image](https://github.com/user-attachments/assets/de1de3a3-06e4-4ce8-b243-3ab3377e8115)
Fig. Result output of Proposed Model

![image](https://github.com/user-attachments/assets/6b21599f-71eb-4e19-9a49-29d3a4ae8271)
Fig. Web Application features and Their Outcomes


## 🛠️ Installation and Setup

Follow these steps to set up the project locally:

1. **Clone the repository:**  
   ```
   git clone https://github.com/yourusername/custard_disease_detection.git
   cd custard_disease_detection
   ```

2. **Set up a virtual environment (optional but recommended):**  
   ```
   python -m venv myvenv
   source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
   ```

3. **Install dependencies:**  
   ```
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**  
   ```
   python manage.py migrate
   ```

5. **Run the development server:**  
   ```
   python manage.py runserver
   ```

6. **Access the application:** Open your browser and go to:  
   ```
   http://127.0.0.1:8000/
   ```


## 🧪 Usage

1. **Register or log in** to your account.
2. Navigate to the **"Upload Image"** section and upload a leaf image.
3. View the **disease prediction result** along with the confidence level.
4. Check **prediction history** for previously uploaded images.


## 🏆 Future Enhancements

- **Visualization of Model Metrics:** Display accuracy, precision, recall, etc.
- **Add More Diseases:** Train the model with additional diseases.
- **Multi-language Support:** Expand for users from different regions.
- **Mobile-Friendly Design:** Improve the UI for smaller screens.


## 🤝 Contributing

Feel free to fork the repository and submit pull requests. All contributions are welcome!


### 📧 Contact

If you have any questions, feel free to reach out at **tanvigunjal22@gmail.com**.
