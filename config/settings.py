import os
# Testing Basic Parameters
BASE_URL_DEV = os.getenv("OMNI_BASE_URL", "https://dev.omnihubs.cloud/")
DEFAULT_TIMEOUT = int(os.getenv("OMNI_DEFAULT_TIMEOUT", "20000"))
HEADLESS = os.getenv("OMNI_HEADLESS", False)


# Testing Data
ACCOUNT_USERNAME = os.getenv("OMNI_ACCOUNT_USERNAME", "testuser01")
ACCOUNT_PASSWORD = os.getenv("OMNI_ACCOUNT_PASSWORD", "testuser01")

ENTRA_USERNAME = os.getenv("OMNI_ENTRA_USERNAME", "omnitest3@cathlife.symphox.com")
ENTRA_PASSWORD = os.getenv("OMNI_ENTRA_PASSWORD", "Omni168168168")

GOOGLE_USERNAME = os.getenv("OMNI_GOOGLE_USERNAME", "")
GOOGLE_PASSWORD = os.getenv("OMNI_GOOGLE_PASSWORD", "")

PROJECT_ABBR = os.getenv("OMNI_PROJECT_NAME", "e2e-project-abbr")