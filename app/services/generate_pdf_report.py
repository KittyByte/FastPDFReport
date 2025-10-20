import matplotlib
matplotlib.use('Agg')  # Устанавливаем неинтерактивный бэкенд для избежания ошибок с GUI
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import date
import matplotlib.dates as mdates
from collections import defaultdict
from typing import List, Dict
from app.settings import settings
from random import random


# Пример списка данных (замените на реальные)
list_of_data = [
    {
        'period_from': date(2025, 7, 1),
        'period_to': date(2025, 7, 31),
        'total_orders': 700,
        'total_revenue': 55000.0,
        'avg_order_value': 78.57,
        'top_product_name': 'Смартфон XYZ',
        'top_product_sales': 12000.0,
        'cancelled_orders': 20,
        'successful_orders': 650,
        'returned_orders': 30,
        'payment_method_stats': {
            'card': 15000.0,
            'cash': 600.0,
            'online': 39400.0
        },
        'category_breakdown': {
            'Умный дом': 30000.0,
            'Транспорт': 15000.0,
            'Аксессуары': 8000.0,
            'Электроника': 2000.0
        },
        'sales_by_day': {
            '2025-07-01': 1000.0,
            '2025-07-15': 5000.0
        },
        'comment': 'Первый месяц: Стабильный рост.'
    },
    {
        'period_from': date(2025, 8, 1),
        'period_to': date(2025, 8, 31),
        'total_orders': 800,
        'total_revenue': 70000.0,
        'avg_order_value': 87.50,
        'top_product_name': 'Смартфон ABC',
        'top_product_sales': 13000.0,
        'cancelled_orders': 30,
        'successful_orders': 750,
        'returned_orders': 20,
        'payment_method_stats': {
            'card': 16929.66,
            'cash': 687.84,
            'online': 58185.03
        },
        'category_breakdown': {
            'Умный дом': 36845.91,
            'Транспорт': 23492.99,
            'Аксессуары': 12301.43,
            'Электроника': 3162.21
        },
        'sales_by_day': {
            '2025-08-16': 418.92,
            '2025-08-20': 3000.0
        },
        'comment': 'Второй месяц: Увеличение онлайн-заказов.'
    }
    # Добавьте больше словарей по необходимости
]

def aggregate_data(list_of_data: List[Dict]) -> Dict:
    """
    Агрегирует данные из списка словарей.
    - Скалярные поля: суммирует (для дат - min/max).
    - Статистики (dict): суммирует значения по ключам.
    - sales_by_day: суммирует по датам.
    - top_product: берет из первого словаря (для простоты; можно доработать).
    - comment: объединяет все комментарии.
    """
    aggregated = defaultdict(lambda: defaultdict(float))
    total_orders = 0
    total_revenue = 0.0
    min_period_from = list_of_data[0]['period_from']
    max_period_to = list_of_data[0]['period_to']
    total_cancelled = 0
    total_successful = 0
    total_returned = 0
    comments = []

    for item in list_of_data:
        # Периоды
        min_period_from = min(min_period_from, item['period_from'])
        max_period_to = max(max_period_to, item['period_to'])

        # Скалярные
        total_orders += item['total_orders']
        total_revenue += item['total_revenue']
        total_cancelled += item['cancelled_orders']
        total_successful += item['successful_orders']
        total_returned += item['returned_orders']

        # Статистики
        for k, v in item['payment_method_stats'].items():
            aggregated['payment_method_stats'][k] += v
        for k, v in item['category_breakdown'].items():
            aggregated['category_breakdown'][k] += v
        for date_str, sales in item['sales_by_day'].items():
            aggregated['sales_by_day'][date_str] += sales

        # Комментарии
        comments.append(item['comment'])

    # Финальные значения
    avg_order_value = total_revenue / total_orders if total_orders > 0 else 0.0

    return {
        'period_from': min_period_from,
        'period_to': max_period_to,
        'total_orders': total_orders,
        'total_revenue': total_revenue,
        'avg_order_value': avg_order_value,
        'top_product_name': list_of_data[0]['top_product_name'],  # Из первого; доработайте если нужно
        'top_product_sales': list_of_data[0]['top_product_sales'],  # Аналогично
        'cancelled_orders': total_cancelled,
        'successful_orders': total_successful,
        'returned_orders': total_returned,
        'payment_method_stats': dict(aggregated['payment_method_stats']),
        'category_breakdown': dict(aggregated['category_breakdown']),
        'sales_by_day': dict(aggregated['sales_by_day']),
        'comment': ' | '.join(comments)  # Объединяем комментарии
    }

