Here’s a **minimal README.md** that matches exactly what you asked for — simple steps: install Conda, install requirements, then run the app.

```markdown
# Ultralytics Gradio App

A simple Gradio interface for running YOLO object detection with Ultralytics.

---

## 🚀 Setup

### 1. Install Conda
Download and install [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/download).

---

### 2. Create and activate environment
```bash
conda create -n oral-disease-api python=3.9 -y
conda activate oral-disease-api
```

---

### 3. Install requirements
```bash
pip install -r requirements.txt
```

---

### 4. Run the app
```bash
python main.py
```

Gradio will start a local server. Open the link shown in the terminal (usually `http://127.0.0.1:7860`) in your browser.

---

## 📂 Project files
- `main.py` → Gradio interface script  
- `requirements.txt` → Dependencies (`ultralytics`, `gradio`, `pillow`)  
- `best.pt` → YOLO model weights (place your trained weights here)  

```

---

This is the simplest workflow: Conda for environment management, pip for installing from `requirements.txt`, then run `main.py`.  

Would you like me to also generate a **ready‑to‑use requirements.txt** with pinned versions for `ultralytics`, `gradio`, and `pillow` so you don’t have to check them manually?
