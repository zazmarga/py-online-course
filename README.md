# Online Course

- Read [the guideline](https://github.com/mate-academy/py-task-guideline/blob/main/README.md) before start

We want to create a website for finding the best online courses.
In order to store information about courses, we need a new `OnlineCourse` class.
Could you implement it for us?

`OnlineCourse` `__init__` method takes three arguments:
* `name` - course name (should be stored in `self.name`)
* `description` - course description (should be stored in `self.description`)
* `weeks` - duration of the course in weeks (should be stored in `self.weeks`)

```python
course = OnlineCourse(
    name="Python Basics",
    description="The best course to start learning Python",
    weeks=2,
)
print(course.description)  # The best course to start learn Python
```

Often we will receive information about the course in the form of a `course_dict` dictionary 
with such fields:
* `course_dict["name"]` - course name
* `course_dict["description"]` - course description
* `course_dict["days"]` - duration of the course in days

To convert course duration to weeks, `OnlineCourse` should have `days_to_weeks` **staticmethod**, 
that takes one argument `days` and convert this number to weeks.

Note: The last week may not be whole.

Example:
```python
OnlineCourse.days_to_weeks(10) == 2
OnlineCourse.days_to_weeks(14) == 2
OnlineCourse.days_to_weeks(15) == 3
```

`OnlineCourse` should have `from_dict` **classmethod**. It should take 
two parameters: 
* `cls` - a default parameter for classmethod 
* `course_dict` - a dictionary described above

Method should return a new instance of `OnlineCourse` with correct attributes.
It should use `days_to_weeks` method to convert days to weeks.
Example:
```python
course_dict = {
    "name": "Python Core",
    "description": "After this course you will know everything about Python",
    "days": 12,
}
python_course = OnlineCourse.from_dict(course_dict)
print(python_course.weeks)  # 2
```
