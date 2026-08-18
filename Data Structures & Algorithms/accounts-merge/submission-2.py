class DSU:
    # Initialise `n` components with integer names from 0 to n - 1 in O(n) time.
    def __init__(self, n: int) -> None:
        self.ids = list(range(n))
        self.sizes = [1] * n
        self.components = n

    # Add a connection between `p` and `q` in O(alpha(n)) amortised time, O(log n) worst case.
    def union(self, p: int, q: int) -> None:
        pid, qid = self.find(p), self.find(q)

        if pid == qid:
            return

        if self.sizes[pid] < self.sizes[qid]:
            pid, qid = qid, pid

        self.ids[qid] = pid
        self.sizes[pid] += self.sizes[qid]
        self.components -= 1

    # Return the component identifier for `p` in O(alpha(n)) amortised time, O(log n) worst case.
    def find(self, p: int) -> int:
        if p != self.ids[p]:
            self.ids[p] = self.find(self.ids[p])

        return self.ids[p]

    # Check if `p` and `q` are in the same component in O(alpha(n)) amortised time, O(log n) worst case.
    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    # Return the number of components in O(1) time.
    def count(self) -> int:
        return self.components

    # Return all components in O(n * alpha(n)) amortised time.
    def groups(self) -> list[list[int]]:
        groups = defaultdict(list)

        for i in range(len(self.ids)):
            root = self.find(i)
            groups[root].append(i)

        return list(groups.values())


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        origins: dict[str, int] = {}

        # Merge accounts that share an email.
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in origins:
                    origins[email] = i
                    continue

                dsu.union(origins[email], i)

        # Combine the emails from each merged group.
        result = []

        for group in dsu.groups():
            name = accounts[group[0]][0]
            emails = set()

            for i in group:
                emails.update(accounts[i][1:])

            result.append([name] + sorted(emails))

        return result
