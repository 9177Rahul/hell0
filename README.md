# OOPsVerse — Java OOPs learning platform (starter)

A syllabus-driven Flask website with expandable Module/Unit navigation, dedicated topic routes rendered through a reusable lesson template, a Java playground, and local progress tracking.

## Run locally (Windows / Ubuntu)

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Ubuntu/macOS: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Java execution
The Run button sends source code to the Flask backend, which calls the Piston execution API. The backend does not execute submitted source code itself. Public execution services can impose rate limits or become unavailable; do not treat this as a production-grade exam system without reviewing provider terms, quotas, privacy, abuse controls, and sandbox limits.

## Deploy on Render
1. Create a GitHub repository and upload this project.
2. In Render, choose **New → Web Service** and connect the repository.
3. Build command: `pip install -r requirements.txt`
4. Start command: `gunicorn app:app`
5. Choose Free for a prototype and deploy.

The included `render.yaml` can also be used as a Blueprint. Free web services can sleep after inactivity and have ephemeral filesystems; this prototype stores completion progress in the browser's localStorage, not in a server database.

## Current scope and next development work
This is a working first scaffold: all 43 syllabus topics are navigable, the lesson template is reusable, the theme toggle and local completion tracking work, and the compiler endpoint is wired. The narrative/explanation/visual sections are starter teaching scaffolds, not yet fully authored lecture notes for every topic. Topic-specific stories, accurate deep explanations, custom diagrams, verified example programs, question banks, accounts, and faculty content management should be built and reviewed unit by unit before classroom use.
