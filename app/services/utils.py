""" Указывать тут все импорты для корректной работы create_all И drop_all """
import random
from datetime import date, timedelta

from sqlalchemy import Integer, and_, cast, func, select, update

from app.database import BaseOrm, engine, session_factory
from app.pdf_reports.models import *
from app.users.models import *
from app.users.dao import UserDAO
from app.celery import celery_app
from celery.result import AsyncResult as AsyncResultTyping


def create_user():
    UserDAO.create(
        username='Spongebob',
        password='acuna_matata',
        fullname='Spongebob Squarepants',
        email='qwerty@gmail.com',
        disabled=False,
        telegram_id=670076879
    )


# Предполагаем, что в таблице users уже есть хотя бы один пользователь с id=1.
# При необходимости замените user_id на существующий.
def create_sales_reports(num_records: int = 100):
    create_user()

    product_names = [
        "Умная колонка", "Наушники Bluetooth", "Умная лампа",
        "Фитнес-браслет", "Электросамокат", "Робот-пылесос"
    ]
    categories = ["Электроника", "Аксессуары", "Умный дом", "Транспорт"]
    payment_methods = ["cash", "card", "online"]

    with session_factory() as session:
        for _ in range(num_records):
            # Период отчёта
            start = date.today() - timedelta(days=random.randint(1, 365))
            end = start + timedelta(days=random.randint(1, 30))

            # Заказы и выручка
            total_orders = random.randint(1, 50)
            # Сгенерируем случайные чеки для каждого заказа
            checks = [round(random.uniform(100.0, 10000.0), 2) for _ in range(total_orders)]
            total_revenue = round(sum(checks), 2)
            avg_order_value = round(total_revenue / total_orders, 2)

            # Статусы заказов
            cancelled_orders = random.randint(0, total_orders // 5)
            remaining = total_orders - cancelled_orders
            successful_orders = random.randint(0, remaining)
            returned_orders = random.randint(0, cancelled_orders)

            # Топ-продукт
            top_product_name = random.choice(product_names)
            top_product_sales = round(random.uniform(100.0, total_revenue), 2)

            # Распределение по способам оплаты
            payment_method_stats = {}
            for method in payment_methods:
                payment_method_stats[method] = round(random.uniform(0, total_revenue / 2), 2)
            # Нормируем, чтобы сумма совпадала с total_revenue
            total_pm = sum(payment_method_stats.values())
            for method in payment_method_stats:
                payment_method_stats[method] = round(payment_method_stats[method] / total_pm * total_revenue, 2)

            # Распределение по категориям
            category_breakdown = {}
            for cat in categories:
                category_breakdown[cat] = round(random.uniform(0, total_revenue / 2), 2)
            total_cat = sum(category_breakdown.values())
            for cat in category_breakdown:
                category_breakdown[cat] = round(category_breakdown[cat] / total_cat * total_revenue, 2)

            # Динамика продаж по дням
            days = (end - start).days + 1
            sales_by_day = {}
            for i in range(days):
                day = start + timedelta(days=i)
                sales_by_day[day.isoformat()] = round(random.uniform(0, total_revenue / days), 2)

            # Комментарий
            comment = random.choice([
                "Автоматически сгенерированный отчёт",
                "Содержит все данные по продажам",
                "Проверить не требуется"
            ])

            report = SalesReportOrm(
                user_id=1,
                period_from=start,
                period_to=end,
                total_orders=total_orders,
                total_revenue=total_revenue,
                avg_order_value=avg_order_value,
                top_product_name=top_product_name,
                top_product_sales=top_product_sales,
                cancelled_orders=cancelled_orders,
                successful_orders=successful_orders,
                returned_orders=returned_orders,
                payment_method_stats=payment_method_stats,
                category_breakdown=category_breakdown,
                sales_by_day=sales_by_day,
                comment=comment
            )
            session.add(report)
        session.commit()


def create_tables():
    BaseOrm.metadata.create_all(engine)


def drop_and_create_database():
    print(BaseOrm.metadata.tables.keys())
    print('='*100)
    BaseOrm.metadata.drop_all(engine)
    create_tables()


def select_sales_report():
    with session_factory() as session:
        query = select(SalesReportOrm)
        result = session.execute(query).scalars().first()
        print(result)


def update_sales_report():
    with session_factory() as session:
        query = update(UserOrm).values(
                name=random.choice(['Бобер', 'Цыпа', 'Голубио']),
                fullname=random.choice(['Бобер', 'Цыпа', 'Голубио'])
            ).filter_by(id=2)
        session.execute(query)
        session.commit()


def select_sales_reports_with_avg():
    with session_factory() as session:
        """
        SELECT successful_orders, CAST(avg(cancelled_orders) AS INTEGER) AS avg_cancelled_orders
        FROM sales_report
        WHERE top_product_name LIKE '%Фитнес-браслет%' AND successful_orders > 10
        GROUP BY successful_orders
        """
        query = (
            select(
                SalesReportOrm.successful_orders,
                cast(func.avg(SalesReportOrm.cancelled_orders), Integer).label('avg_cancelled_orders')
            )
            .filter(and_(
                SalesReportOrm.top_product_name.contains('Фитнес-браслет'),
                SalesReportOrm.successful_orders > 10
            ))
            .group_by(SalesReportOrm.successful_orders)
        )

        r = session.execute(query).all()
        print(query.compile(compile_kwargs={'literal_binds': True}))  # вывод SQL с подставленными параметрами
        print(r)  # [(42, 6), (31, 8), (18, 3)]
        print(r[0].avg_cancelled_orders)  # 6  # берем первую запись и обращаемся к label


def t_status(task_id) -> AsyncResultTyping:
    res = celery_app.AsyncResult(task_id)
    return res



def some_sql():
    # create_user()
    # update_sales_report()
    # select_sales_report()
    create_sales_reports()
    # select_sales_reports_with_avg()
    

    return 'OK'

