# Nutrition-Analysis-App

A modular Python GUI-based nutrition insights tool built for food data exploration and comparison. It has been designed in collaboration with `alexander-cavalliotis` and `LucasBr1624` with equal contributions (33.33% each).

## 📋 Requirements

- Python 3.13 or higher
- Required packages (automatically installed with setup instructions below):
  - `wxPython` - GUI framework
  - `matplotlib` - Data visualization
  - `pandas` - Data manipulation
  - `numpy` - Numerical operations

## 🚀 Quick Start

### Option 1: Using Virtual Environment

1. **Clone and navigate to the project:**

   ```bash
   git clone <repository-url>
   cd Nutrition-Analysis-App
   ```

2. **Create and activate virtual environment:**

   ```bash
   # Create virtual environment
   python -m venv .venv
   
   # Activate virtual environment
   # On Windows:
   .venv\Scripts\Activate.ps1
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install wxpython matplotlib pandas numpy
   ```

4. **Run the application:**

   ```bash
   python run.py
   ```

### Option 2: Using PyCharm

1. **Open the project in PyCharm:**
   - Launch **PyCharm**
   - Click on **File → Open...** and select the project folder

2. **Set up your Python interpreter:**
   - Go to **File → Settings → Project → Python Interpreter**
   - Select Python 3.13 or click the gear icon ⚙️ → **Add...** to create a new virtual environment
   - PyCharm will automatically detect and install the required packages

3. **Run the application:**
   - Locate the `run.py` file in the project explorer
   - Right-click `run.py` and select **Run**
   - The application window will open automatically

## 🎯 Features

- Interactive GUI for nutrition data analysis
- Data visualization with charts and graphs
- Food comparison tools
- Nutrition density analysis
