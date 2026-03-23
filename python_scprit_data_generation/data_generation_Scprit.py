# import pandas as pd
# import numpy as np
# import random
# from datetime import datetime, timedelta
# import os

# np.random.seed(42)
# random.seed(42)

# SAVE_PATH = r"C:\Users\Tnluser\Desktop\datasets\project1"
# os.makedirs(SAVE_PATH, exist_ok=True)

# # ----------------------------------------
# # CONFIG
# # ----------------------------------------
# NUM_USERS = 600
# START_DATE = datetime(2025, 1, 1)

# # ----------------------------------------
# # PRODUCTS (ONLY 2 MODELS - SAME BRAND)
# # ----------------------------------------
# products = pd.DataFrame([
#     ["P301","Dell Latitude 5440","Laptop","Mid","Electronics",85000,60000],
#     ["P302","Dell Latitude 7440","Laptop","Premium","Electronics",125000,90000],
# ], columns=[
#     "product_id","product_name","product_type",
#     "segment","category","unit_price","cost_price"
# ])

# # ----------------------------------------
# # USERS
# # ----------------------------------------
# cities = ["Mumbai","Bangalore","Delhi","Hyderabad","Chennai"]
# devices = ["Mobile","Desktop","Tablet"]

# users = []
# for i in range(NUM_USERS):
#     reg_date = START_DATE + timedelta(days=random.randint(0, 120))

#     users.append([
#         f"U{i+1:04}",
#         reg_date.date(),
#         random.choice(cities),
#         random.choices(devices, weights=[0.6,0.35,0.05])[0]
#     ])

# users = pd.DataFrame(users, columns=[
#     "user_id","registration_date","city","device_type"
# ])

# # ----------------------------------------
# # SESSIONS + EVENTS
# # ----------------------------------------
# events = []
# sessions = []
# session_counter = 1

# for _, user in users.iterrows():
#     num_sessions = random.randint(2, 20)

#     for _ in range(num_sessions):
#         session_id = f"S{session_counter:05}"
#         session_counter += 1

#         session_start = datetime.combine(user["registration_date"], datetime.min.time()) + timedelta(days=random.randint(0, 180))

#         sessions.append([
#             session_id,
#             user["user_id"],
#             session_start,
#             random.randint(2, 25)
#         ])

#         t = session_start

#         # Home page
#         events.append([user["user_id"], session_id, "page_view", t, "home", None])

#         # User browses 1 or 2 products
#         viewed_products = random.sample(list(products["product_id"]), k=random.randint(1,2))

#         for product in viewed_products:
#             t += timedelta(minutes=random.randint(1,5))
#             events.append([user["user_id"], session_id, "product_view", t, "product", product])

#             # Add to cart (conditional)
#             if random.random() < 0.5:
#                 t += timedelta(minutes=random.randint(1,3))
#                 events.append([user["user_id"], session_id, "add_to_cart", t, "cart", product])

#                 # Checkout
#                 if random.random() < 0.6:
#                     t += timedelta(minutes=random.randint(1,3))
#                     events.append([user["user_id"], session_id, "checkout", t, "checkout", product])

#                     # Purchase
#                     if random.random() < 0.7:
#                         t += timedelta(minutes=random.randint(1,5))
#                         events.append([user["user_id"], session_id, "purchase", t, "confirmation", product])

# events = pd.DataFrame(events, columns=[
#     "user_id","session_id","event_name","event_timestamp","page_type","product_id"
# ])

# sessions = pd.DataFrame(sessions, columns=[
#     "session_id","user_id","session_start","session_duration_min"
# ])

# # ----------------------------------------
# # USER SEGMENT (BASED ON SESSIONS)
# # ----------------------------------------
# session_counts = sessions.groupby("user_id").size().reset_index(name="total_sessions")

# def segment(x):
#     if x < 3:
#         return "New"
#     elif x <= 8:
#         return "Engaged"
#     else:
#         return "Power User"

# session_counts["user_segment"] = session_counts["total_sessions"].apply(segment)

