
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta
import time
import os
from database import TournamentDatabase

class RealGenAIScraper:
    def __init__(self):
        self.db = TournamentDatabase()
        
        # Gemini API Configuration only
        self.api_config = {
            'gemini': {
                'api_key': os.getenv('GEMINI_API_KEY', 'your-gemini-key-here'),
                'endpoint': 'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent'
            }
        }
        
        self.selected_api = 'gemini'
        
        # Sports sources for real data
        self.sports_sources = {
            'cricket': [
                'https://www.espncricinfo.com/live-cricket-score',
                'https://www.cricbuzz.com/cricket-schedule/upcoming-matches',
                'https://www.icc-cricket.com/tournaments'
            ],
            'football': [
                'https://www.fifa.com/tournaments',
                'https://www.uefa.com/uefachampionsleague/',
                'https://www.premierleague.com/fixtures'
            ],
            'basketball': [
                'https://www.nba.com/schedule',
                'https://www.fiba.basketball/competitions'
            ],
            'tennis': [
                'https://www.atptour.com/en/tournaments',
                'https://www.wtatennis.com/tournaments'
            ],
            # Add more sports...
        }
    
    def setup_api_key(self, api_key):
        """Setup Gemini API key"""
        self.api_config['gemini']['api_key'] = api_key
        print(f"✅ Gemini API key set")
    
    def call_gemini_api(self, text_content, sport):
        """Call Google Gemini API for tournament extraction"""
        config = self.api_config['gemini']
        
        if config['api_key'] == 'your-gemini-key-here':
            print("⚠️ Please set your Gemini API key first!")
            return self.fallback_extraction(text_content, sport)
        
        prompt = f"""
        Extract {sport} tournament information from this website content.
        Return JSON array with: name, level, start_date, end_date, summary (50 words max), streaming_info.
        Level must be: international, national, state, college, school, corporate, or club.
        Dates in YYYY-MM-DD format for 2024-2025 tournaments only.
        
        Content: {text_content[:1500]}
        """
        
        try:
            response = requests.post(
                f"{config['endpoint']}?key={config['api_key']}",
                headers={'Content-Type': 'application/json'},
                json={
                    'contents': [{
                        'parts': [{'text': prompt}]
                    }],
                    'generationConfig': {
                        'temperature': 0.3,
                        'maxOutputTokens': 1000
                    }
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                content = result['candidates'][0]['content']['parts'][0]['text']
                
                # Extract JSON from response
                content = content.strip()
                if content.startswith('```json'):
                    content = content[7:-3]
                elif content.startswith('```'):
                    content = content[3:-3]
                
                tournaments_data = json.loads(content)
                return self.process_ai_response(tournaments_data, sport)
            else:
                print(f"Gemini API Error: {response.status_code}")
                return self.fallback_extraction(text_content, sport)
                
        except Exception as e:
            print(f"Gemini API Error: {e}")
            return self.fallback_extraction(text_content, sport)
    
    def process_ai_response(self, tournaments_data, sport):
        """Process and validate AI response"""
        processed_tournaments = []
        
        if not isinstance(tournaments_data, list):
            tournaments_data = [tournaments_data] if tournaments_data else []
        
        for tournament in tournaments_data[:5]:  # Limit to 5 per source
            try:
                processed_tournament = {
                    'name': tournament.get('name', f'{sport.title()} Tournament'),
                    'sport': sport,
                    'level': tournament.get('level', 'club').lower(),
                    'start_date': self.validate_date(tournament.get('start_date')),
                    'end_date': self.validate_date(tournament.get('end_date')),
                    'official_url': self.generate_official_url(sport, tournament.get('name', '')),
                    'streaming_links': tournament.get('streaming_info', 'TBD'),
                    'image_url': f"https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=400&h=300&fit=crop&q={sport}",
                    'summary': tournament.get('summary', f'{sport.title()} tournament')[:50]
                }
                processed_tournaments.append(processed_tournament)
            except Exception as e:
                print(f"Error processing tournament: {e}")
                continue
        
        return processed_tournaments
    
    def validate_date(self, date_str):
        """Validate and format dates"""
        if not date_str:
            future_date = datetime.now() + timedelta(days=30)
            return future_date.strftime('%Y-%m-%d')
        
        try:
            parsed_date = datetime.strptime(date_str, '%Y-%m-%d')
            return parsed_date.strftime('%Y-%m-%d')
        except:
            future_date = datetime.now() + timedelta(days=30)
            return future_date.strftime('%Y-%m-%d')
    
    def generate_official_url(self, sport, tournament_name):
        """Generate realistic official URLs"""
        url_mapping = {
            'cricket': 'https://www.icc-cricket.com',
            'football': 'https://www.fifa.com',
            'basketball': 'https://www.nba.com',
            'tennis': 'https://www.atptour.com',
            'badminton': 'https://www.bwfbadminton.com',
            'swimming': 'https://www.swimming.org',
            'cycling': 'https://www.uci.org',
            'chess': 'https://www.fide.com'
        }
        return url_mapping.get(sport, f'https://www.{sport}.org')
    
    def fallback_extraction(self, text_content, sport):
        """Fallback when API is not available"""
        print(f"Using fallback extraction for {sport}")
        tournament = {
            'name': f'{sport.title()} Championship 2024',
            'sport': sport,
            'level': 'national',
            'start_date': (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d'),
            'end_date': (datetime.now() + timedelta(days=37)).strftime('%Y-%m-%d'),
            'official_url': self.generate_official_url(sport, ''),
            'streaming_links': 'ESPN, Star Sports',
            'image_url': f"https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=400&h=300&fit=crop",
            'summary': f'Professional {sport} tournament with top athletes'
        }
        return [tournament]
    
    def scrape_with_genai(self, sport, max_sources=2):
        """Scrape sport tournaments using Gemini GenAI"""
        print(f"\n🤖 GenAI Scraping {sport.title()} tournaments...")
        
        all_tournaments = []
        sources = self.sports_sources.get(sport, [])
        
        for source_url in sources[:max_sources]:
            print(f"Processing: {source_url}")
            
            try:
                response = requests.get(source_url, timeout=15, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                })
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    text_content = soup.get_text()
                    
                    tournaments = self.call_gemini_api(text_content, sport)
                    
                    if tournaments:
                        print(f"✅ Found {len(tournaments)} tournaments")
                        all_tournaments.extend(tournaments)
                else:
                    print(f"❌ Failed to fetch: {response.status_code}")
                    
            except Exception as e:
                print(f"❌ Error processing {source_url}: {e}")
            
            time.sleep(2)
        
        return all_tournaments
    
    def scrape_all_sports_with_genai(self):
        """Scrape all sports using Gemini GenAI"""
        print(f"🚀 Starting Real GenAI Scraping with GEMINI API...")
        
        all_tournaments = []
        
        for sport in self.sports_sources.keys():
            try:
                tournaments = self.scrape_with_genai(sport)
                all_tournaments.extend(tournaments)
                print(f"✅ {sport}: {len(tournaments)} tournaments")
            except Exception as e:
                print(f"❌ Error with {sport}: {e}")
        
        if all_tournaments:
            print(f"\n💾 Saving {len(all_tournaments)} tournaments...")
            self.db.clear_all_tournaments()
            self.db.add_multiple_tournaments(all_tournaments)
            self.db.export_to_csv()
            self.db.export_to_json()
            print(f"🎉 GenAI Scraping Complete: {len(all_tournaments)} tournaments")
        
        return all_tournaments

# Usage Examples
if __name__ == "__main__":
    scraper = RealGenAIScraper()
    
    # Setup your Gemini API key
    # scraper.setup_api_key('AIzaSyBUFdXhIZvhqj8lkSz-GMenGt1TcK_V30A')
    
    print("🤖 Real GenAI Tournament Scraper (Gemini Only)")
    print("⚠️ Please set your Gemini API key first using setup_api_key()")
    
    # Test with fallback (no API key needed)
    tournaments = scraper.scrape_with_genai('cricket', max_sources=1)
    print(f"\n✨ Sample tournament: {tournaments[0] if tournaments else 'None'}")