def make_vault(secret_code):
    def combination_generator():
        yield f"Accessing vault wit: {secret_code}"
    return combination_generator

my_vault_factory = make_vault("Gold-999")
the_generator = my_vault_factory()

print(next(the_generator))
