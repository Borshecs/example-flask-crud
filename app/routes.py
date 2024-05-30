from flask import render_template, request, redirect, jsonify, url_for
from app import app, db
from app.models import Character, Weapon, Spell, Characteristic, Skill, CreatorAccount
@app.route('/')
@app.route('/index')
    # entries = [
    #     {
    #         'id' : 1,
    #         'title': 'test title 1',
    #         'description' : 'test desc 1',
    #         'status' : True
    #     },
    #     {
    #         'id': 2,
    #         'title': 'test title 2',
    #         'description': 'test desc 2',
    #         'status': False
    #     }
    # ]
def index():
    characters = Character.query.all()
    spells = Spell.query.all()
    weapons = Weapon.query.all()
    characteristics = Characteristic.query.all()
    skills = Skill.query.all()

    return render_template('index.html', 
                           characters=characters, 
                           spells=spells, 
                           weapons=weapons, 
                           characteristics=characteristics, 
                           skills=skills)
# Получение информации о доступных классах персонажей
@app.route('/classes', methods=['GET'])
def get_classes():
    classes = ['Warrior', 'Wizard', 'Rogue', 'Ranger', 'Sorcerer', 'Paladin']  # Пример доступных классов
    return jsonify({'classes': classes})

# Получение информации о доступных расах персонажей
@app.route('/races', methods=['GET'])
def get_races():
    races = ['Human', 'Elf', 'Dwarf', 'Orc', 'Undead', 'Gnome']  # Пример доступных рас
    return jsonify({'races': races})

# Получение информации о доступном оружии


@app.route('/spellsAdd', methods=['POST'])
def create_spell():
    data = request.get_json()
    new_spell = Spell(
        description=data['description'],
        impact=data['impact'],
        difficulty_level=data['difficulty_level']
    )
    db.session.add(new_spell)
    db.session.commit()
    return jsonify({'message': 'Spell created successfully'}), 201



# Получение информации о доступных заклинаниях
@app.route('/spells', methods=['GET'])
def get_spells():
    spells = Spell.query.all()  # Получение всех записей о заклинаниях из базы данных
    spells_list = [{'id': spell.id, 'description': spell.description} for spell in spells]  # Преобразование в список словарей
    return jsonify({'spells': spells_list})

# Получение информации о доступных характеристиках
@app.route('/characteristics', methods=['GET'])
def get_characteristics():
    characteristics = Characteristic.query.all()  # Получение всех записей о характеристиках из базы данных
    characteristics_list = [{'id': characteristic.id, 'name': characteristic.name} for characteristic in characteristics]  # Преобразование в список словарей
    return jsonify({'characteristics': characteristics_list})

# Получение информации о доступных навыках
@app.route('/skills', methods=['GET'])
def get_skills():
    skills = Skill.query.all()  # Получение всех записей о навыках из базы данных
    skills_list = [{'id': skill.id, 'name': skill.name} for skill in skills]  # Преобразование в список словарей
    return jsonify({'skills': skills_list})

# Получение информации о персонаже по его ID
@app.route('/characters/<int:id>', methods=['GET'])
def get_character(id):
    character = Character.query.get(id)  # Получение персонажа по его ID из базы данных
    if character:
        return jsonify({'id': character.id, 'name': character.name, 'age': character.age, 'description': character.description,
                        'active': character.active, 'gender': character.gender, 'race': character.race, 'char_class': character.char_class,
                        'creator_id': character.creator_id})
    else:
        return jsonify({'message': 'Character not found'}), 404

# Создание нового персонажа
@app.route('/characters', methods=['POST'])
def create_character():
    data = request.get_json()
    name = data.get('name')
    age = data.get('age')
    description = data.get('description')
    active = data.get('active', True)  # По умолчанию персонаж активен
    gender = data.get('gender')
    race = data.get('race')
    char_class = data.get('char_class')
    creator_id = data.get('creator_id')

    if not name or not age or not gender or not race or not char_class or not creator_id:
        return jsonify({'message': 'Missing required fields'}), 400

    character = Character(name=name, age=age, description=description, active=active, gender=gender,
                          race=race, char_class=char_class, creator_id=creator_id)
    db.session.add(character)
    db.session.commit()

    return jsonify({'message': 'Character created successfully'}), 201

