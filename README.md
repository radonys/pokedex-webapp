# pokedex-webapp
Pokedex - All about Pokemon

This web application was created for an Database Management project which involves all types of SQL joins along with triggers, views and storage procedures.

The web application has been created using Python scripts with Common Gateway Interface (CGI) module as back-end and HTML and CSS (with Bootstrap) as front-end. The scripts also involve use MySQLdb module for accessing MySQL database.

How to Use :

The scripts need to be placed in the /cgi-bin folder in Document Root of your server. Then the scripts need to be given special permissions using "sudo chmod 755 " to run on your server, else it will throw errors. In the scripts, change the name of the entries in "db = MySQLdb.connect("server","user","password","database" )" where first entry is server-name, second is username for database, third is the password for database, set by you and last one is the database name.

Then start your web server and MySQL server and run the scripts.

Contribute :

Keep contributing to the database and web-application so that it can be used as the perfect Pokedex!
