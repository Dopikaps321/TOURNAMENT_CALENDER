
from flask import Flask, jsonify, render_template, request
from database import TournamentDatabase
import json


app = Flask(__name__, template_folder='../templates', static_folder='../static')
db = TournamentDatabase()

@app.route('/')
def home():
    """Home page with simple UI"""
    return render_template('index.html')

@app.route('/api/tournaments')
def get_all_tournaments():
    """API endpoint to get all tournaments"""
    try:
        tournaments = db.get_all_tournaments()
        return jsonify({
            'success': True,
            'count': len(tournaments),
            'tournaments': tournaments
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/tournaments/<sport>')
def get_tournaments_by_sport(sport):
    """API endpoint to get tournaments by sport"""
    try:
        tournaments = db.get_tournaments_by_sport(sport.lower())
        return jsonify({
            'success': True,
            'sport': sport,
            'count': len(tournaments),
            'tournaments': tournaments
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/tournaments/level/<level>')
def get_tournaments_by_level(level):
    """API endpoint to get tournaments by level"""
    try:
        all_tournaments = db.get_all_tournaments()
        filtered_tournaments = [t for t in all_tournaments if t.get('level', '').lower() == level.lower()]
        
        return jsonify({
            'success': True,
            'level': level,
            'count': len(filtered_tournaments),
            'tournaments': filtered_tournaments
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/sports')
def get_available_sports():
    """API endpoint to get list of sports"""
    try:
        all_tournaments = db.get_all_tournaments()
        sports = list(set(t.get('sport', '') for t in all_tournaments))
        sports = [s for s in sports if s]  # Remove empty strings
        
        return jsonify({
            'success': True,
            'count': len(sports),
            'sports': sorted(sports)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/stats')
def get_tournament_stats():
    """API endpoint to get tournament statistics"""
    try:
        all_tournaments = db.get_all_tournaments()
        
        # Count by sport
        sports_count = {}
        levels_count = {}
        
        for tournament in all_tournaments:
            sport = tournament.get('sport', 'unknown')
            level = tournament.get('level', 'unknown')
            
            sports_count[sport] = sports_count.get(sport, 0) + 1
            levels_count[level] = levels_count.get(level, 0) + 1
        
        return jsonify({
            'success': True,
            'total_tournaments': len(all_tournaments),
            'sports_count': sports_count,
            'levels_count': levels_count
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/refresh')
def refresh_tournaments():
    """API endpoint to refresh tournament data"""
    try:
        from genai_scraper import RealGenAIScraper as SimpleTournamentScraper
        
        print("Starting tournament refresh...")
        scraper = SimpleTournamentScraper()
        
        
        db.clear_all_tournaments()
        
        
        tournaments = scraper.scrape_all_sports()
        
        return jsonify({
            'success': True,
            'message': f'Refreshed with {len(tournaments)} tournaments',
            'count': len(tournaments)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'success': False,
        'error': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'success': False,
        'error': 'Internal server error'
    }), 500

if __name__ == '__main__':
    print("Starting Tournament Calendar API...")
    print("Available endpoints:")
    print("  GET /                           - Web UI")
    print("  GET /api/tournaments            - All tournaments") 
    print("  GET /api/tournaments/<sport>    - Tournaments by sport")
    print("  GET /api/tournaments/level/<level> - Tournaments by level")
    print("  GET /api/sports                 - Available sports")
    print("  GET /api/stats                  - Tournament statistics")
    print("  GET /api/refresh                - Refresh tournament data")
    print("\nStarting server at http://localhost:5000")
    
    
    app.run(debug=True, host='0.0.0.0', port=5000)