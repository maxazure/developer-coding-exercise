# Blog Server Side API for Media Suite NZ

## Installation Steps

1. **Create .venv and activate**

   ```
   virtualenv .venv
   source .venv/bin/activate
   ```

2. **Installation dependencies**

   ```
   pip install -r requirements.txt
   ```

3. **Initialize the database (extract the tags from the text of \*.md and store the content in the database)**

   ```
   python seed.py
   ```

4. **Start the application**

   ```
   python manage.py runserver
   ```

Contact information:

   maxazure@gmail.com
   
   Jay Liu