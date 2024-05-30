from app import app, db
from app.models import Character, Weapon, Spell, Characteristic, Skill

def add_initial_data():
    with app.app_context():
        # Пример данных для таблиц
        spells = [
            Spell(descrip="Fireball", impact="Burn", dif_lvl=3),
            Spell(descrip="Ice Blast", impact="Freeze", dif_lvl=4)
        ]
        weapons = [
            Weapon(w_type="Sword", skill_rate=80, players_rate=75, quest=True),
            Weapon(w_type="Bow", skill_rate=60, players_rate=70, quest=False)
        ]
        characteristics = [
            Characteristic(charac_name="Strength"),
            Characteristic(charac_name="Agility")
        ]
        skills = [
            Skill(skill_name="Stealth"),
            Skill(skill_name="Archery")
        ]

        # Добавление данных в базу данных
        db.session.add_all(spells)
        db.session.add_all(weapons)
        db.session.add_all(characteristics)
        db.session.add_all(skills)
        db.session.commit()
        print("Initial data added successfully.")

if __name__ == '__main__':
    add_initial_data()
