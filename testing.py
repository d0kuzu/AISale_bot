import os
import psycopg2
from openai import OpenAI

# Подключение к базе данных
def connect_db():
    conn = psycopg2.connect(
        dbname="aisale",
        user="postgres",
        password="dokuzu_desu",
        host="localhost"
    )
    return conn

# Поиск товаров в базе данных
def search_products(conn, query):
    with conn.cursor() as cur:
        sql = """
        SELECT name, description, price FROM products
        WHERE name ILIKE %s OR description ILIKE %s
        """
        cur.execute(sql, ('%' + query + '%', '%' + query + '%'))
        results = cur.fetchall()

    if not results:
        return "Ничего не найдено по вашему запросу."

    response = []
    for row in results:
        response.append(f"Название: {row[0]}\nОписание: {row[1]}\nЦена: {row[2]} KZT\n")
    return '\n'.join(response)

# Инициализация GPT API
def chat_with_gpt(messages):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    return messages, reply

# Основная логика
if __name__ == "__main__":
    # Подключение к БД
    conn = connect_db()

    # Структура таблицы товаров
    table_schema = """
    Таблица products содержит следующие поля:
    - id (int): Уникальный идентификатор товара.
    - name (text): Название товара.
    - description (text): Описание товара.
    - price (float): Цена товара в тенге.
    - category (text): Категория товара (например, 'Телефоны', 'Ноутбуки').
    - brand (text): Бренд товара.
    - stock (int): Количество на складе.
    - created_at (timestamp): Дата добавления товара.
    """

    # История сообщений
    messages = [
        {"role": "system", "content": "Ты консультант интернет-магазина. Вот структура таблицы товаров, с которой ты работаешь:\n" + table_schema}
    ]

    while True:
        # Ввод пользователя
        user_input = input("Вы: ")
        messages.append({"role": "user", "content": user_input})

        # Проверка на поиск в БД
        if any(word in user_input.lower() for word in ["телефоны", "цена", "бренд"]):
            results = search_products(conn, user_input)
            messages.append({"role": "assistant", "content": results})

        # GPT ответ с учетом контекста
        messages, reply = chat_with_gpt(messages)
        print("Бот:", reply)
