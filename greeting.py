def greet(name):
    """Return a friendly greeting for a non-empty name."""
    name = name.strip()
    if not name:
        raise ValueError("Name must not be empty")
    return f"Hello, {name}!"
