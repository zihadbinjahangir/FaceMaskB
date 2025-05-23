# 🎨 Mask Predictor Frontend (Streamlit)

This is the frontend of the Polygon Predictor app, built with Streamlit. It allows users to upload an image, sends it to the FastAPI backend, and displays the predicted polygon-masked result.

---

## 📁 Structure

```
frontend/
├── app.py         # Streamlit web app
```

---

## 🚀 How to Run

1. Install Streamlit and dependencies:

```bash
pip install -r requirements.txt
```

2. Start the frontend app:

```bash
streamlit run frontend/app.py
```

---

## 🔗 Notes

- Make sure the backend is running and accessible.
- Update the backend URL in `app.py` from:

```python
response = requests.post("http://localhost:8000/predict/", ...)
```

to:

```python
response = requests.post("https://your-backend-service.onrender.com/predict/", ...)
```

- Replace `your-backend-service` with your actual Render backend URL.

---

## 💡 Features

- Upload `.jpg`, `.png`, or `.jpeg` images.
- Visual side-by-side display of original and predicted mask.
- Clean and simple UI using Streamlit.

---
