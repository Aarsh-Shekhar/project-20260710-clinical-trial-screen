import unittest

from clinical_trial_screen.models import Record
from clinical_trial_screen.scoring import score_record


class DepthCheck32(unittest.TestCase):
    def test_032_operator_handoff(self):
        record = Record(id="candidate-032", exposure=91087, signal=0.435, urgency=6)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
