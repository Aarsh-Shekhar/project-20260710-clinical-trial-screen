import unittest

from clinical_trial_screen.models import Record
from clinical_trial_screen.scoring import score_record


class DepthCheck41(unittest.TestCase):
    def test_041_edge_case_review(self):
        record = Record(id="candidate-041", exposure=33325, signal=0.447, urgency=5)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