# Обновление информации о персонаже по его ID
@app.route('/characters/<int:id>', methods=['PUT'])
def update_character(id):
    character = Character.query.get(id)
    if not character:
        return jsonify({'message': 'Character not found'}), 404

    data = request.get_json()
    character.name = data.get('name', character.name)
    character.age = data.get('age', character.age)
    character.description = data.get('description', character.description)
    character.active = data.get('active', character.active)
    character.gender = data.get('gender', character.gender)
    character.race = data.get('race', character.race)
    character.char_class = data.get('char_class', character.char_class)
    character.creator_id = data.get('creator_id', character.creator_id)

    db.session.commit()

    return jsonify({'message': 'Character updated successfully'})

# Удаление персонажа по его ID
@app.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    character = Character.query.get(id)
    if not character:
        return jsonify({'message': 'Character not found'}), 404

    db.session.delete(character)
    db.session.commit()

    return jsonify({'message': 'Character deleted successfully'})


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_character(id):
    character = Character.query.get(id)
    if request.method == 'POST':
        character.name = request.form['name']
        character.age = request.form['age']
        character.description = request.form['description']
        character.gender = request.form['gender']
        character.race = request.form['race']
        character.char_class = request.form['char_class']
        character.creator_id = request.form['creator_id']
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('edit_character.html', character=character)

@app.route('/spell/<int:id>', methods=['DELETE'])
def delete_spell(id):
    spell = Spell.query.get(id)
    if not spell:
        return jsonify({'message': 'Character not found'}), 404

    db.session.delete(spell)
    db.session.commit()

    return jsonify({'message': 'Character deleted successfully'})

@app.route('/weapons', methods=['POST'])
def weapons():
    if request.method == 'POST':
        data = request.json
        new_weapon = Weapon(
            type=data['type'],
            skill_rate=data['skill_rate'],
            players_rate=data['players_rate'],
            quest=data.get('quest', True)
        )
        db.session.add(new_weapon)
        db.session.commit()
        return jsonify(message='Weapon created successfully'), 201
    
@app.route('/weapons/<int:id>', methods=['DELETE'])
def delete_weapon(id):
    weapon = Weapon.query.get(id)
    if not weapon:
        return jsonify({'message': 'Weapon not found'}), 404

    db.session.delete(weapon)
    db.session.commit()

    return jsonify({'message': 'Weapon deleted successfully'}), 200

@app.route('/weapons', methods=['GET'])
def get_all_weapons():
    weapons = Weapon.query.all()
    weapons_list = [{'id': weapon.id, 'type': weapon.type} for weapon in weapons]
    return jsonify({'weapons': weapons_list})



# Characteristics
@app.route('/characteristics', methods=['POST'])
def create_characteristic():
    data = request.json
    new_characteristic = Characteristic(name=data['name'])
    db.session.add(new_characteristic)
    db.session.commit()
    return jsonify({'message': 'Characteristic created'}), 201

@app.route('/characteristics/<int:id>', methods=['DELETE'])
def delete_characteristic(id):
    characteristic = Characteristic.query.get_or_404(id)
    db.session.delete(characteristic)
    db.session.commit()
    return jsonify({'message': 'Characteristic deleted'}), 200

# Skills
@app.route('/skills', methods=['POST'])
def create_skill():
    data = request.json
    new_skill = Skill(name=data['name'])
    db.session.add(new_skill)
    db.session.commit()
    return jsonify({'message': 'Skill created'}), 201

@app.route('/skills/<int:id>', methods=['DELETE'])
def delete_skill(id):
    skill = Skill.query.get_or_404(id)
    db.session.delete(skill)
    db.session.commit()
    return jsonify({'message': 'Skill deleted'}), 200