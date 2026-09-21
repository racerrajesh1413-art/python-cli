def greet(name: str, language: str) -> str:
    name = name.strip()
    language = language.strip()
    return f"Hello {name}! {language} is a great choice."


def main():
    print(greet(input("Name: "), input("Language: ")))


if __name__ == "__main__":
    main()


