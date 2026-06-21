def camel_to_snake(text):
    result = ""

    for char in text:
        if char.isupper():
            result += "_" + char.lower()
        else:
            result += char

    return result


print(camel_to_snake("firstName"))          # first_name
print(camel_to_snake("name"))               # name
print(camel_to_snake("preferredFirstName")) # preferred_first_name
print(camel_to_snake("lastName"))           # last_name