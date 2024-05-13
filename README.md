## Arabic NLP Pipeline and Web Scraping Project

This repository contains an Arabic NLP pipeline and a Scrapy web scraping project designed for extracting and processing textual data from Arabic news websites : www.addustour.com


### Structure the project 


```markdown
Lab1
├── .venv
├── lab1
│ ├── spiders
│ │ ├── init.py
│ │ └── addustourspider.py
│ ├── init.py
│ ├── items.py
│ ├── middlewares.py
│ ├── pipelines.py
│ ├── settings.py
├── NLP_pipeline
│ ├── NLP_pipeline.ipynb
│ ├── arabicdata.json
├── scrapy.cfg
└── README.md
'''

### Project Components:

#### NLP Pipeline (NLP_pipeline.ipynb):

This Jupyter Notebook implements a comprehensive pipeline for cleaning, processing, and analyzing Arabic text. It includes:

- **Text Cleaning:** Removing HTML tags, URLs, punctuation, numbers, and Arabic diacritics.
- **Tokenization:** Exploring different tokenization techniques such as sentence and word tokenization using various methods.
- **Stop Word Removal:** Filtering out common, non-informative words using NLTK's Arabic stop words list.
- **Stemming and Lemmatization:** Comparing ISRIStemmer and Qalsadi Lemmatizer to reduce words to their base form.
- **Part-of-Speech (POS) Tagging:** Experimenting with both rule-based (SpaCy) and machine learning-based (Stanford Tagger) approaches for POS tagging.
- **Named Entity Recognition (NER):** Extracting named entities like locations (LOC) using Stanza's Arabic NER capabilities.

#### Scrapy Project:

- **items.py:** Defines the data structure for scraped items with fields like author, title, content, etc.
- **pipelines.py:** Implements a MongoDB pipeline to store scraped items efficiently in a MongoDB database.

### Usage:

#### Set up the environment:

- Install required libraries:

    ```bash
    pip install scrapy nltk stanza qalsadi pymongo spacy
    ```

- Download the Stanford POS Tagger and Arabic model from the official website.

- Update the paths in `NLP_pipeline.ipynb` to point to the downloaded files.

#### Configure Scrapy project:

- Modify the spider in the `spiders` directory to target the desired Arabic news website.

- Update the MongoDB connection details in `settings.py`.

#### Run the Scrapy spider:

- Use the `scrapy crawl <spider_name>` command to start scraping.

#### Process scraped data:

- Run the `NLP_pipeline.ipynb` notebook to clean, analyze, and extract insights from the collected text data.

