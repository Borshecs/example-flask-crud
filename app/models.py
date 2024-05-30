from app import db

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(1000))
    active = db.Column(db.Boolean, default=True)
    gender = db.Column(db.String(10), nullable=False)
    race = db.Column(db.String(50), nullable=False)
    char_class = db.Column(db.String(50), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('creator_account.id'), nullable=False)

class Weapon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50), nullable=False)
    skill_rate = db.Column(db.Integer, nullable=False)
    players_rate = db.Column(db.Integer, nullable=False)
    quest = db.Column(db.Boolean, default=True)

class Spell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(1000), nullable=False)
    impact = db.Column(db.Text, nullable=False)
    difficulty_level = db.Column(db.Integer, nullable=False)

class Characteristic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class CreatorAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator_name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
