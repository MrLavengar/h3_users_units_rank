# Heroes 3 Units ranking

### What is this application about?
In this web app I downloaded data about all Heroes of Might and Magic 3 (HOMM3) units using Beautfiull Soup library, then save it to json and fill database using manage.py command. You can find information about all castles, and creatures. You can edit this information if you are loggend in. Finaly, you can vote.

### Main functionality
Main functionality of this web app is to allow you to vote, which units are the best. You have to decide between two troops of units. Then, your votes and all other users votes will display in 'Creatures rank' section.

### Database
Postgresql (I used pgAdmin3 on ubuntu)
Name your database *h3_creatures_rank*

To fill database with creatures and castles, run migrations, then:
```
python manage.py pupulatedata
```
It will fill your database with all heroes 3 creatures and their stats.

### Task list
- [ ] add Django admin
- [ ] hide password in environment variable
