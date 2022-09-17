class ExpenseService:

    @staticmethod
    def validate_and_create_exact_split_map(split_map, email_user_map, amount, created_by):
        total_amount = 0
        split_amount_map = dict()
        group_users = email_user_map.keys()

        for user, part_amount in split_map.items():
            if user not in group_users:
                raise Exception("{} not present in group".format(user))
            total_amount += part_amount

            if user == created_by:
                part_amount = part_amount - amount
            split_amount_map[email_user_map[user]] = part_amount
        if total_amount != amount:
            raise Exception("{} != {} mismatch amount".format(amount, total_amount))

        return split_amount_map

    @staticmethod
    def create_split_amount_body(amount, email_user_map, created_by):
        split_amount_map = dict()
        count = len(email_user_map)
        part_amount = round(amount / (count * 1.0), 2)
        for user_email, user_id in email_user_map.items():
            if user_email == created_by:
                split_amount_map[user_id] = part_amount - amount
            else:
                split_amount_map[user_id] = part_amount
        return split_amount_map

