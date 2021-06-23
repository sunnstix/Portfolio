"""portfolio development configuration."""

import os
from pathlib import Path

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# File Upload to var/uploads/
UPLOAD_FOLDER = Path(os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
    'var', 'uploads'
))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
