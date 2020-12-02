from policy import Policy


def is_valid_password_occurrence(policy_password: (Policy, str)) -> bool:
    policy: Policy = policy_password[0]
    password = policy_password[1]
    occurrences = password.count(policy.letter)
    return occurrences in range(policy.lower_bound, policy.upper_bound + 1)


def validate_occurrences(password_db: (Policy, str)) -> int:
    return sum(is_valid_password_occurrence(x) for x in password_db)


def is_valid_password_position(policy_password: (Policy, str)) -> bool:
    policy: Policy = policy_password[0]
    password = policy_password[1]
    conditions = [password[policy.lower_bound - 1] == policy.letter, password[policy.upper_bound - 1] == policy.letter]
    return any(conditions) and not all(conditions)


def validate_positions(password_db: (Policy, str)) -> int:
    return sum(is_valid_password_position(x) for x in password_db)
