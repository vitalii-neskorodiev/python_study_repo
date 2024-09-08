from lesson_16.part_1.employee import TeamLead
from assertpy import assert_that


class TestEmployee:
    qa_automation_team_lead: TeamLead = TeamLead("Mark", 5000, "Best Department", 5)

    expected_mark_attrs: dict[str, object] = {
        "name": "Mark",
        "salary": 5000,
        "department": "Best Department",
        "team_size": 5
    }

    def test_employee_attrs(self):
        print(self.qa_automation_team_lead.__dict__)

        (assert_that(self.qa_automation_team_lead, "Desired user's attrs are not equal desired dict attrs")
         .is_equal_to(self.expected_mark_attrs))
