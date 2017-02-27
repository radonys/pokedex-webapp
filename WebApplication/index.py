#!/usr/bin/python

import cgi
import cgitb; cgitb.enable()  # for troubleshooting

print "Content-type:text/html\r\n\r\n"

print '''

<html>
<title> Welcome to Pokedex </title>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
<style>
.jumbotron {
    background-color: #f4511e;
    color: #fff;
    padding: 90px 25px;
}

.container-fluid {
    padding: 60px 50px;
}

.navbar {
    margin-bottom: 0;
    background-color: #f4511e;
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
    color: #f4511e !important;
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
    <h1>Pokedex</h1> 
    <p>An encyclopedia of Pokemon species</p> 
  </div>

<div class="container-fluid">
  <h2>About Pokedex</h2> 
  <p>The Pokedex is a digital encyclopedia created by Professor Oak as an invaluable tool to trainers in the Pokemon world. It gives information about all Pokemon in the world that are contained in its database, although it differs in how it acquires and presents information over the different media. However, they are also only given to a few trainers at a time, generally to the ones that are felt to have exceptional potential and skill. There are different types of Pokedexes and each Pokedex is special to a specific region.</p>
</div>

<div class="container-fluid bg-grey">
  <h5 align="right">Developed by <a href = "https://www.facebook.com/yashsrivastava30">Yash Srivastava</a></h5>
</div>
</body>
</body>
</html>

'''
