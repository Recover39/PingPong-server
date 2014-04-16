ids = {
    'Sugarpoint': 'APA91bGiQsQF22IHfKnmXWI7Ee2fM4RaSWzIL35sJz-Ra3c1T3sZu8izfMMqwmoW088K2bxRKS4jbuqgdQtA54CRAMAWTtfBxK1wL6S8pQwylqwZ3NJkcDZDYmkR21GAxstnfoX1tlVCNUhbw_B_oD--3suviQAACfswkFRmRDXK22B4zs3GocE',
    'Namhoon': 'APA91bG0pedHvc8WyTSXPeqthTnCkkLRoo-zvZwHzU3v_39MIyNN0ASc86O60Dh6jiNgD03CYNErtow_pBxHZkJ8rBXjXJ7teg_Jt0BfBNzVq6Hsl77DnWgqgMGFqGeUn4YetKdrUJ2ikPBXWniFqP-pRp-VNZgGHNjPkD9X_RA8VVwoo7qH7f0',
    'sender': 'APA91bFgouvwV3tFIGCfqJsGZmp-NBJBabw1tTkGi0HasGsYHi8PYrl51YpDs7az_d8yWIpGodthuIQWi63nnlm4UeUpoL1ULNAwN2KcrOkSn7g64iFSRhcKuXRpkvSFd0l0qBDux60rvVrQXAC3MBZlaAEX8IDfx1nGRiJ1t38KOjPC_kJr4ag'
}

def check_id(friend_id):
    for key in ids:
        if key == friend_id:
            return True
    return False
