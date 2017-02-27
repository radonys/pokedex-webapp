#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import MySQLdb

form = cgi.FieldStorage() 

# Get data from fields
id1 = form.getvalue('id1')
pokemon_name = form.getvalue('pokemon_name')
pre_evolution = form.getvalue('pre_evolution')

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","Pokemon" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

print "Content-type:text/html\r\n\r\n"

print '''

<html>
<title>Contibute - Pokedex</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<style>
.jumbotron {
    background-color: #060000 ;
    color: #fff;
    padding: 90px 25px;
}

.container-fluid {
    padding: 60px 50px;
}

.navbar {
    margin-bottom: 0;
    background-color: #060000;
    z-index: 9999;
    border: 0;
    font-size: 14px !important;
    line-height: 5 !important;
    letter-spacing: 4px;
    border-radius: 0;
}

.navbar li a, .navbar .navbar-brand {
    color: #fff !important;

}

.navbar-nav li a:hover, .navbar-nav li.active a {
    color: #060000  !important;
    background-color: #fff !important;
}

.navbar-default .navbar-toggle {
    border-color: transparent;
    color: #fff !important;
}

.bg-grey {
    background-color: #f6f6f6;
}

</style>

<nav class="navbar navbar-default navbar-fixed-top">
  <div class="container">
    <div class="navbar-header">
      <a class="navbar-brand" href="/cgi-bin/DBMS_Project/index.py"><img src = "http://vignette3.wikia.nocookie.net/logopedia/images/e/e5/Pokemon_logo.png/revision/latest?cb=20120128115827" class = "img-responsive" width="150" height="150"></a>
    </div>
    <div class="collapse navbar-collapse" id="myNavbar">
      <ul class="nav navbar-nav navbar-right">
        <li><a href="/cgi-bin/DBMS_Project/types.py">TYPES</a></li>
        <li><a href="/cgi-bin/DBMS_Project/evolution.py">EVOLUTIONS</a></li>
        <li><a href="/cgi-bin/DBMS_Project/health.py">STAMINA & POWER</a></li>
        <li><a href="/cgi-bin/DBMS_Project/statistics.py">STATISTICS</a></li>
        <li><a href="/cgi-bin/DBMS_Project/contribute.py">CONTRIBUTE</a></li>
      </ul>
    </div>
  </div>
</nav>

<body>
  <div class="jumbotron text-center">
    <h1>Contribute to Pokedex</h1> 
    <p>Your access to the Pokemon world</p> 
  </div>

<div class="container-fluid">
  <h2>Enter new Pokemons</h2><br>
  <form action="/cgi-bin/DBMS_Project/contribute.py" method="post">
    <div class="form-group">
    <label for="id1">ID :</label><br><br>
    <input type="number" class="form-control" id="id1" name="id1"><br><br>
    <label for="pokemon_name">Pokemon Name :</label><br><br>
    <input type="text" class="form-control" id="pokemon_name" name="pokemon_name"><br><br>
    <label for="pre_evolution">Pre Evolution :</label><br><br>
    <input type="text" class="form-control" id="pre_evolution" name="pre_evolution">
  </div><br>
  <button type="submit" class="btn btn-default">Submit</button>

</form><br><br>'''

str1 = str(pokemon_name)
id2 = str(id1)
str2 = str(pre_evolution)

if str2=="None" :
    str2 = "\0"

sql = "INSERT into Evolution (id,species,pre_evolution) values( '"+(id2)+"','"+(str1)+"','"+(str2)+"');"

if str1!="None":

    try:
    # Execute the SQL command
        cursor.execute(sql)
        db.commit()
    # Fetch all the rows in a list of lists.
        print "<h3>Entered Sucessfully!</h3>"
    except:
        print "<h3>Not Allowed!</h3>"

# disconnect from server
db.close()

print '''
</div>

<div class="container-fluid bg-grey">
<h3>To get Pokemon IDs</h3>
  <a href="/cgi-bin/DBMS_Project/procedure.py" class="btn btn-default btn-lg">Click Here</a>
<h6 align="right">Involves triggers.</h6>
<h5 align="right">Developed by <a href = "https://www.facebook.com/yashsrivastava30">Yash Srivastava</a></h5>
</div>
</body>
</body>
</html>

'''
