Selenium Tech Demo
===================
These scripts are meant to showcase of how to deal with various async issues in automating using selenium.



To start the server, use Node to start the server:
	
	> npm install
	> node server.js

This will start a server at http://localhost:4567/index.html

Selenium scripts can be found under the /tests/ folder.
(Note: you'll have to install selenium driver bindings if you haven't already.
`pip install selenium`)

Techniques Demonstrated
========================
* Doing actions in JavaScript - http://localhost:4567/index.html#/
* jQuery queue polling. - http://localhost:4567/index.html#/movebox
* JavaScript Ajax Promise Latching - http://localhost:4567/index.html#/livesearch

