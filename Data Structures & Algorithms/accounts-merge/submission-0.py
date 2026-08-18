class Account:
    def __init__(self, name: str, emails: List[str]) -> None:
        self.name = name
        self.emails = set(emails)

    def intersects(self, emails: List[str]) -> bool:
        for email in emails:
            if email in self.emails:
                return True

        return False

    def merge(self, emails: List[str]) -> None:
        self.emails.update(emails)

    def display(self) -> List[str]:
        return [self.name] + sorted(self.emails)


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        processed = []

        for account in accounts:
            name, emails = account[0], account[1:]

            found = False
            for current in processed:
                if current.intersects(emails):
                    found = True
                    current.merge(emails)
                    break

            if not found:
                processed.append(Account(name, emails))

        return [current.display() for current in processed]
