#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run FastAPI app
uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# Run Gradio app
python gradio_app/app.py &

# Run PlantUML generator
# (no need to run this as it's not a standalone app)

# Run tests
python -m unittest tests/test_knowledge.py
