import unittest

from clinical_trial_screen.models import Record
from clinical_trial_screen.scoring import score_record


class DepthCheck35(unittest.TestCase):
    def test_035_backlog_triage(self):
        record = Record(id="candidate-035", exposure=93959, signal=0.751, urgency=7)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
