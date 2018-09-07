"""
Benchmark batch creation of a large number of simple Items in a transaction.
"""

from axiom.attributes import integer, text
from axiom.item import Item
from axiom.store import Store
from epsilon.scripts import benchmark


class AB(Item):
    a = integer()
    b = text()


def main():
    s = Store("TEMPORARY.axiom")
    rows = [(x, str(x)) for x in range(10000)]
    s.transact(lambda: s.batchInsert(AB, (AB.a, AB.b), rows))

    def deleteStuff():
        for it in s.query(AB):
            it.deleteFromStore()

    benchmark.start()
    s.transact(deleteStuff)
    benchmark.stop()


if __name__ == '__main__':
    main()
