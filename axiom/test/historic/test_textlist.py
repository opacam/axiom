from axiom.test.historic.stub_textlist import Dummy
from axiom.test.historic.stubloader import StubbedTest


class TextlistTransitionTest(StubbedTest):
    def test_transition(self):
        """
        Test that the textlist survives the encoding transition intact.
        """
        d = self.store.findUnique(Dummy)
        self.assertEqual(d.attribute, ['foo', 'bar'])
