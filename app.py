def process_input(user_input):
    if not user_input or not user_input.strip():
        return "Invalid input: input cannot be empty."

    return f"Input accepted: {user_input}"


user_input = input("Enter your input: ")
print(process_input(user_input))
