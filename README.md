# Portfolio
This portfolio is originally a project asked by Junior42 Paris. Which is an organization that helps students improve their coding skills by working for companies that need developers.
My objective is to deploy this project to GitHub Page, once I'm happy with how it looks, and how it works. :smiley:


## Install

- Run `docker-compose build`


- Edit the `.env.template`
  > - You don't have to edit the pgadmin variables if you don't want to access the admin page  
  > - Make sure that you rename it `.env`


- If it's your first time running it, you'll have to seperately run `docker-compose --env-file backend/.env up db` first, then `docker-compose up backend_app`. Otherwise the backend will try to connect to the db before it's ready.


- Run `docker-compose up frontend`
  > - You can actually run that whenever you want
  > - Go to `localhost:8080` to check the app. You won't have anything displayed since you didn't insert any data in the database.

- If you want to access the pgadmin page, run `docker-compose --env-file backend/.env up pgadmin`
  > - You can then go to `localhost:5050` and connect with the credentials you provided in the `.env`.
  > - You'll need it to create an admin user


- To insert data into the database, you'll have to set up your python environment, with virtualenv for example.
  > - Inside the backend dir, run `virtualenv env`.
  > - Run `source env/bin/active`
  > - Run `pip3 install -r requirements.txt`
  > - Run `python3 insert_fixtures.py` to insert the `fixtures.json` data into your database
 
- Go to `localhost:8080` and check that projects are here
  > - There is an issue with how the projects are loaded. You'll have to change tab once or twice before you see anything.
 
 ## Create an admin user

- Go to `localhost:5050` and connect to pgadmin with your credentials


- Add a new server
  > - Name it whatever you want (for me it's `portfolio`)
  > - `host: db`
  > - `user` refers to `postgres_user` in the `.env` file
  > - `password` refers to `postgres_password` in the `.env` file

- Once you created a new server, access the `user` table: portfolio -> Schemas --> Tables --> right click on `user` --> View/Edit Data (All rows)
  > - At this point, you have to enter the email address and the hash (256SHA) of your password (https://passwordsgenerator.net/sha256-hash-generator/)
  > - Save the user (F6)
  > - I'm planning on automate it, but not now :smiley:

- You can now access the admin page and import my projects from github
  > - `localhost:8080/admin`



## Notes

This Portfolio is still a work in progress. There are several known issues, and a few features I plan to add.



