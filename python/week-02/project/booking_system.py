__contributor__ = "Muhammed Mahir Varlioglu"
__email__ = "mmahirv@hotmail.com"

movie_list_onshow = [
    {
        'title': 'The Matrix',
        'genre': 'Action',
        'show_times': [
            {
                'start_time': '09:00',
                'ticket_price': 15.00,
                'seats_number': 100
            },
            {
                'start_time': '12:00',
                'ticket_price': 15.00,
                'seats_number': 100
            },
            {
                'start_time': '18:00',
                'ticket_price': 18.00,
                'seats_number': 80
            }
        ]
    },

    {
        'title': 'Inception',
        'genre': 'Sci-Fi',
        'show_times': [
            {
                'start_time': '10:00',
                'ticket_price': 14.00,
                'seats_number': 120
            },
            {
                'start_time': '15:00',
                'ticket_price': 16.00,
                'seats_number': 90
            },
            {
                'start_time': '20:00',
                'ticket_price': 18.00,
                'seats_number': 50
            }
        ]
    },

    {
        'title': 'The Dark Knight',
        'genre': 'Action',
        'show_times': [
            {
                'start_time': '11:00',
                'ticket_price': 13.00,
                'seats_number': 100
            },
            {
                'start_time': '17:00',
                'ticket_price': 15.00,
                'seats_number': 75
            },
            {
                'start_time': '21:00',
                'ticket_price': 20.00,
                'seats_number': 40
            }
        ]
    },

    {
        'title': 'Pulp Fiction',
        'genre': 'Crime',
        'show_times': [
            {
                'start_time': '13:00',
                'ticket_price': 14.00,
                'seats_number': 110
            },
            {
                'start_time': '16:30',
                'ticket_price': 15.00,
                'seats_number': 85
            },
            {
                'start_time': '21:30',
                'ticket_price': 18.00,
                'seats_number': 45
            }
        ]
    },

    {
        'title': 'Gladiator',
        'genre': 'Drama',
        'show_times': [
            {
                'start_time': '10:30',
                'ticket_price': 13.00,
                'seats_number': 100
            },
            {
                'start_time': '15:30',
                'ticket_price': 15.00,
                'seats_number': 80
            },
            {
                'start_time': '20:30',
                'ticket_price': 19.00,
                'seats_number': 50
            }
        ]
    }
]

snack_bar_list = {
    'Popcorn Small': 5.00,
    'Popcorn Medium': 7.00,
    'Popcorn Large': 9.00,
    'Nachos': 7.00,
    'Soda': 3.00,
    'Candy': 2.00,
    'Chocolate': 4.00,
    'Ice Cream': 6.00,
    'Cola': 3.00,
    'water': 1.00,
    'tea': 2.00,
}

order_information = {
    'customer_name': '',
    'movie_names': '',
    'movie_show_time': '',
    'ticket_quantity': 0,
    'snacks': [],
    'cost_of_snacks': 0.00,
    'cost_of_tickets': 0.00,
    'subtotal': 0.00,
    'cost_of_fees': 0.00,
    'total_amount': 0.00,
}

past_customer_orders = []

#Someone searches for a genre we don't currently have any movies in — this should just show "no results," not break the program
#Instead, the program should show a short, clear message explaining what went wrong.
def filter_movies_by_genre(genre):
    filtered_movies = []

    for movie in movie_list_onshow:
        if movie['genre'].lower() == genre.strip().lower():
            filtered_movies.append(movie)

    if not filtered_movies:
        print(f'No movies found for genre "{genre}".')

    return filtered_movies

#Instead, the program should show a short, clear message explaining what went wrong.
def filter_movies_by_ticket_price(ticket_price):
    filtered_movies = []
    for movie in movie_list_onshow:
            for show_time in movie['show_times']:
                if show_time['ticket_price'] <= ticket_price:
                    filtered_movies.append({
                        "title":movie['title'],
                        "genre":movie['genre'],
                        "start_time":show_time['start_time'],
                        "ticket_price":show_time['ticket_price']
                    })
                    break
    if not filtered_movies:
        print(f'No movies found with ticket price of €{ticket_price} or less.')

    return filtered_movies

def calculate_total_cost_of_tickets(ticket_quantity, ticket_price):
    total_cost = ticket_quantity * ticket_price

    return total_cost

def calculate_total_cost_of_snacks(snack_list):
    total_snack_cost = 0.0
    for snack in snack_list:
        snack_name = snack["snack_name"]
        snack_quantity = snack["snack_quantity"]
        snack_unit_price = snack_bar_list[snack_name]
        snack_total = snack_quantity * snack_unit_price
        total_snack_cost += snack_total
    
    return total_snack_cost

def calculate_total_cost_of_fees(cost_of_tickets, cost_of_snacks, fee_rates = [0.05, 0.02, 0.01]):
    subtotal = cost_of_tickets + cost_of_snacks
    def apply_fees_recursive(current_total, remaining_fees):
        if not remaining_fees:
            return current_total
        current_fee_rate = remaining_fees[0]
        new_total = current_total * (1+ current_fee_rate)
        return apply_fees_recursive(new_total, remaining_fees[1:])
    
    final_total = apply_fees_recursive(subtotal, fee_rates)
    total_fees = final_total - subtotal
    return total_fees

def calculate_total_cost_of_booking(cost_of_tickets, cost_of_snacks, cost_of_fees):
    subtotal = cost_of_tickets + cost_of_snacks
    total = subtotal + cost_of_fees
    return total

#Someone tries to book more seats than are actually available.
#Instead, the program should show a short, clear message explaining what went wrong.
def update_movie_list(movie_name, show_time, ticket_quantity):

    return 0

