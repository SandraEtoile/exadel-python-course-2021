def create_user(*args, age=42, **kwargs):
    return {
        "name": args[0],
        "surname": args[1],
        "age": age,
        "extra": kwargs
    }


print(create_user("John", "Doe"))

print(create_user("Bill", "Gates", age=65))

print(create_user("Marie", "Curie", age=66, occupation="physicist", won_nobel=True))
