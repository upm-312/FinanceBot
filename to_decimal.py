from decimal import Decimal

class Quotation:
    def __init__(self, units, nano):
        self.units = units
        self.nano = nano

    def get_units(self):
        return self.units

    def get_nano(self):
        return self.nano

    def to_big_decimal(self):
        if self.units == 0 and self.nano == 0:
            return Decimal(0)
        return Decimal(self.units) + Decimal(self.nano) / Decimal(1_000_000_000)

# Пример использования
def main():
    # Создаем объект Quotation
    quotation = Quotation(123, 456_000_000)  # 123.456 в формате Quotation
    print(f"Quotation: units={quotation.get_units()}, nano={quotation.get_nano()}")

    # Преобразуем Quotation в Decimal
    big_decimal_value = quotation.to_big_decimal()
    print(f"Converted to BigDecimal: {big_decimal_value}")

if __name__ == "__main__":
    main()