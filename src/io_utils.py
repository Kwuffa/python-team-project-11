def load_schedule_from_file(filepath: str) -> list:
    """Зчитує розклад із текстового файлу при запуску програми."""
    schedule = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                # Розбиваємо рядок на частини
                day, time, subject = line.strip().split(" | ")
                schedule.append({'day': day, 'time': time, 'subject': subject})
    except FileNotFoundError:
        print("Файл розкладу не знайдено. Починаємо з чистого аркуша!")
    except ValueError:
        print("Помилка формату даних у файлі!")
    
    return schedule

def save_schedule_to_file(filepath: str, schedule: list) -> None:
    """Зберігає весь розклад у текстовий файл."""
    with open(filepath, "w", encoding="utf-8") as f:
        for item in schedule:
            # Склеюємо словник назад у рядок
            f.write(f"{item['day']} | {item['time']} | {item['subject']}\n")

def print_menu():
    """Виводить головне меню програми."""
    print("\n--- Планувальник навчального тижня ---")
    print("1. Додати заняття")
    print("2. Переглянути весь розклад")
    print("3. Пошук за предметом")
    print("4. Вихід")
    return input("Оберіть дію: ")

def get_class_input():
    """Запитує дані у користувача."""
    day = input("День тижня: ")
    time = input("Час (напр. 08:30): ")
    subject = input("Назва предмета: ")
    return day, time, subject

def format_lesson(lesson):
    """Форматує словник заняття у зручний рядок."""
    return f"[{lesson['day']}] {lesson['time']} - {lesson['subject']}"

def display_schedule(schedule):
    """Виводить список занять на екран."""
    if not schedule:
        print("Розклад порожній.")
        return
    for item in schedule:
        print(format_lesson(item))

