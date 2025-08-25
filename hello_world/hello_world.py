"""
  hello_world.py

  The canonical example which demonstrates some of the syntax used to create
  a single-page Django app.

"""
from nanodjango import Django

app = Django()


@app.route("/")
def hello_world(request):
    return "<p>Hello, World!</p>"
