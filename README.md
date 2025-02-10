# Паттерны проектирования на языке Python

Здесь собраны примеры реализации паттернов проектирования. Этот репозиторий появился в процессе моего изучения самих паттернов. По мере продвижения в теме
я делал небольшие примеры для себя и решил в конце концов собрать материал в одном месте.

## Оглавление

* [Порождающие паттерны](./generating/)
  * [Абстрактная фабрика](./generating/abstract_factory/)
  * [Строитель](./generating/builder/)
  * [Фабричный метод](./generating/factory_method/)
  * [Прототип](./generating/prototype/)
  * [Одиночка](./generating/singleton/)
* [Поведенческие паттерны](./behavioral/)
  * [Цепочка обязанностей](./behavioral/chain/)
  * [Команда](./behavioral/command/)
  * [Интерпретатор](./behavioral/interpreter/)
  * [Итератор](./behavioral/iterator/)
  * [Посредник](./behavioral/mediator/)
  * [Хранитель](./behavioral/memento/)
  * [Наблюдатель](./behavioral/observer/)
  * [Состояние](./behavioral/state/)
  * [Стратегия](./behavioral/strategy/)
  * [Шаблонный метод](./behavioral/template_method/)
  * [Посетитель](./behavioral/visitor/)
* [Структурные паттерны](./structural/)
  * [Адаптер](./structural/adapter/)
  * [Компоновщик](./structural/composite/)
  * [Декоратор](./structural/decorator/)
  * [Фасад](./structural/facade/)
  * [Прокси](./structural/proxy/)

## Структура проекта

Проект тематически разделен на пакеты, которые отражают типы паттернов - порождающие, поведенческие и структурные соответственно. В иерархии проекта
это выглядит так:

* `generating` - пакет порождающих паттернов;
* `behavioral` - пакет поведенческих паттернов;
* `structural` - пакет структурных паттернов.

Сами паттерны также являются пакетами внутри каждой из категорий. Структура
пакета с паттерном выглядит следующим образом:

* `__init__.py` - файл верхнего уровня в пакете паттерна, содержит общее описание. Также может содержать формальное описание примера;
* `examples` - пакет с примером, здесь представлено использование паттерна;
  * `example.py` - модуль в котором реализовано использование конкретного паттерна. Важное замечание - иногда описывая пример можно было бы применить несколько паттернов, но акцент сделан только на конкретном;
* `pattern` - пакет с реализацией самого паттерна;
  * `abc.py` - модуль с интерфейсом конкретного паттерна;
  * `base.py` - модуль с реализацией базовых сущностей для примеров. Здесь может быть реализован например базовый класс от которого будут наследоваться другие классы в пакете `examples`.

## Как читать модуль `example.py`

Если в модуле требуется определить какие-либо сущности, через наследование от базовых, то они декларируются сразу после директивы импорта. Как это выглядит на примере паттерна - цепочка обязанностей:

```python
import re

from ..pattern.base import (
    BasePassValidator,
    PasswordValidationError,
)


class PassLengthValidator(BasePassValidator):
    """Валидатор длины пароля."""

    def _validate(self, password: str) -> str:
        """Валидация длины пароля."""
        if len(password) < 10:
            raise PasswordValidationError.create_length_error()

        return password


class PassOnlyAlphabeticalValidator(BasePassValidator):
    """Валидатор наличия только букв в теле пароля."""

    def _validate(self, password: str) -> str:
        "Валидация на наличие только букв в теле пароля."
        if password.isalpha():
            raise PasswordValidationError.create_only_alphabetical_error()

        return password

...

```

В самом конце модуля можно посмотреть на сборку примера в одно целое. В дальнейшем процедура сборки скорее всего поменяется. Но на текущий момент это выглядит так:

```python

...

class PassCaseValidator(BasePassValidator):
    """Валидатор регистров тела пароля."""

    def _validate(self, password: str) -> str:
        """Валидация наличия разных регистров в теле пароля."""
        upper_password = password.upper()
        lower_password = password.casefold()
        if upper_password == password or lower_password == password:
            raise PasswordValidationError.create_case_error()

        return password


pass_validator = PassLengthValidator()
pass_validator.set_next_validator(validator=PassOnlyAlphabeticalValidator())
pass_validator.set_next_validator(validator=PassOnlyNumericalValidator())
pass_validator.set_next_validator(validator=PassOnlySpecialValidator())
pass_validator.set_next_validator(validator=PassNotAlphabeticalValidator())
pass_validator.set_next_validator(validator=PassNotNumericalValidator())
pass_validator.set_next_validator(validator=PassNotSpecialValidator())
pass_validator.set_next_validator(validator=PassCaseValidator())
```
