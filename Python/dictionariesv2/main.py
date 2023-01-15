# Do not modify these lines
# from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line


# PART I


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
        "name": name,
        "date_of_birth": date_of_birth,
        "place_of_birth": place_of_birth,
        "height": height,
        "nationality": nationality,
    }
    return passport


create_passport("Bilal Abou-Allal", "2001-01-29", "Amsterdam", 1.80, "Nether")


# PART II

passport = {
    "name": "Bilal",
    "date_of_birth": "2001-01-29",
    "place_of_birth": "Amsterdam",
    "height": 1.80,
    "nationality": "Netherlands",
    "stamps": [],
}


def add_stamp(passport, country):
    country = country.lower()

    if (
        country not in passport["stamps"]
        and country not in passport["nationality"].lower()
    ):
        passport["stamps"].append(country)

    return passport


add_stamp(passport, "Morocco")
add_stamp(passport, "China")
add_stamp(passport, "Germany")


# PART III


def add_biometric_data(passport, bmd_type_name, bmd_data_value, bmd_rec_date):
    passport["biometric"] = {
        bmd_type_name: {"value": bmd_data_value, "date": bmd_rec_date}
    }
    return print(passport)


bilal = create_passport(
    "Bilal Abou-Allal", "2001-01-29", "Amsterdam", 1.80, "Netherlands"
)
bilal = add_biometric_data(bilal, "eye_color_left", "blue", "2020-05-05")
print(bilal)
