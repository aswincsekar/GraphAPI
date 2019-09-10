from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo, RelationshipFrom, StructuredRel, DateTimeProperty)
import datetime
import pytz

config.DATABASE_URL = 'bolt://neo4j:adminpass@localhost:7687'


class Country(StructuredNode):
    code = StringProperty(unique_index=True, required=True)
    inhabitant = RelationshipFrom('Person', 'PERSONS')


class FriendRel(StructuredRel):
    since = DateTimeProperty(
        default=lambda: datetime.datetime.now(pytz.utc)
    )
    met = StringProperty()
    label = StringProperty(default='')


class Person(StructuredNode):
    uid = UniqueIdProperty()
    name = StringProperty(unique_index=True)
    age = IntegerProperty(index=True, default=0)
    friends = RelationshipTo('Person', 'FRIEND', model=FriendRel)
    country = RelationshipTo(Country, 'IS_FROM')