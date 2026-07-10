import unittest

from clinical_trial_screen.models import Record
from clinical_trial_screen.scoring import score_record


class DepthCheck50(unittest.TestCase):
    def test_050_threshold_calibration(self):
        record = Record(id="candidate-050", exposure=60075, signal=0.492, urgency=7)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
