"""
Поведенческий паттерн - итератор.

О паттерне:
    Паттерн позволяет итеративно обходить связанные объекты. При этом не
    известно сколько этих объектов находится в связке.

Пример:
    В качестве примера рассмотрим итератор связанного списка. В питоне
    итератором является сам итератор, а также генератор. Обходить связанный
    список следовательно будем двумя способами. Реализуем:
        - итератор, через методы __iter__ и __next__
        - итератор, как генератор
"""
