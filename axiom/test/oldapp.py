from axiom.attributes import text, integer, reference
from axiom.item import Item


class Player(Item):
    typeName = 'test_app_player'
    schemaVersion = 1

    name = text()
    sword = reference()


class Sword(Item):
    typeName = 'test_app_sword'
    schemaVersion = 1

    name = text()
    hurtfulness = integer()
