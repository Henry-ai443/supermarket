class Supermarket:
    def __init__(self):
        self.items = {
            'Apple': 0.5,
            'Banana': 0.3,
            'Orange': 0.7,
            'Milk': 1.5,
            'Bread': 1.0,
            'Eggs': 2.0,
            'Rice': 3.0
        }

        self.cart = []

        def add_item(self, item, quantity):
            if item in self.items:
                self.cart.append({'item': item, 'Quantity': quantity, 'price': self.items[item]})
                print(f"Added{quantity}{item}(s) to your cart")
            else:
                print(f"Sorry, {item} is not available.")

        def remove_item(self, item):
            for entry in self.cart:
                if entry['item'] == item:
                    self.cart = [entry for entry in self.cart if ['item'] != item]
                    print(f"Removed {item} from your cart.")
                    return
                print(f"{item} is not in your cart.")

        def calculate_total(self):
            total = 0
            for entry in self.cart:
                total += entry['quantity'] * entry['price']
                return total
        
        def apply_discount(self, discount_percentage):
            total = self.calculate_total
            discount = (discount_percentage / 100) * total
            return total - discount
        
        def generate_receipt(self, discount_percentage = 10):
            if len(self.cart) == 0:
                print("Your cart is empty")
                return
            
            print("\nReceipt")
            print("------------------------")
            for entry in self.cart:
                print(f"{entry['quantity']} x {entry['item']} @ Ksh{entry['price']} each")
                total = self.calculate_total()
                discounted_total = self.apply_discount(discount_percentage)
                print("-----------------")
                print(f"Total:Ksh{total:.2f}")
                print(f"Total with {discount_percentage}% discount: Ksh{discounted_total:.2f}")
                print("Thankyou for shopping with us!!")

supermarket = Supermarket()
print(supermarket)
