# 🏫 Campus Crowd Predictor

A lightweight Python tool that predicts how busy campus facilities are at any given day and time — helping students avoid crowded spots and plan their visits smarter.

---

## 📌 Problem Statement

Students often walk to the gym, library, or cafeteria only to find them packed. There's no easy way to know in advance how crowded a facility will be. This project solves that by using historical footfall patterns to predict crowd levels before you leave your room.

---

## 🚀 Features

- Generates synthetic historical footfall data for three campus facilities
- Predicts crowd status (Empty / Moderate / Crowded) for any facility, day, and time
- Accounts for facility operating hours and weekend patterns
- Simple command-line interface — no setup beyond Python

---

## 🏗️ Project Structure

```
campus-crowd-predictor/
│
├── generate_data.py   # Generates the historical dataset (dataset.csv)
├── predictor.py       # Loads data and runs crowd predictions
└── dataset.csv        # Auto-generated after running generate_data.py
```

---

## ⚙️ Setup & Installation

**Requirements:** Python 3.x (no external libraries needed)

1. Download the project:
   - Go to the GitHub repository page
   - Click **Code → Download ZIP** and extract it to a folder on your computer

2. Generate the dataset:
   ```bash
   python generate_data.py
   ```
   This creates `dataset.csv` with 90 days of simulated footfall data.

3. Run the predictor:
   ```bash
   python predictor.py
   ```

---

## 🖥️ Usage

After running `predictor.py`, you'll be prompted to enter:

```
--- Campus Crowd Predictor ---
Enter facility (Gym, Library, Cafeteria): Gym
Enter day (e.g. Monday): Friday
Enter time (e.g. 14:00): 18:00

Calculating...
Status: Crowded
Average people: 74.3
------------------------------
```

### Supported Facilities & Hours

| Facility   | Operating Hours     |
|------------|---------------------|
| Gym        | 04:00 – 23:00       |
| Library    | 08:00 – 22:00       |
| Cafeteria  | 10:00 – 01:00 (+1)  |

### Input Format

- **Facility:** `Gym`, `Library`, or `Cafeteria` (case-insensitive)
- **Day:** Full day name, e.g. `Monday`, `Saturday`
- **Time:** 24-hour format on the hour, e.g. `09:00`, `17:00`

---

## 🧠 How It Works

1. **Data Generation (`generate_data.py`):** Simulates 90 days of crowd data with realistic patterns — morning rushes at the library, evening peaks at the gym, and lighter weekends.

2. **Prediction (`predictor.py`):** For a given facility + day + time, it averages all historical headcounts from matching records and classifies the result:
   - **Empty** → fewer than 25 people
   - **Moderate** → 25–59 people
   - **Crowded** → 60 or more people

---

## 📄 License

This project was built as a BYOP capstone submission. Feel free to fork and adapt it for your own campus.