# users = users.merge(session_counts, on="user_id")

# # ----------------------------------------
# # ORDERS
# # ----------------------------------------
# orders = []
# purchase_events = events[events["event_name"] == "purchase"]

# for i, row in purchase_events.iterrows():
#     product = products[products["product_id"] == row["product_id"]].iloc[0]

#     quantity = random.randint(1,2)

#     # Campaign-based discount logic
#     discount_pct = 10 if product["segment"] == "Premium" else 15

#     total_rev = quantity * product["unit_price"]
#     discount = total_rev * discount_pct/100
#     final_rev = total_rev - discount
#     total_cost = quantity * product["cost_price"]
#     profit = final_rev - total_cost

#     status = random.choices(
#         ["Completed","Cancelled","Failed"],
#         weights=[0.85,0.1,0.05]
#     )[0]

#     orders.append([
#         f"O{i:05}",
#         row["user_id"],
#         row["session_id"],
#         row["event_timestamp"].date(),
#         product["product_id"],
#         product["product_name"],
#         quantity,
#         total_rev,
#         final_rev,
#         profit,
#         discount_pct,
#         status
#     ])

# orders = pd.DataFrame(orders, columns=[
#     "order_id","user_id","session_id","order_date",
#     "product_id","product_name","quantity",
#     "total_revenue","final_revenue","profit",
#     "discount_pct","order_status"
# ])

# # ----------------------------------------
# # SAVE
# # ----------------------------------------
# users.to_csv(os.path.join(SAVE_PATH, "users.csv"), index=False)
# products.to_csv(os.path.join(SAVE_PATH, "products.csv"), index=False)
# sessions.to_csv(os.path.join(SAVE_PATH, "sessions.csv"), index=False)
# events.to_csv(os.path.join(SAVE_PATH, "events.csv"), index=False)
# orders.to_csv(os.path.join(SAVE_PATH, "orders.csv"), index=False)

# print("✅ Production-grade dataset created!")



import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

np.random.seed(42)
random.seed(42)

SAVE_PATH = r"C:\Users\Tnluser\Desktop\datasets\project1\folder1"
os.makedirs(SAVE_PATH, exist_ok=True)

# ----------------------------------------
# CONFIG
# ----------------------------------------
NUM_USERS = 600
START_DATE = datetime(2025, 1, 1)

# ----------------------------------------
# PRODUCTS (UNCHANGED)
# ----------------------------------------
products = pd.DataFrame([
    ["P301","Dell Latitude 5440","Laptop","Mid","Electronics",85000,60000],
    ["P302","Dell Latitude 7440","Laptop","Premium","Electronics",125000,90000],
], columns=[
    "product_id","product_name","product_type",
    "segment","category","unit_price","cost_price"
])

# ----------------------------------------
# USERS (UNCHANGED)
# ----------------------------------------
cities = ["Mumbai","Bangalore","Delhi","Hyderabad","Chennai"]
devices = ["Mobile","Desktop","Tablet"]

users = []
for i in range(NUM_USERS):
    reg_date = START_DATE + timedelta(days=random.randint(0, 120))

    users.append([
        f"U{i+1:04}",
        reg_date.date(),
        random.choice(cities),
        random.choices(devices, weights=[0.6,0.35,0.05])[0]
    ])

users = pd.DataFrame(users, columns=[
    "user_id","registration_date","city","device_type"
])

# ----------------------------------------
# SESSIONS + EVENTS (FIXED LOGIC)
# ----------------------------------------
events = []
sessions = []
session_counter = 1

