from bottle import Bottle, run, request, get, post, template
import random
import docker
import urllib

app = Bottle()
client = docker.from_env()

def unquote_args(func):
  def do(*args, **kwargs):
    return func(*args, **{key: urllib.parse.unquote(x) if isinstance(x, str) else x for key, x in kwargs.items()})
  return do

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
  print(payload)
  if payload is not None:
    global client
    res = client.containers.run('infinit/dopenssl:3d6c942f9c580832cbf0c07cf8c9c6dc860ea44a',
                                '"' + str(payload) + '"',
                                remove = True).decode('ascii')
  return t.format(res = res, payload = payload or "")

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 80, threaded = True)
