import pytest

from app.main import OnlineCourse


class OnlineClass(OnlineCourse):
    pass


@pytest.mark.parametrize(
    "name,description,weeks",
    [
        ("Python Basics", "The first Python course you pass", 2),
        ("Python Basics Extended", "You will learn how to write code in Python", 3),
        ("Python Core", "The best course ever", 4),
    ],
)
def test_constructor(name, description, weeks):
    course = OnlineCourse(name=name, description=description, weeks=weeks)
    assert course.name == name, (
        f"Course should have 'name' equal to {name} "
        f"when course is created with "
        f"'OnlineCourse(name={name}, description={description}, weeks={weeks})'"
    )

    assert course.description == description, (
        f"Course should have 'description' equal to {description} "
        f"when course is created with "
        f"'OnlineCourse(name={name}, description={description}, weeks={weeks})'"
    )

    assert course.weeks == weeks, (
        f"Course should have 'weeks' equal to {weeks} "
        f"when course is created with "
        f"'OnlineCourse(name={name}, description={description}, weeks={weeks})'"
    )


@pytest.mark.parametrize(
    "days,weeks",
    [
        (1, 1),
        (6, 1),
        (7, 1),
        (8, 2),
        (12, 2),
        (14, 2),
        (15, 3),
        (70, 10),
        (71, 11),
        (121, 18),
    ],
)
def test_days_to_weeks(days, weeks):
    assert OnlineCourse.days_to_weeks(days) == weeks, (
        f"Staticmethod 'days_to_weeks' should return {weeks} "
        f"when 'days' is equal to {days}"
    )


@pytest.mark.parametrize(
    "dictionary,name,description,weeks",
    [
        (
            {
                "name": "Python Basics",
                "description": "The best course to start learning Python!",
                "days": 13,
            },
            "Python Basics",
            "The best course to start learning Python!",
            2,
        ),
        (
            {
                "name": "Python Basics Extended",
                "description": "After this course you will know everything about Python data types",
                "days": 16,
            },
            "Python Basics Extended",
            "After this course you will know everything about Python data types",
            3,
        ),
        (
            {
                "name": "Python Core",
                "description": "My favourite course",
                "days": 28,
            },
            "Python Core",
            "My favourite course",
            4,
        ),
    ],
)
def test_from_dict_method(dictionary, name, description, weeks):
    course = OnlineCourse.from_dict(dictionary)
    assert course.name == name, (
        f"Course should have 'name' equal to {name} "
        f"when course is created with "
        f"'OnlineCourse.from_dict({dictionary})'"
    )

    assert course.description == description, (
        f"Course should have 'description' equal to {description} "
        f"when course is created with "
        f"'OnlineCourse.from_dict({dictionary})'"
    )

    assert course.weeks == weeks, (
        f"Course should have 'weeks' equal to {weeks} "
        f"when course is created with "
        f"'OnlineCourse.from_dict({dictionary})'"
    )


@pytest.mark.parametrize(
    "dictionary,name,description,weeks",
    [
        (
            {
                "name": "Python Basics",
                "description": "The best course to start learning Python!",
                "days": 13,
            },
            "Python Basics",
            "The best course to start learning Python!",
            2,
        ),
    ],
)
def test_should_return_cls_instance(dictionary, name, description, weeks):
    online_class = OnlineClass.from_dict(dictionary)

    assert (
        online_class.__class__.__name__ == "OnlineClass"
    ), "Method 'from_dict' should return 'cls' instance"
    assert online_class.name == name, (
        f"Course should have 'name' equal to {name} "
        f"when course is created with "
        f"'OnlineCourse.from_dict({dictionary})'"
    )

    assert online_class.description == description, (
        f"Course should have 'description' equal to {description} "
        f"when course is created with "
        f"'OnlineCourse.from_dict({dictionary})'"
    )

    assert online_class.weeks == weeks, (
        f"Course should have 'weeks' equal to {weeks} "
        f"when course is created with "
        f"'OnlineCourse.from_dict({dictionary})'"
    )
