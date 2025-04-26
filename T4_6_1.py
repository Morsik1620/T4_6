import random
import timeit


# Напишите класс Queue, который реализует основные операции очереди: enqueue (добавление элемента), dequeue (удаление
# элемента), is_empty (проверка, пуста ли очередь) и peek (просмотр первого элемента в очереди)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, items):
        self.items.append(items)

    def dequeue(self): # удалить элемент из начала очереди
        if not self.is_empty():
            return self.items.pop(0)

    def peek (self):
        if not self.is_empty():
            return self.items[0]

    def size(self):
        return len(self.items)

#queue = Queue()

#queue.enqueue(10)
#queue.enqueue("test")
#queue.enqueue(True)
#print(queue.is_empty())
#print(queue.peek())
#print(queue.size())
#queue.dequeue()
#print(queue.peek())
#print(queue.size())

# Смоделируйте простой процесс обработки задач в очереди. Допустим, у вас есть список задач, каждая из которых занимает
# определенное время на выполнение. Используйте очередь для обработки задач и выводите время, когда каждая задача будет
# завершена

def simulate_task_processing(tasks):
    task_queue = Queue()
    for task_name, task_duration in tasks:
        task_queue.enqueue((task_name, task_duration)) # добавляю задачу в очередь

    current_time = 0
    print("Начало обработки задач...")

    while not task_queue.is_empty(): # запустить цикл пока задачи не закончатся
        task, duration = task_queue.dequeue() # : Удаляет и возвращает первый элемент из очереди и записываем в переменные
        current_time += duration # прибавляем значение duration к текущему значению переменной current_time
        print(f"Задача '{task}' завершена в {current_time} единиц времени.")

    print("Обработка всех задач завершена.")


# Пример использования
tasks = [
    ("Распланировать день", 10),
    ("Провести переговоры", 20),
    ("Закупить билеты", 30),
    ("Выбрать гостиницу", 20),
]

simulate_task_processing(tasks)


# Напишите функцию для реализации сортировки слиянием (MergeSort) с примером использования

def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        MergeSort(left_half)
        MergeSort(right_half)
        i = j = k = 0
 # Слияние двух половин
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
 # Проверка остатков
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


list_sizes = [10, 100, 1000] # Размеры списков для тестирования
def MergeSort_time(arr):
    MergeSort(arr.copy())  # Сортирую копию, чтобы не изменять исходный список

# Запуск тестов и вывод результатов
print("____________________________")
print("List Size | MergeSort Time |")
print("----------|----------------|")
for range_list in list_sizes:
    arr = [random.randint(0, 1000) for _ in range(range_list)] # создаю список случайных чисел
#    print("Исходный массив:",arr)
    MergeSort_time_take = timeit.timeit(stmt = lambda: MergeSort_time(arr), number=1000) # Измеряем время выполнения линейного поиска
#    print("Отсортированный массив:", MergeSort(arr))

    print(f"{range_list:10}| {MergeSort_time_take:15f}|")