# 📊 DataPulse: Real-Time CDC Dashboard Demo

DataPulse is a Streamlit-based real-time dashboard simulating a Change Data Capture (CDC) pipeline. It allows users to simulate new sales events and visualize sales data trends dynamically—ideal for showcasing how real-time ETL dashboards can be built using modern Python tools.

---

## ✨ Features

- 🧪 Simulated CDC pipeline with SQLite (mimicking PostgreSQL CDC or Snowflake)
- 📈 Real-time dashboard: product revenue, daily sales trends, product share
- 🧾 Interactive filters and download to CSV
- 👤 Multi-user login using `streamlit-authenticator`
- 🔒 Credentialed access with hashed passwords (configurable via `credentials.yaml`)
![{1D3A4394-1084-4812-8204-B1557FC12705}](https://github.com/user-attachments/assets/e72c2403-2281-4de8-85da-ba57359ded15)
![{B8F1970A-7168-49ED-84D0-361CDA26A9CD}](https://github.com/user-attachments/assets/be0ee29e-4f98-467d-a4b5-c585f8d69209)
![{0AD6DBE1-6A2B-463F-A839-E0FFA14F5003}](https://github.com/user-attachments/assets/d7587446-9edf-4415-8f37-591b65b68235)

---

## 🛠 Tech Stack

- Streamlit
- SQLite via SQLAlchemy
- Plotly for data visualization
- Pandas
- streamlit-authenticator for login/auth
- YAML-based credential system

---

## 📁 Folder Structure

```
DataPulse/
│
├── app.py                         # Main Streamlit app
├── generate_hash.py              # Helper to generate hashed passwords
│
├── data/
│   └── dummy_source.sqlite       # SQLite source database
│
├── utils/
│   ├── db.py                     # Database access functions
│   └── cdc_simulator.py          # Simulate CDC sale events
│
├── config/
│   └── credentials.yaml          # Authentication users config
│
├── .streamlit/
│   └── config.toml               # UI theme
```
