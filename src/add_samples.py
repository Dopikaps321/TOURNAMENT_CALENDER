
from database import TournamentDatabase

def add_real_working_samples():
    db = TournamentDatabase()
    
    
    samples = [
        {
            'name': 'ICC Cricket World Cup',
            'sport': 'cricket',
            'level': 'international',
            'start_date': '2024-10-15',
            'end_date': '2024-11-20',
            'official_url': 'https://www.icc-cricket.com',  
            'streaming_links': 'Star Sports, Hotstar',
            'image_url': 'https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=400&h=300&fit=crop',
            'summary': 'The biggest cricket tournament in the world'
        },
        {
            'name': 'FIFA World Cup',
            'sport': 'football',
            'level': 'international',
            'start_date': '2024-12-01',
            'end_date': '2024-12-31',
            'official_url': 'https://www.fifa.com',  
            'streaming_links': 'ESPN, Fox Sports',
            'image_url': 'https://images.unsplash.com/photo-1431324155629-1a6deb1dec8d?w=400&h=300&fit=crop',
            'summary': 'The most watched football tournament globally'
        },
        {
            'name': 'All England Open',
            'sport': 'badminton',
            'level': 'international',
            'start_date': '2025-03-12',
            'end_date': '2025-03-17',
            'official_url': 'https://www.bwfworldtour.bwfbadminton.com',  
            'streaming_links': 'BBC Sport, Eurosport',
            'image_url': 'https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?w=400&h=300&fit=crop',
            'summary': 'Premier badminton championship event'
        },
        {
            'name': 'Mumbai Marathon',
            'sport': 'running',
            'level': 'national',
            'start_date': '2025-01-19',
            'end_date': '2025-01-19',
            'official_url': 'https://www.tatamumbaimarathon.com',  
            'streaming_links': 'Sony Sports Network',
            'image_url': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400&h=300&fit=crop',
            'summary': 'India biggest international marathon event'
        },
        {
            'name': 'Pro Kabaddi League',
            'sport': 'kabaddi',
            'level': 'national',
            'start_date': '2024-10-05',
            'end_date': '2024-12-15',
            'official_url': 'https://www.prokabaddi.com',  
            'streaming_links': 'Star Sports',
            'image_url': 'https://images.unsplash.com/photo-1594736797933-d0b22d3f6ebf?w=400&h=300&fit=crop',
            'summary': 'India premier professional kabaddi league'
        },
        {
            'name': 'National Swimming Championships',
            'sport': 'swimming',
            'level': 'national',
            'start_date': '2025-02-10',
            'end_date': '2025-02-15',
            'official_url': 'https://www.swimming.org.in',  
            'streaming_links': 'DD Sports',
            'image_url': 'https://images.unsplash.com/photo-1530549387789-4c1017266635?w=400&h=300&fit=crop',
            'summary': 'Top swimmers compete for national titles'
        },
        {
            'name': 'NBA Regular Season',
            'sport': 'basketball',
            'level': 'international',
            'start_date': '2024-10-15',
            'end_date': '2025-04-15',
            'official_url': 'https://www.nba.com',  
            'streaming_links': 'NBA League Pass, ESPN',
            'image_url': 'https://images.unsplash.com/photo-1546519638-68e109498ffc?w=400&h=300&fit=crop',
            'summary': 'Premier professional basketball league'
        },
        {
            'name': 'World Chess Championship',
            'sport': 'chess',
            'level': 'international',
            'start_date': '2024-12-20',
            'end_date': '2024-12-28',
            'official_url': 'https://www.fide.com',  
            'streaming_links': 'Chess.com, Chess24',
            'image_url': 'https://images.unsplash.com/photo-1606092195730-5d7b9af1efc5?w=400&h=300&fit=crop',
            'summary': 'World top chess players compete for the title'
        },
        {
            'name': 'Commonwealth Games Table Tennis',
            'sport': 'table tennis',
            'level': 'international',
            'start_date': '2024-07-28',
            'end_date': '2024-08-08',
            'official_url': 'https://www.ittf.com',  
            'streaming_links': 'BBC Sport, Seven Network',
            'image_url': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=400&h=300&fit=crop',
            'summary': 'International table tennis championship'
        },
        {
            'name': 'International Day of Yoga',
            'sport': 'yoga',
            'level': 'international',
            'start_date': '2025-06-21',
            'end_date': '2025-06-21',
            'official_url': 'https://www.un.org/en/observances/yoga-day',  
            'streaming_links': 'Yoga Alliance, YouTube',
            'image_url': 'https://images.unsplash.com/photo-1506126613408-eca07ce68e71?w=400&h=300&fit=crop',
            'summary': 'Global yoga practitioners demonstrate skills'
        },
        {
            'name': 'TCS Corporate Cricket Championship',
            'sport': 'cricket',
            'level': 'corporate',
            'start_date': '2024-12-05',
            'end_date': '2024-12-25',
            'official_url': 'https://www.tcs.com',  
            'streaming_links': 'Corporate TV, Local streaming',
            'image_url': 'https://images.unsplash.com/photo-1540747913346-19e32dc3e97e?w=400&h=300&fit=crop',
            'summary': 'IT companies cricket tournament championship'
        },
        {
            'name': 'Tour de France',
            'sport': 'cycling',
            'level': 'international',
            'start_date': '2025-07-05',
            'end_date': '2025-07-27',
            'official_url': 'https://www.letour.fr/en',  
            'streaming_links': 'Eurosport, NBC Sports',
            'image_url': 'https://images.unsplash.com/photo-1558618068-fcd25c85cd64?w=400&h=300&fit=crop',
            'summary': 'World most prestigious cycling race'
        },
        {
            'name': 'World Bodybuilding Championships',
            'sport': 'gym',
            'level': 'international',
            'start_date': '2024-11-15',
            'end_date': '2024-11-17',
            'official_url': 'https://www.ifbb.com',  
            'streaming_links': 'Muscle & Fitness TV',
            'image_url': 'https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b?w=400&h=300&fit=crop',
            'summary': 'International bodybuilding and fitness competition'
        }
    ]
    
    print(f"Adding {len(samples)} tournaments with REAL working URLs...")
    db.clear_all_tournaments()
    db.add_multiple_tournaments(samples)
    
    print("✅ Real sample tournaments added!")
    print(f"Total tournaments: {len(samples)}")
    
    
    db.export_to_csv()
    db.export_to_json()
    
    
    sports = set(t['sport'] for t in samples)
    print(f"Sports covered: {', '.join(sorted(sports))}")
    
    return samples

if __name__ == "__main__":
    add_real_working_samples()