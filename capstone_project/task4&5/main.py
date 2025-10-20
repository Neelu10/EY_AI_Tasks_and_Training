import pandas as pd
import threading
import queue
import time
import logging


logging.basicConfig(
    filename='order_processing.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def producer(orders_df, order_queue):
    for _, order in orders_df.iterrows():
        logging.info(f"Order received: {order['OrderID']}")
        print(f"Adding order {order['OrderID']} to queue")
        order_queue.put(order.to_dict())
        time.sleep(1)
    order_queue.put(None)

def consumer(products_df, order_queue):
    processed_orders = []
    start_time = time.time()

    while True:
        order = order_queue.get()
        if order is None:
            break

        product_row = products_df[products_df['ProductID'] == order['ProductID']]
        if product_row.empty:
            logging.error(f"ProductID {order['ProductID']} not found for OrderID {order['OrderID']}")
            continue

        try:
            price = product_row.iloc[0]['Price']
            total_price = float(order['Quantity']) * float(price)
            order_month = pd.to_datetime(order["OrderDate"]).month_name()

            processed_orders.append({
                "OrderID": order['OrderID'],
                "CustomerID": order['CustomerID'],
                "ProductID": order['ProductID'],
                "Quantity": order['Quantity'],
                "OrderDate": order['OrderDate'],
                "TotalPrice": total_price,
                "OrderMonth": order_month
            })

            logging.info(f"Order processed: {order['OrderID']} | TotalPrice: {total_price}")
            print(f"Processed order {order['OrderID']} | Total: {total_price}")

        except Exception as e:
            logging.error(f"Error processing OrderID {order['OrderID']}: {str(e)}")

        order_queue.task_done()

    df = pd.DataFrame(processed_orders)
    df.to_csv("processed_orders.csv", index=False)
    logging.info(f"ETL completed in {time.time() - start_time:.2f} seconds")
    logging.info(f"Total orders processed: {len(processed_orders)}")
    print("All orders processed and saved to processed_orders.csv")


if __name__ == "__main__":
    q = queue.Queue()

    orders = pd.read_csv("orders.csv")
    products = pd.read_csv("products.csv")

    producer_thread = threading.Thread(target=producer, args=(orders, q))
    consumer_thread = threading.Thread(target=consumer, args=(products, q))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    print("All orders processed successfully.")