def booking_ticket():
    customer_name = input('Enter the customer name: ')
    order_information['customer_name'] = customer_name

    movie_name = input('Enter the movie name to book a ticket: ')

    #Someone enters a customer or movie that doesn't exist in the system.
    if(movie_name not in [movie['title'] for movie in movie_list_onshow]):
        print(f'Movie "{movie_name}" is not available in the movie list.')
        return 0

    show_time = input('Enter the show time (HH:MM) to book a ticket: ')

    movie = next(m for m in movie_list_onshow if m['title'] == movie_name)

    #someone enters a show time that doesn't exist for the selected movie.
    if show_time not in [st['start_time'] for st in movie['show_times']]:
        print(f'Show time "{show_time}" is not available for movie "{movie_name}".')
        return 0

    while True:
        quantity_input = input('Enter the number of tickets to book: ')
        try:
            ticket_quantity = int(quantity_input)
            break
        except ValueError:
            print(f'"{quantity_input}" is not a valid number. Please enter a whole number.')

    showtime_info = next(st for st in movie['show_times'] if st['start_time'] == show_time)

    if ticket_quantity > showtime_info['seats_number']:
        print(f'Cannot book {ticket_quantity} tickets. Only {showtime_info["seats_number"]} seats are available.')
        return 0

    update_movie_list(movie_name, show_time, ticket_quantity)

    return 0

#Someone tries to check out an order that has no movie selected yet.
#Instead, the program should show a short, clear message explaining what went wrong.
def check_out_order(order_information):
    if not order_information['movie_names']:
        print("No movie has been selected for this order yet. Please book a ticket first.")
        return None

    if order_information['ticket_quantity'] <= 0:
        print("There are no tickets in this order. Please book a ticket first.")
        return None

    subtotal = order_information['cost_of_tickets'] + order_information['cost_of_snacks']
    order_information['subtotal'] = subtotal

    fees = calculate_total_cost_of_fees(
        order_information['cost_of_tickets'],
        order_information['cost_of_snacks']
    )
    order_information['cost_of_fees'] = fees

    total = calculate_total_cost_of_booking(
        order_information['cost_of_tickets'],
        order_information['cost_of_snacks'],
        fees
    )
    order_information['total_amount'] = total

    ticket_unit_price = order_information['cost_of_tickets'] / order_information['ticket_quantity']

    print("\n========== RECEIPT ==========")
    print(f"Customer: {order_information['customer_name']}")
    print(f"Movie:    {order_information['movie_names']} ({order_information['movie_show_time']})")
    print("-" * 30)

    ticket_line = f"Tickets ({order_information['ticket_quantity']} x ${ticket_unit_price:.2f})"
    print(f"{ticket_line:<20}${order_information['cost_of_tickets']:>7.2f}")

    for snack in order_information['snacks']:
        line = f"{snack['snack_name']} x{snack['snack_quantity']}"
        price = snack_bar_list[snack['snack_name']] * snack['snack_quantity']
        print(f"{line:<20}${price:>7.2f}")

    print("-" * 30)
    print(f"{'Subtotal:':<20}${subtotal:>7.2f}")
    print(f"{'Total with fees:':<24}${total:>7.2f}")
    print("=" * 30)

    update_movie_list(
        order_information['movie_names'],
        order_information['movie_show_time'],
        order_information['ticket_quantity']
    )

    past_customer_orders.append(order_information.copy())

    print("\nPayment complete, enjoy the show!")
    return order_information

def print_snack_bar_list(snack_bar_list):
    print("\n===== SNACK BAR MENU =====")
    for snack_name, price in snack_bar_list.items():
        print(f"{snack_name:<20}${price:>6.2f}")
    print("===========================")


def take_snack_order():
    order_snacks = []
    while True:
        print_snack_bar_list(snack_bar_list)

        snack_name = input('Enter the snack name to order (or type "done" to finish): ')

        if snack_name.lower() == 'done':
            break

        matched_key = None
        for key in snack_bar_list:
            if key.lower() == snack_name.lower():
                matched_key = key
                break

        if matched_key is None:
            print(f'Snack "{snack_name}" is not available in the snack bar list.')
            continue

        while True:
            quantity_input = input('Enter the quantity of the snack to order: ')
            try:
                snack_quantity = int(quantity_input)
                break
            except ValueError:
                print(f'"{quantity_input}" is not a valid number. Please enter a whole number.')

        order_snacks.append({
            'snack_name': matched_key,
            'snack_quantity': snack_quantity
            })

    return order_snacks


print('Welcome to the Movie Booking System!')

while True:
    user_selection = input("""
        Please select an option:
            1. Filter movies by genre
            2. Filter movies by ticket price
            3. Book a ticket
            4. Order snacks
            5. Check out order
            6. Exit
    """)

    if(user_selection == '1'):
        genre = input('Enter a genre to filter movies: ')
        filtered_movies = filter_movies_by_genre(genre)

        print(f'Filtered movies by genre "{genre}": {filtered_movies}')
    elif(user_selection == '2'):
        ticket_price = float(input('Enter a ticket price to filter movies: '))
        filtered_movies = filter_movies_by_ticket_price(ticket_price)

        print(f'Filtered movies by ticket price "{ticket_price}": {filtered_movies}')
    elif(user_selection == '3'):
        booking_ticket()
    elif(user_selection == '4'):
        order_snacks_list = take_snack_order()

        if len(order_snacks_list) == 0:
            print('No snacks were ordered.')
        else:
            calculate_total_cost_of_snacks(order_snacks_list)
    elif(user_selection == '5'):
        check_out_order(order_information)
    elif(user_selection == '6'):
        print('Exiting the Movie Booking System. Goodbye!')
        break