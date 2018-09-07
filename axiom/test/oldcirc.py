# -*- test-case-name: axiom.test.test_upgrading.DeletionTest.testCircular -*-
from axiom.attributes import reference, integer
from axiom.item import Item


class A(Item):
    typeName = 'test_circular_a'
    b = reference()


class B(Item):
    typeName = 'test_circular_b'
    a = reference()
    n = integer()
