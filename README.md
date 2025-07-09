🏥 Health Data Pipeline with Streamlit Dashboard
This is a personal data engineering project that demonstrates a complete mini data pipeline — from ingesting a large CSV file, storing it in a SQLite database, and visualizing the data through an interactive Streamlit dashboard.

✅ Built during my learning journey as a Data Engineer after working at Walmart.

📁 Project Structure
health-data-pipeline/
├── data/
│   └── health_data_large.csv        # Source data (uploaded manually)
├── scripts/
│   ├── ingest_data.py               # ETL script to load CSV into SQLite DB
│   └── dashboard.py                 # Streamlit app for data visualization
├── health.db                        # SQLite database (generated after ETL)
├── README.md                        # Project documentation

⚙️ Tech Stack
Python 3
Pandas
SQLite3
Streamlit
Git & GitHub

🚀 How to Run the Project
1. Clone the Repository
git clone https://github.com/p0d04x5/health-data-pipeline.git
cd health-data-pipeline
2. Install Dependencies
pip install pandas streamlit
3. Ingest the Data
python scripts/ingest_data.py
✅ This will read the CSV file and create the health.db SQLite database.

4. Launch the Streamlit Dashboard
streamlit run scripts/dashboard.py
📍 Then open the link shown in your terminal (usually http://localhost:8501) to view the dashboard.

📊 Dashboard Features
✅ Total record summary
✅ Gender-wise distribution
✅ Age group analysis
✅ Condition frequency
✅ Interactive filtering options

## 📸 Dashboard Preview
<img src="screenshots/dashboard_part1.png" width="700"/>
<br/>
<img src="screenshots/dashboard_part2.png" width="700"/>


🧠 What I Learned
Writing clean ETL scripts in Python
Handling large datasets with Pandas
Performing database operations using SQLite
Building dashboards using Streamlit
Using Git & GitHub for version control

🎯 Project Purpose
Demonstrate end-to-end data pipeline skills
Practice ETL and data visualization
Add to my portfolio for data engineering interviews

🙋‍♀️ About Me
Pooja DM
Ex-Data Engineer at Walmart Global Tech
Learning & Building Data Engineering Projects

🔗 GitHub Profile
🔗 Project Repo

⭐ If you like this project, feel free to give it a star on GitHub!