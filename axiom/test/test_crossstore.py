from twisted.python import filepath
from twisted.trial.unittest import TestCase

from axiom.attributes import integer
from axiom.item import Item
from axiom.store import Store
from axiom.substore import SubStore


class ExplosiveItem(Item):
    nothing = integer()

    def yourHeadAsplode(self):
        1 / 0


class CrossStoreTest(TestCase):

    def setUp(self):
        self.spath = filepath.FilePath(self.mktemp() + ".axiom")
        self.store = Store(self.spath)
        self.substoreitem = SubStore.createNew(self.store,
                                               ["sub.axiom"])

        self.substore = self.substoreitem.open()
        # Not available yet.
        self.substore.attachToParent()


class TestCrossStoreTransactions(CrossStoreTest):

    def testCrossStoreTransactionality(self):
        def createTwoSubStoreThings():
            ExplosiveItem(store=self.store)
            ei = ExplosiveItem(store=self.substore)
            ei.yourHeadAsplode()

        self.assertRaises(ZeroDivisionError,
                          self.store.transact,
                          createTwoSubStoreThings)

        self.assertEqual(
            self.store.query(ExplosiveItem).count(),
            0)

        self.assertEqual(
            self.substore.query(ExplosiveItem).count(),
            0)


class TestCrossStoreInsert(CrossStoreTest):

    def testCrossStoreInsert(self):
        def populate(s, n):
            for i in range(n):
                ExplosiveItem(store=s)

        self.store.transact(populate, self.store, 2)
        self.store.transact(populate, self.substore, 3)

        self.assertEqual(
            self.store.query(ExplosiveItem).count(),
            2)

        self.assertEqual(
            self.substore.query(ExplosiveItem).count(),
            3)
