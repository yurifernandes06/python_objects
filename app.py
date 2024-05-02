from modelos.restaurant import Restaurant


square_restaurant = Restaurant("praça", "Gourmet")
square_restaurant.receive_evaluation("Lucas", 4)
square_restaurant.receive_evaluation("Cauã", 5)
square_restaurant.receive_evaluation("Miguel", 4.5)


def main():
    Restaurant.list_restaurants()

if __name__ == "__main__":
    main()