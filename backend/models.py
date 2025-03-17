from app import db
from datetime import datetime

class Note(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  # role = db.Column(db.String(50), nullable=False)
  description = db.Column(db.Text, nullable=False)
  # gender = db.Column(db.String(10), nullable=False)
  img_url = db.Column(db.String(200), nullable=True)
  created_at = db.Column(db.DateTime, default=datetime.now)
  updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)


  def to_json(self):
    return {
      "id":self.id,
      "name":self.name,
      # "role":self.role,
      "description":self.description,
      # "gender":self.gender,
      "imgUrl":self.img_url,
      "createdAt": self.created_at.isoformat() if self.created_at else None,
      "updatedAt": self.updated_at.isoformat() if self.updated_at else None
    }

 