# uetr_generator.py
import random
import string
from datetime import datetime

def generate_uetr():
    """
    Generates a UETR in the 8-4-4-4-12 format:
    - 8 characters: Timestamp (YYYYMMDD)
    - 4 characters: Random alphanumeric
    - 4 characters: Random alphanumeric
    - 4 characters: Random alphanumeric
    - 12 characters: Random alphanumeric
    """
    # Generate timestamp (8 characters: YYYYMMDD)
    timestamp = datetime.utcnow().strftime("%Y%m%d")

    # Generate random alphanumeric strings for the remaining parts
    def random_alphanumeric(length):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    part1 = random_alphanumeric(4)  # 4 characters
    part2 = random_alphanumeric(4)  # 4 characters
    part3 = random_alphanumeric(4)  # 4 characters
    part4 = random_alphanumeric(12)  # 12 characters

    # Combine all parts into the 8-4-4-4-12 format
    uetr = f"{timestamp}-{part1}-{part2}-{part3}-{part4}"

    return uetr