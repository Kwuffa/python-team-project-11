from io_utils import print_menu, get_class_input, display_schedule, load_schedule_from_file, save_schedule_to_file
from planner_logic import add_class, search_lessons

def main():
    filepath = "data/schedule.txt"
    
    # Завантажуємо дані при старті програми
    schedule = load_schedule_from_file(filepath)
    
    while True:
        choice = print_menu()
        
        if choice == '1':
            day, time, subject = get_class_input()
            
            # Запам'ятовуємо довжину розкладу ДО додавання
            old_length = len(schedule)
            
            schedule = add_class(schedule, day, time, subject)
            
            # Якщо довжина змінилася, значить заняття додалося
            if len(schedule) > old_length:
                save_schedule_to_file(filepath, schedule)
                print("✅ Заняття успішно додано та збережено у файл!")
            else:
                print("❌ Помилка: Заняття не додано (можливо, порожня назва).")
            
        elif choice == '2':
            display_schedule(schedule)
            
        elif choice == '3':
            query = input("Введіть назву предмета для пошуку: ")
            results = search_lessons(schedule, query)
            if results:
                print("\nЗнайдені заняття:")
                display_schedule(results)
            else:
                print("Нічого не знайдено.")
                
        elif choice == '4':
            print("Вихід з програми...")
            break
        else:
            print("❌ Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()