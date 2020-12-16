from main.day16.notes import Notes


def solve(notes: Notes) -> int:
    invalid_fields = []
    for nearby_ticket in notes.nearby_tickets:
        for nearby_ticket_value in nearby_ticket:
            valid_value = False
            for field_rule in notes.field_rules:
                if nearby_ticket_value in field_rule[0] or nearby_ticket_value in field_rule[1]:
                    valid_value = True
                    break
            if not valid_value:
                invalid_fields.append(nearby_ticket_value)
    return sum(invalid_fields)
