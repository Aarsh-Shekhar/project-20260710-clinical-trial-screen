import unittest

from clinical_trial_screen.models import Record
from clinical_trial_screen.scoring import score_record


class DepthCheck2(unittest.TestCase):
    def test_002_operator_handoff(self):
        record = Record(id="candidate-002", exposure=8543, signal=0.590, urgency=3)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
