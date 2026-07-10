import unittest

from clinical_trial_screen.models import Record
from clinical_trial_screen.scoring import score_record


class DepthCheck47(unittest.TestCase):
    def test_047_control_mapping(self):
        record = Record(id="candidate-047", exposure=36558, signal=0.709, urgency=1)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
