def create_user(first_name: str, last_name: str, age: int = 42, **kwargs):
    return {
        "name": first_name,
        "surname": last_name,
        "age": age,
        "extra": kwargs
    }


print(create_user("John", "Doe"))

print(create_user("Bill", "Gates", age=65))

print(create_user("Marie", "Curie", age=66, occupation="physicist", won_nobel=True))
