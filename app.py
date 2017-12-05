import sys

version = "3d6c942f9c580832cbf0c07cf8c9c6dc860ea44a"
# Check --version:
# > if --version <xxx>: version = <xxx>
# > if --version: version = <default>
# > if --version --other stuff: version = <default>
if sys.argv.count('--version') and ((1 + sys.argv.index('--version')) < len(sys.argv)):
  v = sys.argv[sys.argv.index('--version') + 1]
  if not v.startswith('--'):
    version = v

from bottle import Bottle, run, request, get, post, template
app = Bottle()

import docker
client = docker.from_env()

# Unquote url parameters.
def unquote_args(func):
  import urllib
  def do(*args, **kwargs):
    return func(*args, **{key: urllib.parse.unquote(x) if isinstance(x, str) else x for key, x in kwargs.items()})
  return do

# Forward url parameters to the function.
def read_url_parameters(func):
  def do(*args, **kwargs):
    return func(*args, **kwargs, **dict(request.params))
  return do

@app.route('/encypher')
@read_url_parameters
@unquote_args
def index(payload = None):
  t = '''
<!DOCTYPE html>
<html>
  <body>

  <form action="encypher" method="get">
    <input type="text" name="payload" value="{payload}"><button type="submit" value="Submit">Submit</button>
  </form>

  </br>
    Result:
  </br>

  <pre>
{res}
  </pre>

  </body>
</html>
  '''
  res = ""
  if payload is not None:
    res = client.containers.run('infinit/dopenssl:{}'.format(version),
                                '"{}"'.format(payload),
                                remove = True).decode('ascii')
  return t.format(res = res, payload = payload or "")

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 80, threaded = True)
