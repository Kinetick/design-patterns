import generating.abstract_factory as abc_factory
import generating.builder as builder

if __name__ == '__main__':
    # Абстрактная фабрика.
    yamaha_driver = abc_factory.Driver(
        vehicle_factory=abc_factory.YamahaVehicleFactory()
    )
    honda_driver = abc_factory.Driver(
        vehicle_factory=abc_factory.HondaVehicleFactory()
    )

    # Строитель.
    diesel_car = builder.DieselCarBuilder().create_car()
    diesel_car_driver = builder.Driver(car=diesel_car)
