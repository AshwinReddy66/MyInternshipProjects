continue_converting = False


def length_converter():
  print("Welcome to length convertor")
  print("1. Meters to Feet")
  print("2. Feet to Meters")
  choice = int(input("Enter your choice 1 or 2: "))
  value = float(input("Enter the value to convert: "))

  if choice == 1:
    converted_value = value * 3.28084
    print(f"{value} meters is equal to {converted_value} feet")
  elif choice == 2:
    converted_value = value / 3.28084
    print(f"{value} feet is equal to {converted_value} meters")
  else:
    print("Invalid choice")
  if input(
      'if you want to try the coverter with other values means type"y" otherwise "n": '
  ) == 'y':
    continue_converting = True


while not continue_converting:
  length_converter()
