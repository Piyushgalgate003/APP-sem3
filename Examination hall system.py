class Student:
    def __init__(self, name: str, roll_number: str, hall_number: int):
        self.name = name
        self.roll_number = roll_number
        self.hall_number = hall_number
        self.block = self._assign_block(hall_number)

    def _assign_block(self, hall_number: int) -> str:
        if 101 <= hall_number <= 110:
            return "Block A"
        elif 111 <= hall_number <= 120:
            return "Block B"
        else:
            return "Block C"

    def display_info(self):
        print(f"| {self.roll_number:<12} | {self.name:<20} | Hall {self.hall_number:<5} | {self.block:<8} |")


class ExamHall:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def display_seating_arrangement(self):
        if not self.students:
            print("No student records found.")
            return

        print("\n" + "=" * 56)
        print("            EXAMINATION HALL SEATING ARRANGEMENT         ")
        print("=" * 56)
        print(f"| {'Roll Number':<12} | {'Student Name':<20} | {'Hall No':<8} | {'Block':<8} |")
        print("-" * 56)
        for student in self.students:
            student.display_info()
        print("=" * 56)

    @staticmethod
    def unique_paths(m: int, n: int) -> int:
        dp = [[1] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]


if __name__ == "__main__":
    hall_system = ExamHall()

    hall_system.add_student(Student("Aarav Sharma", "21CS001", 102))
    hall_system.add_student(Student("Priya Patel", "21CS002", 115))
    hall_system.add_student(Student("Rohan Verma", "21CS003", 125))

    hall_system.display_seating_arrangement()

    rows, cols = 3, 3
    paths = hall_system.unique_paths(rows, cols)
    print(f"\n[DP] Unique paths to cross an {rows}x{cols} exam hall grid: {paths}")