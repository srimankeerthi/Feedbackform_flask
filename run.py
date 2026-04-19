import os
import sys

# Ensure the nested project package path is importable when the workspace root
# is the parent directory of the actual Flask project.
project_root = os.path.join(os.path.dirname(__file__), "FeedbackForm-Flask-App")
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from feedback import create_app

app = create_app()

if __name__ == "__main__":
    app.run()
