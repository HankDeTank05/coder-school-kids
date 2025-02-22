def make_sandwich(_bread: str, _substance_list: list[str]):
    print("here's your sandwich:\n")
    print(_bread)
    for item in _substance_list:
        print(item)
    print(_bread)

bread = "bagel"
substance_list = ["crunchy peanut butter", "strawberry jelly"]
make_sandwich(bread, substance_list)
