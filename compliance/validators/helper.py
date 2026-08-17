

def province_decode_from_cnic(cnic):
    """
    Decode the province from the CNIC number.
    :param cnic: CNIC number as a string
    :return: Province name as a string
    """
    province_code = cnic[0]
    province_mapping = {
    '1': 'Khyber Pakhtunkhwa',
    '2': 'Khyber Pakhtunkhwa',  # FATA now merged into Khyber Pakhtunkhwa
    '3': 'Punjab',
    '4': 'Sindh',
    '5': 'Balochistan',
    '6': 'Islamabad Capital Territory',
    '7': 'Gilgit-Baltistan',
    '8': 'Azad Jammu and Kashmir',
    }
    return province_mapping.get(province_code, "Unknown Province")


def parse_income(value):
    value = str(value).upper()

    value = (
        value.replace("PKR", "")
        .replace("RS.", "")
        .replace("RS", "")
        .replace(",", "")
        .strip()
    )

    return int(value)