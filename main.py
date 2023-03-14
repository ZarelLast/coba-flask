# Library
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

# Init
app = Flask("VideoAPI")
api = Api(app)

# Model
parser = reqparse.RequestParser()
parser.add_argument("id", required=True)
parser.add_argument("title", required=True, dest="title")
parser.add_argument("type", required=True)

# JSON
images = {
  "0": {"id":"000", "title":"Sepatu Sport", "type":"Sport"},
  "1": {"id":"001", "title":"Sepatu Formal", "type":"Formal"},
  "2": {"id":"002", "title":"Sepatu Casual", "type":"Casual"},
}

# Controller
class DataController(Resource):
  def get(self):
    return images
  
  def post(self):
    args = parser.parse_args()
    new_image = {"id":args["id"], "title":args["title"], "type":args["type"]}
    image_id = max(int(i) for i in images.keys()) + 1
    images[image_id] = new_image
    return images[image_id], 201

class DetailController(Resource):
  def get(self, image_id):
    return images[image_id]
  
  def put(self, image_id):
    args = parser.parse_args()
    new_image = {"id":args["id"], "title":args["title"], "type":args["type"]}
    images[image_id] = new_image
    return {image_id: images[image_id]}, 201 # Status Spesifik
  
  def delete(self, image_id):
    if image_id not in images:
      abort(404, message=f"Images {image_id} not found!")
    del images[image_id]
    return "deleted", 204

# Route
api.add_resource(DataController, "/images/")
api.add_resource(DetailController, "/images/<image_id>")

# Main
if __name__ == "__main__":
  app.run()