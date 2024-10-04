"""
Структурный паттерн проектирования - фасад.

О паттерне:
    Паттерн позволяет скрыть сложность системы и упростить использование
    API для пользователя. Паттерн использует агрегацию компонентов системы
    и может предоставлять клиенту, как общий интерфейс для взаимодействия с
    системой, так и отдельные компоненты.

Когда использовать:
    - если требуется уменьшить связанность клиента и компонентов системы
    - если требуется упростить взаимодействие клиента с системой
    - если требуется создать подсистемы из компонентов системы, здесь
    фасад верхнего уровня будет клиентом фасада уровнем ниже

Пример:
    Рассмотрим систему по загрузке файлов. Что хочет пользователь -
    ввести индекс файла и загрузить файл на диск. Сам файл находится в
    хранилище, путь к файлу в хранилище записан в БД под целочисленным
    индексом.

    Компоненты системы:
        - менеджер БД
        - менеджер хранилища
        - менеджер ФС

    Интерфейс менеджера БД:
        - получить путь к файлу по его индексу

    Интерфейс менеджера хранилища:
        - получить файл по его пути

    Интерфейс менеджера файловой системы:
        - записать полученный файл на диск

    Интерфейс фасада:
        - загрузить файл

"""
