def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    print(greet("GitHub Actions"))
    print(hello_world())