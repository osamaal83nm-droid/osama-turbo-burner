name: Osama Turbo Burner Core

on:
  workflow_dispatch:

jobs:
  run_core:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Run Osama Core
        env:
          AIRTABLE_API_KEY: ${{ secrets.AIRTABLE_API_KEY }}
        run: python main.py
