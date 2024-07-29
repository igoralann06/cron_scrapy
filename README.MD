# cron running scripts
- Process using following shell commands

# Install all libraries
$ cd cron_scrape
$ pip install -r requirement.txt

# Use python venv environment
$ python -m venv venv/source
$ source /venv/source/bin/activate

# Threading scraping scripts (cron)
$ python serve.py

- run the rebuy script
- run the kleinanzeigen.py script
- run the vinted script

# Run the frontend
$ streamlit run main.py --server.port=[PORT]

ex:) streamlit run main.py --server.port=80