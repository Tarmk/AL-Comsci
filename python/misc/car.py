from __future__ import annotations


class Car:
    def __init__(self, registration: str, make: str) -> None:
        self.__registration: str = registration
        self.__make: str = make
        self.__mileage: int = 0
        self.__date_of_inspection: str | None = None

    def getRegistration(self) -> str:
        return self.__registration

    def getMake(self) -> str:
        return self.__make

    def getMileage(self) -> int:
        return self.__mileage

    def getDateOfInspection(self) -> str | None:
        return self.__date_of_inspection

    def setInspectionData(self, miles_driven: int, date_of_inspection: str) -> None:
        if miles_driven < 0:
            raise ValueError("miles_driven must be non-negative")
        self.__mileage += miles_driven
        self.__date_of_inspection = date_of_inspection


def main() -> None:
    car = Car("AB12 CDE", "Toyota")
    print(car.getRegistration())
    print(car.getMake())
    print(car.getMileage())
    print(car.getDateOfInspection())

    car.setInspectionData(350, "2025-08-27")
    print(car.getMileage())
    print(car.getDateOfInspection())


if __name__ == "__main__":
    main()



