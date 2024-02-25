# Scraper Demo Project

## Overview
The Scraper Demo Project is designed to integrate and synchronize supplier stock systems into our database in near real-time. This Python-based application extracts product information from XML file and stores it in a MongoDB collection, following a specific schema. Synchronization is triggered every 3 seconds.

## Features
- XML Parsing: Extracts data from XML files.
- MongoDB Integration: Stores and updates product information in a MongoDB database.
- Customizable Product Mapping: Adapts product data to a predefined database schema.
- Periodic Updates: Ensures that the database is synchronized in a periodic manner.

## Installation
To set up the project environment, follow these steps:

1. **Clone the Repository**
    - For SSH:
      ```
      git clone git@github.com:oasilturk/scraper-demo.git
      ```
    - For HTTPS:
      ```
      git clone https://github.com/oasilturk/scraper-demo.git
      ```

2. **Set Up Python Virtual Environment**
    - On Windows:
      ```
      python -m venv venv
      .\venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```
      python3 -m venv venv
      source venv/bin/activate
      ```

3. **Install Dependencies**
    ```
    pip install -r requirements.txt
    ```

4. **MongoDB Setup**
    - Ensure MongoDB is installed and running on your system. [MongoDB Installation Guide](https://docs.mongodb.com/manual/installation/)

5. **Configuration**
    - Copy `sample_config.py` to `config.py`.
    - Set the MongoDB connection URI and other configuration settings in `config.py`.

## Usage
To run the project:

1. Place the XML file in the designated directory.
2. Ensure you virtual environment is active.
3. Execute the main script:
    ```
    python app/main.py
    ```

## Project Structure
- `app/`: Main application directory.
    - `config.py`: Config file for db connection informations.
    - `database.py`: Handles MongoDB interactions.
    - `main.py`: Main script to run the application.
    - `product.py`: Defines the product model.
    - `scheduler.py`: Runs the syncing logic periodically.
    - `xml_parser.py`: Parses XML files.
- `.gitignore`: List of files to be ignored by git.
- `lonca-sample.xml`: XML file with product informations.
- `requirements.txt`: Lists the Python dependencies.
- `README.md`: This file, containing project documentation.