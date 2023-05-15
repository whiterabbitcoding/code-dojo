from collections import namedtuple

# def namedtuplemerge(*args):
#     cls = namedtuple(
#         "_".join(arg.__class__.__name__ for arg in args),
#         reduce(add, (arg._fields for arg in args)),
#     )
#     return cls(*chain(*args))


def merge(*records) -> namedtuple:
    """
    :param records: (varargs list of namedtuple) The patient details.
    :returns: (namedtuple) named Patient, containing details from all records, in entry order.
    """
    fields = []
    for x in records:
        print(dir(x))
        print(x._fields)
        fields += x._fields

    patient = namedtuple("Patient", fields)
    print(patient.eye_color)
    return patient


PersonalDetails = namedtuple("PersonalDetails", ["date_of_birth"])
personal_details = PersonalDetails(date_of_birth="06-04-1972")

Complexion = namedtuple("Complexion", ["eye_color", "hair_color"])
complexion = Complexion(eye_color="Blue", hair_color="Black")
print(complexion.eye_color)

print(merge(personal_details, complexion))
