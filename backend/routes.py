from app import app, db
from flask import request, jsonify
from models import Note
from datetime import datetime

# Get all notes with sorting and optional filtering
@app.route("/api/notes",methods=["GET"])
def get_notes():
  # Sort by newest first
  notes = Note.query.order_by(Note.created_at.desc()).all() 
  result = [notes.to_json() for note in notes]
  return jsonify(result)

# Create a note
@app.route("/api/notes",methods=["POST"])
def create_note():
  try:
    data = request.json

    # Validations
    required_fields = ["name","description"]
    for field in required_fields:
      if field not in data or not data.get(field):
        return jsonify({"error":f'Missing required field: {field}'}), 400

    name = data.get("name")
    # role = data.get("role")
    description = data.get("description")
    # gender = data.get("gender")
    img_url = data.get("imgUrl")

    # Fetch avatar image based on gender
    # if gender == "male":
    #   img_url = f"https://avatar.iran.liara.run/public/boy?username={name}"
    # elif gender == "female":
    #   img_url = f"https://avatar.iran.liara.run/public/girl?username={name}"
    # else:
    

    # new_friend = Note(name=name, role=role, description=description, gender= gender, img_url=img_url)
    new_note= Note(name=name, description=description, img_url=img_url)

    db.session.add(new_note) 
    db.session.commit()

    return jsonify(new_note.to_json()), 201
    
  except Exception as e:
    db.session.rollback()
    return jsonify({"error":str(e)}), 500
  
# Delete a note
@app.route("/api/notes/<int:id>",methods=["DELETE"])
def delete_note(id):
  try:
    note = Note.query.get(id)
    if note is None:
      return jsonify({"error":"Note not found"}), 404
    
    db.session.delete(note)
    db.session.commit()
    return jsonify({"msg":"Note deleted"}), 200
  except Exception as e:
    db.session.rollback()
    return jsonify({"error":str(e)}),500
  
# Update a note
@app.route("/api/notes/<int:id>",methods=["PATCH"])
def update_friend(id):
  try:
    note = Note.query.get(id)
    if note is None:
      return jsonify({"error":"Note not found"}), 404
    
    data = request.json

    note.name = data.get("name",note.name)
    # not1.role = data.get("role",not1.role)
    note.description = data.get("description",note.description)
    # friend.gender = data.get("gender",friend.gender)

    db.session.commit()
    return jsonify(note.to_json()),200
  except Exception as e:
    db.session.rollback()
    return jsonify({"error":str(e)}),500

