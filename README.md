# 🧮 BMI Calculator (GUI + Data Analysis)

A simple yet powerful **BMI Calculator Desktop Application** built using Python.
This project provides a graphical user interface (GUI) to calculate BMI, store user data, and visualize health trends over time.

---

## 🚀 Features

* 📊 Calculate Body Mass Index (BMI)
* 🧾 Automatic BMI category classification (Underweight, Normal, Overweight, Obese)
* 💾 Store multiple user records using SQLite database
* 📜 View historical BMI records
* 📈 Visualize BMI trends using graphs
* ⚠️ Input validation and error handling
* 🖥️ Clean and user-friendly GUI

---

## 🛠️ Tech Stack

* Python
* Tkinter (for GUI)
* SQLite (for database)
* Matplotlib (for graphs)

---

## 📐 BMI Formula

BMI is calculated using the formula:

BMI = weight (kg) / height² (m²)

---

## ▶️ How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/bmi-calculator.git
   ```

2. Navigate to the project folder:

   ```bash
   cd bmi-calculator
   ```

3. Install required dependencies:

   ```bash
   pip install matplotlib
   ```

4. Run the application:

   ```bash
   python bmi_calculator.py
   ```

---

## 📸 Screenshots

(Add your screenshots here)

* GUI Interface
* BMI Result Display
* Graph Visualization

---

## 📂 Project Structure

```
BMI-Calculator/
│
├── bmi_calculator.py
├── requirements.txt
├── README.md
├── .gitignore
├── data.db
├── LICENSE
└── screenshots/

```

---

## 🧠 Design Decisions

Initially, JSON was considered for storing data. However, since the application involves handling multiple users, maintaining historical records, and performing data analysis for graphs, SQLite was chosen for its efficiency, scalability, and structured querying capabilities.

---

## ⚠️ Error Handling

* Handles invalid or empty inputs
* Prevents negative or zero values
* Displays user-friendly error messages

---

## 🌱 Future Improvements

* User authentication system
* Export reports (PDF/CSV)
* Improved UI using CustomTkinter
* Health suggestions based on BMI
* Cloud data storage

---

## 🙌 Acknowledgement

This project was developed as part of academic learning to apply concepts of GUI development, data handling, and visualization in Python.

---

## 📌 Author

Sarthak Jindal

---

## License

This project is licensed under the MIT License.

---

⭐ If you found this project useful, feel free to star the repository!
