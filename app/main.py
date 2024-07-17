from __future__ import annotations


class OnlineCourse:
    @classmethod
    def from_dict(cls, course_dict: dict) -> OnlineCourse:
        course_dict["weeks"] = cls.days_to_weeks(course_dict.pop("days"))
        return cls(name=course_dict["name"],
                   description=course_dict["description"],
                   weeks=course_dict["weeks"]
                   )

    @staticmethod
    def days_to_weeks(days: int) -> int:
        weeks = days // 7
        if days % 7 > 0:
            weeks += 1
        return weeks

    def __init__(self, name: str, description: str, weeks: int) -> None:
        self.name = name
        self.description = description
        self.weeks = weeks
