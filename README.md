# SkyPro.Python course
## Homework 18. Flask-Restx architecture

**Content**

**Structure**

├── run.py \
├── requirements.txt \
├── README.MD \
├── data \
│   └── movies.db - database \
└── app \
    └── dao \
    │   └── model - SQLAclhemy models and marshmallow schemes\
    │       ├── movie.py \
    │       ├── director.py \
    │       └── genre.py \
    ├── service \
    │   ├── movie.py \
    │   ├── director.py \
    │   └── genre.py \
    ├── views \
    │   ├── movies.py \
    │   ├── directors.py \
    │   └── genres.py \
    ├── containter.py - create DAO and Services \
    ├── config.py - app configuration parameters \
    └── setup_db.py - set up database \


Kirill Paveliev\
May 2022