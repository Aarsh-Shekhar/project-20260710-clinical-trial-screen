import unittest

from clinical_trial_screen.models import Record
from clinical_trial_screen.scoring import score_record


class DepthCheck38(unittest.TestCase):
    def test_038_field_validation(self):
        record = Record(id="candidate-038", exposure=74005, signal=0.767, urgency=2)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
