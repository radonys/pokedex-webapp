#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import MySQLdb #Should be changed for Python3.

form = cgi.FieldStorage() 

# Get data from fields
pokemon_name = form.getvalue('pokemon_name')

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","Pokemon" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

print "Content-type:text/html\r\n\r\n"

print '''

<html>
<title>Pokemon Evolutions - Pokedex</title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<style>
.jumbotron {
    background-color: #390383  ;
    color: #fff;
    padding: 90px 25px;
}

.container-fluid {
    padding: 60px 50px;
}

.navbar {
    margin-bottom: 0;
    background-color: #390383  ;
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
    color: #390383   !important;
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
    <h1>Pokemon Evolutions</h1> 
    <p>Pokemon by their evolution family</p> 
  </div>

<div class="container-fluid">
  <h2>Search by Pokemon</h2><br>
  <form action="/cgi-bin/DBMS_Project/evolution.py" method="post">
    <div class="form-group">
    <label for="pokemon_name">Pokemon Name :</label><br><br>
    <input type="text" class="form-control" id="pokemon_name" name="pokemon_name">
  </div><br>
  <button type="submit" class="btn btn-default">Submit</button>

</form><br><br>'''

str1 = str(pokemon_name)
sql = "select a.pre_evolution,a.species,b.species from Evolution a,Evolution b where a.species = b.pre_evolution and a.species = '"+(str1)+"';"

if str1!="None":

    try:
    # Execute the SQL command
        cursor.execute(sql)
    # Fetch all the rows in a list of lists.
        results = cursor.fetchall()

        print '''<div class="container">

        <table class="table table-striped">
            <thead>
            <tr>
                <th>Pre Evolution</th>
                <th>Pokemon</th>
                <th>Pro Evolution</th>
            </tr>
            </thead>
            <tbody>'''

        for row in results:

            name = row[0]
            type1 = row[1]
            type2 = row[2]
            # Now print fetched result
            #print "name=%s,type1=%s,type2=%s <br>" % \
                    #(name, type1, type2)
            print "<tr>"
            print "<td>"
            print name
            print "</td>"
            print "<td>"
            print type1
            print "</td>"
            print "<td>"
            print type2
            print "</td>"
            print "</tr>"
        print '''</tbody>
        </table>
        </div>'''
    except:
        print "Error: unable to fetch data"

# disconnect from server
db.close()

print '''
</div>

<div class="container-fluid bg-grey">
<h6 align="right">The search uses Self Join.</h6>
<h5 align="right">Developed by <a href = "https://www.facebook.com/yashsrivastava30">Yash Srivastava</a></h5>
</div>
</body>
</body>
</html>

'''