for month in range(12):

    base_date = START_DATE + timedelta(days=30 * month)

    # 🔥 CONTROLLED TREND
    if month < 6:
        sessions_5440 = 220
        sessions_7440 = 140
    else:
        sessions_5440 = 140
        sessions_7440 = 220

    for product, session_count in [("P301", sessions_5440), ("P302", sessions_7440)]:

        for _ in range(session_count):

            user = users.sample(1).iloc[0]

            session_id = f"S{session_counter:05}"
            session_counter += 1

            session_start = base_date + timedelta(
                days=random.randint(0, 25),
                minutes=random.randint(0, 1440)
            )

            # SAME STRUCTURE
            sessions.append([
                session_id,
                user["user_id"],
                session_start,
                random.randint(2, 25)
            ])

            t = session_start

            # page_view (UNCHANGED)
            events.append([user["user_id"], session_id, "page_view", t, "home", None])

            # 🔥 ONLY ONE PRODUCT PER SESSION
            t += timedelta(minutes=random.randint(1,3))
            events.append([user["user_id"], session_id, "product_view", t, "product", product])

            # 🔥 PRODUCT-SPECIFIC FUNNEL
            if product == "P301":
                prob_cart = 0.45
                prob_checkout = 0.35
                prob_purchase = 0.25
            else:
                prob_cart = 0.65
                prob_checkout = 0.55
                prob_purchase = 0.45

            if random.random() < prob_cart:
                t += timedelta(minutes=random.randint(1,2))
                events.append([user["user_id"], session_id, "add_to_cart", t, "cart", product])

                if random.random() < prob_checkout:
                    t += timedelta(minutes=random.randint(1,2))
                    events.append([user["user_id"], session_id, "checkout", t, "checkout", product])

                    if random.random() < prob_purchase:
                        t += timedelta(minutes=random.randint(1,3))
                        events.append([user["user_id"], session_id, "purchase", t, "confirmation", product])

events = pd.DataFrame(events, columns=[
    "user_id","session_id","event_name","event_timestamp","page_type","product_id"
])

sessions = pd.DataFrame(sessions, columns=[
    "session_id","user_id","session_start","session_duration_min"
])

# ----------------------------------------
# USER SEGMENT (UNCHANGED)
# ----------------------------------------
session_counts = sessions.groupby("user_id").size().reset_index(name="total_sessions")

def segment(x):
    if x < 3:
        return "New"
    elif x <= 8:
        return "Engaged"
    else:
        return "Power User"

session_counts["user_segment"] = session_counts["total_sessions"].apply(segment)
users = users.merge(session_counts, on="user_id")

# ----------------------------------------
# ORDERS (UNCHANGED)
# ----------------------------------------
orders = []
purchase_events = events[events["event_name"] == "purchase"]

for i, row in purchase_events.iterrows():
    product = products[products["product_id"] == row["product_id"]].iloc[0]

    quantity = random.randint(1,2)

    discount_pct = 10 if product["segment"] == "Premium" else 15

    total_rev = quantity * product["unit_price"]
    discount = total_rev * discount_pct/100
    final_rev = total_rev - discount
    total_cost = quantity * product["cost_price"]
    profit = final_rev - total_cost

    status = random.choices(
        ["Completed","Cancelled","Failed"],
        weights=[0.85,0.1,0.05]
    )[0]

    orders.append([
        f"O{i:05}",
        row["user_id"],
        row["session_id"],
        row["event_timestamp"].date(),
        product["product_id"],
        product["product_name"],
        quantity,
        total_rev,
        final_rev,
        profit,
        discount_pct,
        status
    ])

orders = pd.DataFrame(orders, columns=[
    "order_id","user_id","session_id","order_date",
    "product_id","product_name","quantity",
    "total_revenue","final_revenue","profit",
    "discount_pct","order_status"
])

# ----------------------------------------
# SAVE (UNCHANGED)
# ----------------------------------------
users.to_csv(os.path.join(SAVE_PATH, "users.csv"), index=False)
products.to_csv(os.path.join(SAVE_PATH, "products.csv"), index=False)
sessions.to_csv(os.path.join(SAVE_PATH, "sessions.csv"), index=False)
events.to_csv(os.path.join(SAVE_PATH, "events.csv"), index=False)
orders.to_csv(os.path.join(SAVE_PATH, "orders.csv"), index=False)

print("✅ FINAL DATASET READY — NO MORE FIXES NEEDED")