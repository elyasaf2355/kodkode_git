#1
def get_names_of_active_and_over_18(users_list):
    sorted_names_list = []
    is_active = lambda usr:usr[2]
    for user in users_list:
        if user[1] >= 18 and is_active(user):
            sorted_names_list.append(user[0])
    return sorted_names_list
d = [
    ["Dan", 25, True],
    ["Noa", 16, True],
    ["Yael", 30, False],
]
#2
def validate_user(user_email):
    if not user_email:
        print("Invalid user")
        return False
    return True
def validate_quantity(quantity, stock):
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return False
    return True
def calculate_first_price(prod_price, quantity):
    return prod_price * quantity
def calculate_discount(price, quantity):
    if quantity >= 10:
        return price * 0.9
    if quantity >= 50:
        return price * 0.85
    return price
def update_stock(stock, quantity):
    return stock - quantity
def order_details(order_status, order_user, order_quantity, order_product, order_total):
    return f"Order {order_status}: {order_user} bought {order_quantity}x {order_product} for ${order_total}"


def handle_purchase(user_email, product_name, product_price, stock, quantity):
    if not validate_user(user_email):
        return
    if not validate_quantity(quantity, stock):
        return
    order_status = "confirmed"

    price = calculate_first_price(product_price, quantity)
    final_price = calculate_discount(price, quantity)
    stock = update_stock(stock, quantity)
    print(order_details(order_status, user_email, quantity, product_name, final_price))

#3
#הקוד בשאלה משובש
def validate_name(new_name):
    if not new_name or len(new_name) < 2:
        print("Error: invalid name")
        return False
    return True
def validate_grade(new_grade):
    if new_grade < 0 or new_grade > 100:
        print("Error: grade must be 0-100")
        return False
    return True
def add_grade(new_grade, grades):
    grades.append(new_grade)
    return grades
def add_student(new_name, names):
    names.append(new_name)
    return names
def calculate_stats(grades):
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= 90)
    failing_count = sum(1 for g in grades if g < 56)
    return [total, average, top_count, failing_count]
def print_report(stats):
    pass
#4
def validate_name2(new_name):
    if not new_name or len(new_name) < 2:
        raise ValueError("Invalid name")
def validate_email(email):
    if "@" not in email:
        raise ValueError("Invalid email")
def create_admin_user(name, email):
    validate_name2(name)
    validate_email(email)
    return name, email, "admin", "2024-01-01", True
def create_editor_user(name, email):
    validate_name2(name)
    validate_email(email)
    return name, email, "editor", "2024-01-01", True
def create_viewer_user(name, email):
    validate_name2(name)
    validate_email(email)
    return name, email, "viewer", "2024-01-01", True
#5
def get_status(score):
    if score >= 90:
        return "excellent"
    elif score >= 70:
        return "good"
    elif score >= 55:
        return "average"
    elif score < 55:
        return "fail"

def is_valid_age(age):
    if isinstance(age, int) and 0 < age < 120 :
        return True
    return False

def get_greeting(hour):
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif  17 <= hour < 21:
        return "Good evening"
    else:
        return "Good night"

#6
def student_validate(name, grades):
    if not name:
        print(f"Error: missing name")
        return False
    if not grades:
        print(f"Error: {name} has no grades")
        return False
    return True

def stats_student_calculate(grades):
    total = sum(grades)
    average = total / len(grades)
    status = "pass" if average >= 56 else "fail"
    highest = max(grades)
    lowest = min(grades)
    return [average, status, highest, lowest]
def report_print(result_names, result_averages, result_statuses, result_lows, result_highs):
    print("=" * 40)
    print("Student Grade Report")
    print("=" * 40)
    for i in range(len(result_names)):
        print(f"Name: {result_names[i]}")
        print(f"  Average: {result_averages[i]}")
        print(f"  Status: {result_statuses[i]}")
        print(f"  Range: {result_lows[i]} - {result_highs[i]}")
        print()
    passing_count = sum(1 for s in result_statuses if s == "pass")
    print(f"Total passing: {passing_count}/{len(result_names)}")
def process_grades(names, all_grades):
    result_names = []
    result_averages = []
    result_statuses = []
    result_highs = []
    result_lows = []
    for i in range(len(names)):
        name = names[i]
        grades = all_grades[i]
        if not student_validate(name, grades):
            continue
        stats = stats_student_calculate(grades)
        result_names.append(name)
        result_averages.append(round(stats[0], 1))
        result_statuses.append(stats[1])
        result_highs.append(stats[2])
        result_lows.append(stats[3])

        report_print(result_names, result_averages, result_statuses, result_lows, result_highs)

#7
TAX = 0.17
#process final total price to pay after tax shipping discount calculations
def ProcessCart(prices,quantities,UserType):
  total_price = 0
  for i in range(len(prices)):
    product_price = prices[i]
    product_quantity = quantities[i]
    total_price = total_price + product_price * product_quantity
# add tax
  total_price = total_price + total_price * TAX
#calculate discount base on user type
  if UserType=='premium':
    total_price = total_price * 0.9
  elif UserType=='vip':
    total_price = total_price * 0.8
#calculate shipping price
  if total_price > 500:
    shipping = 0
  elif total_price > 200:
    shipping = 25
  else:
    shipping = 50
  total_price = total_price + shipping
  return total_price
