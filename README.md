GenAI Sports Tournament Calendar
A comprehensive GenAI-powered solution to generate up-to-date sports tournament calendars across 12 sports with multiple competition levels.
 Features
•	GenAI-Powered: Uses AI to extract tournament data from multiple sources
•	12 Sports Coverage: Cricket, Football, Badminton, Running, Gym, Cycling, Swimming, Kabaddi, Yoga, Basketball, Chess, Table Tennis
•	8 Competition Levels: Corporate, School, College/University, Club/Academy, District, State, Zonal/Regional, National, International
•	Real-time Data: Scrapes live tournament information
•	Multiple Formats: CSV and JSON export
•	REST API: Complete API for data access
•	Web UI: Interactive tournament browser
•	Local Tournaments: Includes regional and local competitions
 Project Structure
tournament-calendar/
├── src/
│   ├── database.py           
│   ├── enhanced_scraper.py   
│   ├── api.py         ## Use your Gemini KEY      
│   └── add_samples.py       
├── templates/
│   └── index.html           
├── static/
│   └── style.css           
├── data/
│   ├── tournaments.csv      
│   └── tournaments.json     
├── tournaments.db           
├── requirements.txt         
└── README.md               
 Setup Instructions
Prerequisites
•	Python 3.8+
•	pip (Python package manager)
Installation
1.	Clone/Download the project
# If using git
git clone <repository-url>
cd tournament-calendar

# Or extract the zip file
unzip tournament-calendar.zip
cd tournament-calendar
2.	Install dependencies
pip install -r requirements.txt
3.	Initialize database and add sample data
cd src
python add_samples.py
4.	Run the enhanced GenAI scraper (optional)
python enhanced_scraper.py
5.	Start the API server
python api.py
6.	Access the application
•	Web UI: http://localhost:5000
•	API: http://localhost:5000/api/tournaments
 Requirements.txt
Flask==2.3.3
requests==2.31.0
beautifulsoup4==4.12.2
pandas==2.1.1
sqlite3-to-pandas==0.1.0
numpy==1.24.3
lxml==4.9.3
 Database Schema
CREATE TABLE tournaments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sport TEXT NOT NULL,
    level TEXT,
    start_date TEXT,
    end_date TEXT,
    official_url TEXT,
    streaming_links TEXT,
    image_url TEXT,
    summary TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

 Sample Output
CSV Format
id,name,sport,level,start_date,end_date,official_url,streaming_links,image_url,summary
1,ICC Cricket World Cup,cricket,international,2024-10-15,2024-11-20,https://icc-cricket.com,Star Sports,https://source.unsplash.com/400x300/?cricket,The biggest cricket tournament in the world
JSON Format
[
  {
    "id": 1,
    "name": "ICC Cricket World Cup",
    "sport": "cricket",
    "level": "international",
    "start_date": "2024-10-15",
    "end_date": "2024-11-20",
    "official_url": "https://icc-cricket.com",
    "streaming_links": "Star Sports",
    "image_url": "https://source.unsplash.com/400x300/?cricket",
    "summary": "The biggest cricket tournament in the world"
  }
]

 

