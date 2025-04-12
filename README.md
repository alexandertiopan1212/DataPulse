# 📊 DataPulse: Real-Time CDC Dashboard Demo

DataPulse is a Streamlit-based real-time dashboard simulating a Change Data Capture (CDC) pipeline. It allows users to simulate new sales events and visualize sales data trends dynamically—ideal for showcasing how real-time ETL dashboards can be built using modern Python tools.

---

## ✨ Features

- 🧪 Simulated CDC pipeline with SQLite (mimicking PostgreSQL CDC or Snowflake)
- 📈 Real-time dashboard: product revenue, daily sales trends, product share
- 🧾 Interactive filters and download to CSV
- 👤 Multi-user login using `streamlit-authenticator`
- 🔒 Credentialed access with hashed passwords (configurable via `credentials.yaml`)

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
