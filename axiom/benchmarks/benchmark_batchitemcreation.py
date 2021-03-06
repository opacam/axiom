
"""
Benchmark batch creation of a large number of simple Items in a transaction.
"""

from epsilon.scripts import benchmark

from axiom.store import Store
from axiom.item import Item
from axiom.attributes import integer, text

class AB(Item):
    a = integer()
    b = text()

def main():
    s = Store("TEMPORARY.axiom")
    benchmark.start()
    rows = [(x, unicode(x)) for x in xrange(10000)]
    s.transact(lambda: s.batchInsert(AB, (AB.a, AB.b), rows))
    benchmark.stop()


if __name__ == '__main__':
    main()
