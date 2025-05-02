import itertools


class PokemonBoosterCalculator:
    def __init__(self):
        # Card specifications
        self.booster_package_weight = (23.00, 22.00)

        self.card_types = {
            'Code Card': {'weight': 1.2, 'count': 1, 'fixed': True},
            'Energy Card': {'weight': 1.74, 'count': 0, 'fixed': False},
            'Holo Energy Card': {'weight': (1.93, 1.94), 'count': 0, 'fixed': False},

            'Common Card': {'weight': 1.78, 'count': 0, 'fixed': False},
            'Holo Card': {'weight': (1.89, 1.91), 'count': 0, 'fixed': False},
            'Reverse Holo Card': {'weight': (1.88, 1.90), 'count': 0, 'fixed': False},

            'Full Art Trainer': {'weight': (1.89, 1.90), 'count': 0, 'fixed': False},
            'Pokeball Card': {'weight': (1.92, 1.95), 'count': 0, 'fixed': False},
            'Masterball Card': {'weight': (1.92, 1.94), 'count': 0, 'fixed': False},
            'ACESPEC Card': {'weight': (1.91, 1.93), 'count': 0, 'fixed': False},
            'Gold Card': {'weight': (1.88, 1.94), 'count': 0, 'fixed': False},
            'EvolutionSIR Card': {'weight': 1.90, 'count': 0, 'fixed': False}
        }

        # Booster pack configuration
        self.total_cards = 12
        self.common_cards_normal = 7

    def calculate_possible_contents(self, package_weight):
        # Check if package weight is valid
        if not (self.booster_package_weight[0] <= package_weight <= self.booster_package_weight[1]):
            print(
                f"Invalid package weight. Must be between {self.booster_package_weight[0]} and {self.booster_package_weight[1]} grams.")
            return []

        # Prepare possible card configurations
        possible_contents = []

        # Energy card configuration (always one energy or holo energy)
        energy_options = [
            {'Energy Card': 1},
            {'Holo Energy Card': 1}
        ]

        # Varying card configurations
        card_combinations = [
            {'Holo Card': 1, 'Reverse Holo Card': 2},
            {'Full Art Trainer': 1, 'Reverse Holo Card': 2},
            {'Holo Card': 1, 'Pokeball Card': 1, 'Reverse Holo Card': 1},
            {'Holo Card': 1, 'Masterball Card': 1, 'Reverse Holo Card': 1},
            {'Holo Card': 1, 'ACESPEC Card': 1, 'Reverse Holo Card': 1},
            {'Holo Card': 1, 'Gold Card': 1, 'Reverse Holo Card': 1},
            {'Holo Card': 1, 'EvolutionSIR Card': 1, 'Reverse Holo Card': 1}
        ]

        # Check each possible configuration
        for energy_config in energy_options:
            for card_config in card_combinations:
                # Copy the base card specifications
                current_contents = {
                    'Code Card': 1,
                    'Common Card': self.common_cards_normal
                }
                current_contents.update(energy_config)
                current_contents.update(card_config)

                # Calculate total weight
                total_weight = self._calculate_total_weight(current_contents)

                # Check if total weight matches package weight
                if abs(total_weight - package_weight - sum(self.booster_package_weight) / 2) < 0.05:
                    possible_contents.append(current_contents)

        return possible_contents

    def _calculate_total_weight(self, card_config):
        total_weight = 0
        for card_type, count in card_config.items():
            card_spec = self.card_types[card_type]

            # Handle weight ranges
            if isinstance(card_spec['weight'], tuple):
                # Take midpoint of weight range
                total_weight += ((card_spec['weight'][0] + card_spec['weight'][1]) / 2) * count
            else:
                total_weight += card_spec['weight'] * count

        return total_weight

    def display_results(self, possible_contents):
        if not possible_contents:
            print("No matching booster pack configuration found.")
            return

        print(f"Found {len(possible_contents)} possible booster pack configurations:")
        for i, config in enumerate(possible_contents, 1):
            print(f"\nConfiguration {i}:")
            for card_type, count in config.items():
                print(f"- {card_type}: {count}")


def main():
    calculator = PokemonBoosterCalculator()

    # Get user input for package weight
    while True:
        try:
            package_weight = float(input("What is the weight of your Booster Package (in grams)? "))
            break
        except ValueError:
            print("Please enter a valid number.")

    # Calculate and display possible contents
    possible_contents = calculator.calculate_possible_contents(package_weight)
    calculator.display_results(possible_contents)


if __name__ == "__main__":
    main()