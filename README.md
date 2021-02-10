# Client Mailer
CRM &amp; client Mail system

A project to manage a list of clients which can then be emailed from a selection of email templates. This is controlled through a CLI menu.

# Preview

<img src="menu.png" width="300" height="200">

# Table of Contents

- [Project Title](*Client-Mailer)
- [Preview](*Preview)
- [Installation](*Installation)
- [Data](*Data)
- [Code](*Code)
- [Conclusion](*Conclusion)

# Installation

1. Start by cloning the repository:
```
git clone https://github.com/ChristopherBacon/Client-Mailer.git
cd ClientMailer'
```
2. Create a ```python 3.7.3``` environment.

3. Install dependencies

```
pip install requirements.txt
```
4. To run tests in terminal:
```
cd ClientMailer
pytest
```

# Data

1. ```emails/``` This is where the tmeplates for the emails live. You can add templates to this manually as txt files.

2. ```clients.csv```

# Code

1. [clients.py](*clients.py) Contains the client class, and also client helper functions

# Conclusion
