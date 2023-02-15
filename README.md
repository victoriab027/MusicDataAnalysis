Music Data Analysis
==============================
This project is based off of the Milion_Dollar_Playlist created by Spotify. The goal of this project is to "analyze the Million Playlist Dataset for spotify to recommend songs to users based on the playsit chosen". I expanded the scope of this problem by implementing data from multiple other datasets. These datasets contained more data about each song such as either just tags to other similar songs or traits like "sadness", "romance", and "danceability". Cross referencing with these datasets allowed me to create a more effiecient and accurate algorithm.
<br>
<br>
Since writing this README, the project has massively evolved. Instead of databases, this project has sifted into using the Spotify API to create a new spotify extension, creatify. This website will give users the chance to create a new playlist based on specifc genres and psychoacustoic values. Eventaully, the goal is to work with NLP packages in python to reccomend playlist names to the user based on their pervious playlist naming conventions as well as sentiment analysis on this playlist.

Dataset Usage
------------
- Spotify Million Playlsit Dataset: https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge 
- Music Topics and Metadata: https://data.mendeley.com/datasets/3t9vbwxgr5/1
- MusicOS: https://marianaossilva.github.io/DSW2019/#tables
- Last.fm Dataset: http://millionsongdataset.com/lastfm/

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    ├── web_dev            <- Source code for website implementation
    |
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project formatting based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
