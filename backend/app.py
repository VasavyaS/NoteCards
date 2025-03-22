# TODO: UPDATE THIS FILE FOR DEPLOYMENT
from flask import Flask, send_from_directory,jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS 
import os

app = Flask(__name__, static_folder='../frontend/dist')

# We can comment this CORS config for the production because we are running the frontend and backend on the same server 
CORS(app, origins=["https://thankful-rock-057f0311e.6.azurestaticapps.net"])
 
 
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///friends.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db_path = '/home/data/friends.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///{db_path}"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///friends.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://username:password@localhost/notecards')

db = SQLAlchemy(app)

frontend_folder =  os.path.join(os.getcwd(),"..","frontend")
dist_folder = os.path.join(frontend_folder,"dist")

# Server static files from the "dist" folder under the "frontend" directory

@app.route("/",defaults={"filename":""})
@app.route("/<path:filename>")
@app.after_request
def after_request(response):
    # Ensure CORS headers are applied to all responses
    response.headers['Access-Control-Allow-Origin'] = 'https://thankful-rock-057f0311e.6.azurestaticapps.net'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization'
    return response

# Handle OPTIONS requests for preflight
@app.route('/api/notes', methods=['OPTIONS'])
def options_notes():
    return '', 200  # 204 No Content is also valid for preflight responses

@app.route('/api/notes', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_notes():
    # Your logic here
    return jsonify({"message": "CORS fixed!"})

def index(filename):
  if not filename:
    filename = "index.html"
  return send_from_directory(dist_folder,filename)

# api routes
import routes

with app.app_context():
  db.create_all()

# if __name__ == "__main__":
#   app.run(debug=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=False)

#This is CICD pipeline test, example.....