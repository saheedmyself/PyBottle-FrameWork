import bottle
from bottle import route, template


@route('/')
def index():                                                                     
     return template('home')

app = bottle.app()