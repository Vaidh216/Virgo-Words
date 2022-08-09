# Virgo-Words

Virgo-Words is an article writing competition held online in the College Fest Ekarithin-22.
Where Participants can login with their mobile number and then they will be redirected to their respective links to write their articles.
Here the writing page should not be activated before the required time of 10:00 AM of 5th May and will auto submit the article on 11:00 AM,
And All the articles after 11:02AM Will not be accepted by the server.
All the response will be stored in the individual canditates are stored in server and there is only one entry allowed per phone number.

##  Currently hosted
Currently hosted at [https://virgo-words.herokuapp.com/](https://virgo-words.herokuapp.com/)

## Installation

Create first the Virtual environment or just the default one by name venu which will be activated by following command.
```bash
venv\Scripts\activate
```

Then install all the required packages given on requirements.txt

```bash
pip install -r requirements.txt
```

To run the program type

```bash
python main.py
```
Boom! the webite is good to go.


##  Models and Databases
Here The sqlite3 database is used to store the data of various users and model is as follows

```python
class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),nullable=False)
    phone = db.Column(db.String(10), unique=True,nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    resp = db.Column(db.String(5000))

    def __init__(self,name,email,phone,topic):
        self.name = name
        self.email = email
        self.phone = phone
        self.topic = topic
```

##  Results
The contest is finally over and there were neraby 25-30 participants and the experience with the platform was fantastic.

