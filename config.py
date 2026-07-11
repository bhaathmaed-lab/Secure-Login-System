SECRET_KEY = "your_secret_key_here"
DATABASE = "users.db"
import os

# Application Secret Key
SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "change-this-secret-key"
)

# Database Configuration
DATABASE = "users.db"

# Security Settings
PASSWORD_MIN_LENGTH = 8

# Session Security
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False   # Change to True when using HTTPS
SESSION_COOKIE_SAMESITE = "Lax"
Purpose of config.py:
✅ Stores application settings separately
✅ Protects secret keys from being hardcoded
✅ Manages database configuration
✅ Improves Flask session security
In your app.py, import it:
from config import SECRET_KEY, DATABASE

app.secret_key = SECRET_KEY