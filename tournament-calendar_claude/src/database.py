# src/database.py
import sqlite3
from datetime import datetime
import json

class TournamentDatabase:
    def __init__(self, db_name="tournaments.db"):
        self.db_name = db_name
        self.init_database()
    
    def init_database(self):
        """Create the tournaments table if it doesn't exist"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tournaments (
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
            )
        ''')
        
        conn.commit()
        conn.close()
        print("Database initialized successfully!")
    
    def add_tournament(self, tournament_data):
        """Add a single tournament to database"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO tournaments 
            (name, sport, level, start_date, end_date, official_url, streaming_links, image_url, summary)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            tournament_data.get('name', ''),
            tournament_data.get('sport', ''),
            tournament_data.get('level', ''),
            tournament_data.get('start_date', ''),
            tournament_data.get('end_date', ''),
            tournament_data.get('official_url', ''),
            tournament_data.get('streaming_links', ''),
            tournament_data.get('image_url', ''),
            tournament_data.get('summary', '')
        ))
        
        conn.commit()
        conn.close()
    
    def add_multiple_tournaments(self, tournaments_list):
        """Add multiple tournaments at once"""
        for tournament in tournaments_list:
            self.add_tournament(tournament)
        print(f"Added {len(tournaments_list)} tournaments to database")
    
    def get_all_tournaments(self):
        """Get all tournaments from database"""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row  # This allows us to access columns by name
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM tournaments ORDER BY start_date')
        tournaments = cursor.fetchall()
        
        conn.close()
        
        # Convert to list of dictionaries
        return [dict(tournament) for tournament in tournaments]
    
    def get_tournaments_by_sport(self, sport):
        """Get tournaments for a specific sport"""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM tournaments WHERE sport = ? ORDER BY start_date', (sport,))
        tournaments = cursor.fetchall()
        
        conn.close()
        return [dict(tournament) for tournament in tournaments]
    
    def clear_all_tournaments(self):
        """Clear all tournaments (useful for testing)"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('DELETE FROM tournaments')
        conn.commit()
        conn.close()
        print("All tournaments cleared from database")
    
    def export_to_csv(self, filename="data/tournaments.csv"):
        """Export tournaments to CSV file"""
        import pandas as pd
        tournaments = self.get_all_tournaments()
        
        if tournaments:
            df = pd.DataFrame(tournaments)
            # Create data folder if it doesn't exist
            import os
            os.makedirs('data', exist_ok=True)
            
            df.to_csv(filename, index=False)
            print(f"Exported {len(tournaments)} tournaments to {filename}")
        else:
            print("No tournaments to export")
    
    def export_to_json(self, filename="data/tournaments.json"):
        """Export tournaments to JSON file"""
        tournaments = self.get_all_tournaments()
        
        if tournaments:
            import os
            os.makedirs('data', exist_ok=True)
            
            with open(filename, 'w') as f:
                json.dump(tournaments, f, indent=2)
            print(f"Exported {len(tournaments)} tournaments to {filename}")
        else:
            print("No tournaments to export")

# Test the database
if __name__ == "__main__":
    # Create database instance
    db = TournamentDatabase()
    
    # Add a sample tournament for testing
    sample_tournament = {
        'name': 'Test Cricket Tournament',
        'sport': 'cricket',
        'level': 'national',
        'start_date': '2024-12-01',
        'end_date': '2024-12-15',
        'official_url': 'https://example.com',
        'streaming_links': 'ESPN, Star Sports',
        'image_url': 'https://source.unsplash.com/400x300/?cricket',
        'summary': 'A test cricket tournament for demonstration purposes'
    }
    
    db.add_tournament(sample_tournament)
    
    # Get all tournaments
    all_tournaments = db.get_all_tournaments()
    print(f"Total tournaments: {len(all_tournaments)}")
    
    # Export to files
    db.export_to_csv()
    db.export_to_json()
    
    print("Database setup complete!")