"""Homework_11"""

# # # Банковский вклад # # #
# Создайте класс вклад, который содержит необходимые поля и методы,
# например сумма вклада и его срок.
# Пользователь делает вклад в размере N рублей сроком на R лет под 10% годовых
# (вклад с возможностью ежемесячной капитализации - это означает,
# что проценты прибавляются к сумме вклада ежемесячно).
# Написать класс Bank, метод deposit принимает аргументы N и R,
# и возвращает сумму, которая будет на счету пользователя.
#
# https://myfin.by/wiki/term/kapitalizaciya-procentov

from my_logger import setup_logging
log = setup_logging()


class Deposit:
    """Определение класса Deposit"""
    def __init__(self, amount, term, percent=0.1):
        self.amount = float(amount)
        self.term = int(term)
        self.percent = float(percent)
        self.valid = self._validate_parameters()

        if not self.valid:
            log.error(f"Invalid parameters: amount={amount}, "
                      f"term={term}, percent={percent}")

    def _validate_parameters(self):
        valid = True
        if self.amount <= 0:
            valid = False
            log.error("Сумма вклада должна быть положительной")
        if self.term <= 0:
            valid = False
            log.error("Срок вклада должен быть больше нуля")
        if self.percent <= 0 or self.percent > 1:
            valid = False
            log.error("Процентная ставка должна быть в пределах (0, 1]")
        return valid

    def total_amount(self):
        if not self.valid:
            return None
        return round(self.amount * ((1 + self.percent / 12) ** self.term), 4)


class Bank:
    """Определение класса Bank"""
    def deposit(self, N, R):
        deposit = Deposit(N, R)
        total = deposit.total_amount()
        if total is None:
            log.error(f"Failed to create deposit with amount={N} and term={R}")
        return total


if __name__ == "__main__":
    bank = Bank()
    N = 1000  # сумма вклада
    R = 12  # срок вклада в месяцах
    total_amount = bank.deposit(N, R)
    if total_amount:
        log.info(f"Сумма на счету через {R} месяцев: "
                 f"{total_amount:.4f} рублей")
    else:
        log.error("Ошибка при создании вклада")
