def MassVote(n: int, votes: list[int]) -> str:
    total_votes = sum(votes)
    max_votes = max(votes)
    result = "no winner"

    if max_votes > total_votes / 2:
        result = f"majority winner {votes.index(max_votes) + 1}"
    elif votes.count(max_votes) == 1:
        result = f"minority winner {votes.index(max_votes) + 1}"

    return result
