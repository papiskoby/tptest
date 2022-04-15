from module import Person, Wizard, HealthPotion
from main import main

def test_person_initial_amount():
    person = Person('user1')
    assert person.life_points == 100

def test_wizard_initial_amount():
    wizard = Wizard('user2')
    assert wizard.life_points == 80

def test_person_hit_amount():
    person = Person('user1')
    wizard = Wizard('user2')
    person.hit(wizard)
    assert wizard.life_points == 70

def test_wizard_hit_amount():
    person = Person('user1')
    wizard = Wizard('user2')
    wizard.hit(person)
    assert person.life_points == 85

def test_gained_amount():
    person = Person('user1')
    wizard = Wizard('user2')
    person.gained_life_points(10)
    assert person.life_points == 110

def test_isdead_amount():
    person = Person('user1')
    wizard = Wizard('user2')
    while person.life_points >= 0:
        wizard.hit(person)
    assert person.is_dead() == True


def test_app():
    result=main()
    assert result in ['Hero wins','Wizard wins']

