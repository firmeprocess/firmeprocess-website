# FIRMEProcess Website

The homesite for Firme Process. [Visit it here](http://www.firmeprocess.org).

## Deets
This is a [flask](flask.pocoo.org) site, currently hosted on [heroku](https://www.heroku.com) for alpha and staging.

## Download and work on it locally
You'll need [git](http://git-scm.com/book/en/v2/Getting-Started-Installing-Git), [pip](https://pip.pypa.io/en/latest/installing.html), and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.org/en/latest/install.html) installed before starting.

Once these are installed, it's easy.

    $ git clone git@github.com:firmeprocess/firmeprocess-website.git
    $ cd firmeprocess-website
    $ mkvirtualenv firme
    $ pip install -r requirements
    $ echo ENVIRONMENT=LOCAL >> .env

And you're ready. Run locally using:

    $ foreman start

Then you're good to go.


