from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
  return "It works!!"

if __name__ == '__main__':
  app.run(host="0.0.0.0", port=8080, debug=T)

@app.route("/order-animation")
def order_animation():
  return render_template(
    "order.html",
    invitation = "Welcome at ani creation"
  )

@app.route('/upload')
def upload():
  if 'my_file' not in request.files:
    return "sth wrong"
  upl_file = request.files['my_file']
  storage = new S#Storage(os.get, s3)
  storage.save(path="")
