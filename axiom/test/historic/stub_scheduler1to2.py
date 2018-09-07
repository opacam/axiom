# test-case-name: axiom.test.historic.test_scheduler1to2

"""
Database creator for the test for the upgrade of Scheduler from version 1 to
version 2.
"""

from axiom.dependency import installOn
from axiom.scheduler import Scheduler
from axiom.test.historic.stubloader import saveStub


def createDatabase(store):
    installOn(Scheduler(store=store), store)


if __name__ == '__main__':
    saveStub(createDatabase, 17606)
