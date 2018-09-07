# -*- test-case-name: axiom.test.test_upgrading.DeletionTest.testPowerups -*-

from axiom.attributes import integer
from axiom.item import Item


class Obsolete(Item):
    """
    This is an obsolete class that will be destroyed in the upcoming version.
    """
    typeName = 'test_upgrading_obsolete'
    nothing = integer()
