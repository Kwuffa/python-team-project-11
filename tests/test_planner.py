import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from planner_logic import add_class, create_lesson, search_lessons

class TestPlannerLogic(unittest.TestCase):

    # --- Тести для create_lesson ---
    def test_create_lesson_formatting(self):
        """Перевіряє, чи функція чистить пробіли та форматує час (крапку на двокрапку)."""
        lesson = create_lesson(" Пн ", " 08.30 ", " Програмування ")
        self.assertEqual(lesson['day'], "Понеділок")
        self.assertEqual(lesson['time'], "08:30")
        self.assertEqual(lesson['subject'], "Програмування")

    def test_create_lesson_defaults(self):
        """Перевіряє роботу зі значеннями за замовчуванням при порожньому вводі."""
        lesson = create_lesson("", "", "")
        self.assertEqual(lesson['day'], "Не вказано")
        self.assertEqual(lesson['time'], "--:--")
        self.assertEqual(lesson['subject'], "Без назви")

    # --- Тести для add_class ---
    def test_add_class_success(self):
        """Перевіряє успішне додавання заняття до розкладу."""
        schedule = []
        result = add_class(schedule, "Вівторок", "10:00", "Фізика")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['subject'], "Фізика")

    def test_add_class_ignore_empty(self):
        """Перевіряє, що заняття без назви (Без назви) не додається до розкладу."""
        schedule = []
        result = add_class(schedule, "Ср", "12:00", "   ")
        self.assertEqual(len(result), 0)

    # --- Тести для search_lessons ---
    def test_search_lessons_found(self):
        """Перевіряє, що пошук повертає правильний результат при збігу."""
        schedule = [
            {'day': 'Понеділок', 'time': '08:30', 'subject': 'Вища математика'},
            {'day': 'Вівторок', 'time': '10:00', 'subject': 'Історія'}
        ]
        # Шукаємо "математика" у "Вища математика"
        results = search_lessons(schedule, "математика")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['subject'], "Вища математика")

    def test_search_lessons_empty_query(self):
        """Перевіряє, що при порожньому запиті повертається порожній список."""
        schedule = [{'day': 'Пн', 'time': '08:30', 'subject': 'Хімія'}]
        results = search_lessons(schedule, "  ")
        self.assertEqual(len(results), 0)

if __name__ == '__main__':
    unittest.main()