
from twisted.trial.unittest import TestCase

from axiom.store import Store
from axiom.item import Item
from axiom.attributes import integer, ieee754_double, ConstraintError

import random

class Number(Item):
    typeName = 'test_number'
    schemaVersion = 1

    value = ieee754_double()


class IEEE754DoubleTest(TestCase):

    def testRoundTrip(self):
        s = Store()
        Number(store=s, value=7.1)
        n = s.findFirst(Number)
        self.assertEquals(n.value, 7.1)

class SpecialStoreIDAttributeTest(TestCase):

    def testStringStoreIDsDontWork(self):
        s = Store()
        sid = Number(store=s, value=1.0).storeID
        self.assertRaises(TypeError, s.getItemByID, str(sid))
        self.assertRaises(TypeError, s.getItemByID, float(sid))
        self.assertRaises(TypeError, s.getItemByID, unicode(sid))

class SortedItem(Item):
    typeName = 'test_sorted_thing'
    schemaVersion = 1

    goingUp = integer()
    goingDown = integer()
    theSame = integer()

class SortingTest(TestCase):

    def testCompoundSort(self):
        s = Store()
        L = []
        r10 = range(10)
        random.shuffle(r10)
        L.append(SortedItem(store=s,
                            goingUp=0,
                            goingDown=1000,
                            theSame=8))
        for x in r10:
            L.append(SortedItem(store=s,
                                goingUp=10+x,
                                goingDown=10-x,
                                theSame=7))

        for colnms in [['goingUp'],
                       ['goingUp', 'storeID'],
                       ['goingUp', 'theSame'],
                       ['theSame', 'goingUp'],
                       ['theSame', 'storeID']]:
            LN = L[:]
            LN.sort(key=lambda si: tuple([getattr(si, colnm) for colnm in colnms]))

            ascsort = [getattr(SortedItem, colnm).ascending for colnm in colnms]
            descsort = [getattr(SortedItem, colnm).descending for colnm in colnms]

            self.assertEquals(LN, list(s.query(SortedItem,
                                               sort=ascsort)))
            LN.reverse()
            self.assertEquals(LN, list(s.query(SortedItem,
                                               sort=descsort)))


class FunkyItem(Item):
    name = unicode()

class BadAttributeTest(TestCase):

    def testBadAttribute(self):
        s = Store()
        self.failUnlessRaises(AttributeError, FunkyItem, store=s,name=u"foo")