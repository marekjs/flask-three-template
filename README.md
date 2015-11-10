# Flask-Humbular project template
Project template for Python Flask three-tier, Single Page Applications using the [Humbular project template](https://github.com/RobertoPrevato/Humbular).

## Features
* Single Page Application code structure.
* Project skeleton ready to use, to start a three tier web application using Flask for its presentation layer.
* Localization strategy, using Flask-Babel.
* Authentication and authorization strategies, including anonymous authentication.
* Login mechanism protected against brute forcing (stores login attempts in DB).
* DB based sessions strategy.
* MongoDB collections for accounts, sessions, login attempts.
* Example files for production deployment using Nginx and uWSGI servers.
* Skeleton for data access layers for MongoDB.
* Skeleton for unit testing.
* Custom error pages.
* Application db logger, to store and retrieve messages and exceptions logs in database

## Branches
* [empty-project](https://github.com/RobertoPrevato/flask-three-template/tree/empty-project): empty template without any authentication strategy.
* [master](https://github.com/RobertoPrevato/flask-three-template/tree/master): template with custom authentication and authorization strategy.
* [spa-humbular](https://github.com/RobertoPrevato/flask-three-template/tree/spa-humbular): template with Humbular Single Page Application strategy.

## Dependencies
* Python.
* [Flask](http://flask.pocoo.org/).
* [Flask-Babel](https://pythonhosted.org/Flask-Babel/).
* pymongo
* pycrypto
```bash
$ sudo pip install Flask
$ sudo pip install Flask-Babel
$ sudo pip install pymongo
$ sudo pip install pycrypto
```

## Servers setup
* Basic settings file for Nginx.
* Settings file for uWSGI.
* Development server ready to use: Flask itself.

## Grunt integration
* JavaScript bundling and minification strategy.
* LESS compilation.