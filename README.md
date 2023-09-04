# BondsCalculator
Калькулятор по облигациям, позволяет смотреть доходность по купонам за каждый месяц
Команды создания таблиц БД:
1) Основная информация по облигации:
    bonds_information
    CREATE TABLE bonds_information(
        ticker VARCHAR(30) PRIMARY KEY,
        name VARCHAR(40),
        current_price decimal,
        coupon_value decimal,
        bonds_count integer);
2) Частота выплат купона:
    frequency_of_payment2
    CREATE TABLE frequency_of_payment2(
    Id SERIAL PRIMARY KEY,
    bonds_ticker VARCHAR(30),
    month_of_payment VARCHAR(11),
    FOREIGN KEY(bonds_ticker) REFERENCES bonds_information (ticker)
);
