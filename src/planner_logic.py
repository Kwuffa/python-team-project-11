def create_lesson(day, time, subject):
    """
    Створює словник заняття.
    Проводить валідацію та очищення вхідних текстових даних.

    :param day: День тижня
    :param time: Час заняття
    :param subject: Назва предмета
    :return: Словник із ключами 'day', 'time', 'subject' та значеннями за замовчуванням
    """
    # Відповідність скорочень до повних назв
    days_map = {
        "пн": "Понеділок",
        "понеділок": "Понеділок",
        "вт": "Вівторок",
        "вівторок": "Вівторок",
        "ср": "Середа",
        "середа": "Середа",
        "чт": "Четвер",
        "четвер": "Четвер",
        "пт": "П'ятниця",
        "пʼятниця": "П'ятниця",
        "пятниця": "П'ятниця",
        "сб": "Субота",
        "субота": "Субота",
        "нд": "Неділя",
        "неділя": "Неділя"
    }

    # Готуємо дані: перетворюємо на рядок та чистимо пробіли
    d = str(day).strip().lower()
    t = str(time).strip().replace(".", ":")
    s = str(subject).strip()

    # Перетворюємо день у повну назву
    full_day = days_map.get(d, "Не вказано")

    # Повертаємо словник із перевіреними значеннями
    return {
        'day': full_day,
        'time': t if t else "--:--",
        'subject': s if s else "Без назви"
    }


def add_class(schedule, day, time, subject):
    """
    Додає нове заняття до загального розкладу.

    :param schedule: Список словників, що представляє поточний розклад
    :param day: День тижня
    :param time: Час заняття
    :param subject: Назва предмета
    :return: Оновлений список розкладу
    """
    try:
        # Створюємо нове заняття
        new_lesson = create_lesson(day, time, subject)

        # Додаємо заняття лише якщо назва предмета не порожня
        if new_lesson['subject'] != "Без назви":
            schedule.append(new_lesson)
        return schedule

    except Exception as e:
        print(f"Помилка при додаванні заняття: {e}")
        return schedule


def search_lessons(schedule, query):
    """
    Шукає збіги у розкладі за назвою предмета.

    :param schedule: Список словників із заняттями
    :param query: Рядок для пошуку
    :return: Список знайдених занять, що відповідають запиту
    """
    try:
        # Перевірка, чи не порожній запит прийшов від користувача
        if not query or not str(query).strip():
            return []

        search_query = query.lower().strip()
        results = []

        # Перевіряємо чи є запит в списку
        for lesson in schedule:
            if lesson['subject'] != "Без назви" and search_query in lesson['subject'].lower():
                results.append(lesson)
        return results

    except Exception as e:
        print(f"Помилка пошуку занять: {e}")
        return []
