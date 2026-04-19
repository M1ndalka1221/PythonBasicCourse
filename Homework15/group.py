from exceptions import GroupLimitError

class Group:

    def __init__(self, number, group_limit=10):
        self.number = number
        self.group = set()
        if group_limit <= 0:
            raise ValueError(f"Limit of the group must be greater than 0.")

        self.group_limit = group_limit

    def add_student(self, student):
        self.group.add(student)
        if len(self.group) >= self.group_limit:
            raise GroupLimitError(f"Can't add more than {self.group_limit} students.")

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete is not None:
            self.group.remove(student_to_delete)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n '.join([str(student) for student in self.group])
        return f'Number:{self.number}\n {all_students} '
