# src/config.py - Secure configuration management
import os
from dotenv import load_dotenv
import logging

# Load environment variables from .env file
load_dotenv()

class Config:
    """Secure configuration management"""
    
    # API Configuration
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    
    # Database Configuration
    DATABASE_URL = os.getenv('DATABASE_URL', 'tournaments.db')
    
    # Flask Configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-change-this')
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    PORT = int(os.getenv('PORT', 5000))
    HOST = os.getenv('HOST', '0.0.0.0')
    
    # Rate Limiting
    RATE_LIMIT_REQUESTS = int(os.getenv('RATE_LIMIT_REQUESTS', 100))
    RATE_LIMIT_WINDOW = int(os.getenv('RATE_LIMIT_WINDOW', 3600))  # 1 hour
    
    # Scraping Configuration
    MAX_RETRIES = int(os.getenv('MAX_RETRIES', 3))
    REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', 15))
    DELAY_BETWEEN_REQUESTS = float(os.getenv('DELAY_BETWEEN_REQUESTS', 2.0))
    
    @classmethod
    def validate_config(cls):
        """Validate configuration and log warnings"""
        logger = logging.getLogger(__name__)
        
        if not cls.GEMINI_API_KEY:
            logger.warning("⚠️ GEMINI_API_KEY not set - API functionality will be limited")
            
        if cls.SECRET_KEY == 'your-secret-key-change-this':
            logger.warning("⚠️ Using default SECRET_KEY - change this in production")
            
        logger.info("✅ Configuration validated")
        
        return {
            'gemini_api_configured': bool(cls.GEMINI_API_KEY),
            'debug_mode': cls.DEBUG,
            'database_url': cls.DATABASE_URL
        }

# Create a .env template file
def create_env_template():
    """Create .env template file with all required variables"""
    template = """# Tournament Scraper Configuration
# Copy this file to .env and fill in your values

# API Keys
GEMINI_API_KEY=your-gemini-api-key-here

# Database
DATABASE_URL=tournaments.db

# Flask Settings
SECRET_KEY=your-secret-key-here
DEBUG=False
PORT=5000
HOST=0.0.0.0

# Rate Limiting
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_WINDOW=3600

# Scraping Settings
MAX_RETRIES=3
REQUEST_TIMEOUT=15
DELAY_BETWEEN_REQUESTS=2.0
"""
    
    try:
        with open('.env.template', 'w') as f:
            f.write(template)
        print("✅ Created .env.template file")
    except Exception as e:
        print(f"❌ Failed to create .env.template: {e}")

if __name__ == "__main__":
    create_env_template()
    Config.validate_config()