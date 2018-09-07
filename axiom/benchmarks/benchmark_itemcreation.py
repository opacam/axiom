"""
Benchmark creation of a large number of simple Items in a transaction.
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

    def txn():
        for x in range(10000):
            AB(a=x, b=str(x), store=s)

    benchmark.start()
    s.transact(txn)
    benchmark.stop()


if __name__ == '__main__':
    main()
