# File Content Analyzer
Analyzes file contents from specified folders using Google's Gemini API.

## Prerequisites
- Python 3.x
- Google Gemini API key (set as `GEMINI_API_KEY` environment variable)

## Installation
1. Save the script as `query.py`
2. Install required package:
```bash
pip install google-generativeai
```

## Usage
```bash
python query.py -f FOLDERS -q QUERY [-d] [-w EXTENSIONS]

Arguments
-f, --folders: Comma-separated folder paths (required)
-q, --query: Query string for Gemini API (required)
-d, --dry_run: Dry run without API call (optional)
-w, --white_lists: Comma-separated file extensions (default: .py,.html)
```
