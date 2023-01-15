# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line


def greet(name, greeting_template="Hello, <name>!"):
    new_greeting = greeting_template.replace("<name>", name)
    return new_greeting


greet("Bilal")
greet("Bilal", "Whats up, <name>!")


def force(mass, body="earth"):
    body = body.lower()
    bodies = {
        "sun": 274,
        "jupiter": 24.92,
        "neptune": 11.15,
        "saturn": 10.44,
        "earth": 9.798,
        "uranus": 8.87,
        "venus": 8.87,
        "mars": 3.71,
        "mercury": 3.7,
        "moon": 1.62,
        "pluto": 0.58,
    }
    generate_force = mass * round(bodies.get(body), 1)  # type: ignore
    return generate_force


force(5, "Sun")


def pull(m1, m2, d):
    g = 6.674 * 10**-11
    generate_pull = g * ((m1 * m2) / d**2)
    return generate_pull


pull(17.2, 5.5, 2.3)
