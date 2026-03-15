from field_math_engine.cli import calculator_choice

def main():
    print("================================")
    print("   FIELD MATH ENGINE v1.0       ")
    print("================================")

    while True:
        try:
            calculator_choice()
            again = input("\nRun another calculation? (y/n): ").lower().strip()
            if again != 'y':
                print("Shutting down...")
                break
            print("-" * 32)
        except ValueError as error_message:
            print(f"\n[!] Input Error: {error_message}")
            print("Try again.\n")
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":

   main()