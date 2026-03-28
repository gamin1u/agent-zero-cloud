from python.helpers import dotenv
dotenv.save_dotenv_value("ANONYMIZED_TELEMETRY", "false")

# Optional browser_use import
try:
    import browser_use
    import browser_use.utils
    BROWSER_USE_AVAILABLE = True
except ImportError:
    BROWSER_USE_AVAILABLE = False
