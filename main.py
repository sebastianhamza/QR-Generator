import qrcode

from flask import Flask, jsonify
from flask import send_file
from threading import Thread
from flask_restful import Resource, Api

def generate_qr(content_data):
  qr = qrcode.QRCode(
          version=1,
          box_size=10,
          border=2)
  qr.add_data(content_data)
  qr.make(fit=True)

  img = qr.make_image(fill='black', back_color='white')

  img.save('qrcode001.png')


app = Flask('')
api = Api(app)

app.url_map.strict_slashes = False

class Test(Resource):
  def get(self, content):
    generate_qr(content)
    return send_file('qrcode001.png' , mimetype='image/png')

api.add_resource(Test, '/api/restful/<path:content>')

def run():
  app.run(host='0.0.0.0',port=7210)

t = Thread(target=run)
t.start()  
 