def generate_report_pdf(list_of_data: List[Dict]):
    """
    Генерирует красивый PDF-отчет на основе агрегированных данных из списка.
    """
    if not list_of_data:
        return None

    data = aggregate_data(list_of_data)
    filename = f'sales_report-period_from-{data['period_from']}-period_to-{data['period_to']}-{round(random(), 5)}.pdf'
    file_path = settings.PATH_TO_FILES / filename

    with PdfPages(file_path) as pdf:
        # Настройка стиля для красивого вида
        plt.style.use('default')

        # Страница 1: Общая статистика и ключевые метрики
        fig = plt.figure(figsize=(8.5, 11))  # Размер A4
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.axis('off')

        # Заголовок
        title = f"Агрегированный отчет по продажам\nПериод: {data['period_from'].strftime('%d.%m.%Y')} - {data['period_to'].strftime('%d.%m.%Y')}"
        ax.text(0.5, 0.95, title, ha='center', va='top', fontsize=18, fontweight='bold', transform=ax.transAxes)

        # Ключевые метрики
        y_pos = 0.85
        metrics = [
            f"Общее число заказов: {data['total_orders']}",
            f"Общая выручка: {data['total_revenue']:.2f} руб.",
            f"Средний чек: {data['avg_order_value']:.2f} руб.",
            f"Топ-товар: {data['top_product_name']} ({data['top_product_sales']:.2f} руб.)",
            f"Успешные заказы: {data['successful_orders']}",
            f"Отмененные: {data['cancelled_orders']}, Возвраты: {data['returned_orders']}"
        ]
        for metric in metrics:
            ax.text(0.1, y_pos, metric, ha='left', va='top', fontsize=12, transform=ax.transAxes)
            y_pos -= 0.05

        # Комментарий
        ax.text(0.1, y_pos - 0.1, "Примечания:", ha='left', va='top', fontsize=12, fontweight='bold', transform=ax.transAxes)
        ax.text(0.1, y_pos - 0.15, data['comment'], ha='left', va='top', fontsize=10, wrap=True, transform=ax.transAxes)

        pdf.savefig(fig, bbox_inches='tight')
        plt.close(fig)

        # Страница 2: Распределение по способам оплаты (Pie chart)
        fig = plt.figure(figsize=(8.5, 11))
        ax = fig.add_subplot(111)
        labels = list(data['payment_method_stats'].keys())
        sizes = list(data['payment_method_stats'].values())
        colors = ['#ff9999', '#66b3ff', '#99ff99'][:len(labels)]  # Адаптируем цвета
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
        ax.set_title('Распределение по способам оплаты', fontsize=14, fontweight='bold')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close(fig)

        # Страница 3: Распределение по категориям (Bar chart)
        fig = plt.figure(figsize=(8.5, 11))
        ax = fig.add_subplot(111)
        categories = list(data['category_breakdown'].keys())
        values = list(data['category_breakdown'].values())
        colors_bar = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#feca57'][:len(categories)]
        bars = ax.bar(categories, values, color=colors_bar)
        ax.set_title('Распределение продаж по категориям', fontsize=14, fontweight='bold')
        ax.set_ylabel('Сумма продаж (руб.)')
        # Добавляем значения на бары
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + max(values)*0.01,
                    f'{height:.0f}', ha='center', va='bottom', fontsize=10)
        plt.xticks(rotation=45, ha='right')
        pdf.savefig(fig, bbox_inches='tight')
        plt.close(fig)

        # Страница 4: Динамика продаж по дням (Line chart)
        fig = plt.figure(figsize=(8.5, 11))
        ax = fig.add_subplot(111)
        dates = sorted(list(data['sales_by_day'].keys()))  # Сортируем по дате
        sales = [data['sales_by_day'][d] for d in dates]
        date_objects = [date.fromisoformat(d) for d in dates]  # Преобразование строк в даты
        ax.plot(date_objects, sales, marker='o', linewidth=2, markersize=6, color='#ff6b6b')
        ax.set_title('Динамика продаж по дням', fontsize=14, fontweight='bold')
        ax.set_ylabel('Сумма продаж (руб.)')
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%d.%m.%Y'))
        interval = max(1, len(dates) // 5)
        ax.xaxis.set_major_locator(mdates.DayLocator(interval=interval))
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        pdf.savefig(fig, bbox_inches='tight')
        plt.close(fig)

    print(f"Агрегированный PDF-отчет сохранен как {filename}")
    return file_path

if __name__ == "__main__":
    generate_report_pdf(list_of_data)



