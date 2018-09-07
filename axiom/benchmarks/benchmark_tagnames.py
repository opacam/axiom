"""
Benchmark the tagNames method of L{axiom.tags.Catalog}
"""

from axiom import store, item, attributes, tags
from epsilon.scripts import benchmark

N_TAGS = 20
N_COPIES = 5000
N_LOOPS = 1000


class TaggedObject(item.Item):
    name = attributes.text()


def main():
    s = store.Store("tags.axiom")
    c = tags.Catalog(store=s)
    o = TaggedObject(store=s)

    def tagObjects(tag, copies):
        for x in range(copies):
            c.tag(o, tag)

    for i in range(N_TAGS):
        s.transact(tagObjects, str(i), N_COPIES)

    def getTags():
        for i in range(N_LOOPS):
            list(c.tagNames())

    benchmark.start()
    s.transact(getTags)
    benchmark.stop()


if __name__ == '__main__':
    main()
