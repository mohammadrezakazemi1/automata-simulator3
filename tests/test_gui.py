import os
import unittest

os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

from PySide6.QtWidgets import QApplication
from main import MainWindow


class GuiSmokeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication.instance() or QApplication([])

    def test_window_builds_and_conversion_handlers_exist(self):
        window = MainWindow()
        self.assertTrue(hasattr(window, "load_conversion_source"))
        self.assertTrue(hasattr(window, "auto_layout_conversion_graphs"))
        self.assertTrue(hasattr(window, "convert_nfa"))
        window.close()

    def test_designer_modes_are_independent(self):
        window = MainWindow()

        window.create_state()
        dfa_machine = window.machine
        self.assertEqual(window._designer_mode, "DFA")
        self.assertEqual(len(dfa_machine.states), 1)

        window.set_designer_mode("NFA")
        self.assertEqual(window._designer_mode, "NFA")
        self.assertEqual(len(window.machine.states), 0)

        window.create_state()
        nfa_machine = window.machine
        self.assertEqual(len(nfa_machine.states), 1)

        window.set_designer_mode("DFA")
        self.assertIs(window.machine, dfa_machine)
        self.assertEqual(len(window.machine.states), 1)

        window.set_designer_mode("NFA")
        self.assertIs(window.machine, nfa_machine)
        self.assertEqual(len(window.machine.states), 1)

        window.close()


if __name__ == "__main__":
    unittest.main()
