# Gauss-Jordan Elimination Calculator

A fully interactive web application that solves systems of linear equations using the Gauss-Jordan elimination method. Built with Flask (Python backend) and HTML/CSS/JavaScript (frontend), deployed on Vercel.

## Live Demo

🔗 **https://gauss-jordan-hub.vercel.app**

## Features

- **Mathematical Discussion** — Clear explanation of Gauss-Jordan elimination and elementary row operations
- **Two Worked Examples** — Step-by-step solutions for 2×2 and 3×3 systems with all intermediate matrices shown
- **Interactive Calculator** — Dynamic matrix sizing (1-6 rows, 2-7 columns) with a customizable input grid
- **Step-by-Step Results** — Each elimination step is displayed with proper LaTeX matrix formatting
- **Export Functionality** — Download the complete solution steps as a .txt file
- **Responsive Design** — Works on desktop, tablet, and mobile devices

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.9+ with Flask |
| Frontend | HTML5, CSS3 (Tailwind CSS), JavaScript |
| Math Rendering | MathJax (LaTeX to formatted math) |
| Deployment | Vercel (Serverless Python Runtime) |
| Version Control | Git + GitHub |

## Project Structure
gauss-jordan-hub/
├── app.py # Flask application (routes & request handling)
├── gauss_jordan.py # Gauss-Jordan elimination algorithm (manual implementation)
├── requirements.txt # Python dependencies
├── vercel.json # Vercel deployment configuration
├── .gitignore # Git ignore rules
├── README.md # Project documentation
└── templates/
└── index.html # Frontend (HTML, CSS, JavaScript, MathJax)

## Installation (Local Development)

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ranielqt/gauss-jordan-hub.git
   cd gauss-jordan-hub

   # Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
python app.py
