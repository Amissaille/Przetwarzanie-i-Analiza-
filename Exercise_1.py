def create_greeting(name, surname):
    greeting = f"Cześć {name} {surname}!"
    return greeting


input_name = "Tomasz"
input_surname = "Karolak"

result = create_greeting(input_name, input_surname)

print(result)
