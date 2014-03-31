ids = {
    'Sugarpoint': 'APA91bFaPcxpCDvai9UgfWbsIvNNmkXBbdxQO3ZW5GWi-AUvWFGtuk0zQdBYN8J29an1vvifOxNi7hWkaRbj8eSYIpoZx2gjKeCw8eU7fS8T4JUK2FpSxIxM2K0dtaRHdk1Wgwx5SHaNN6DUvXPBsbMqfQY6nllWjQ',
    'Namhoon': 'APA91bG0pedHvc8WyTSXPeqthTnCkkLRoo-zvZwHzU3v_39MIyNN0ASc86O60Dh6jiNgD03CYNErtow_pBxHZkJ8rBXjXJ7teg_Jt0BfBNzVq6Hsl77DnWgqgMGFqGeUn4YetKdrUJ2ikPBXWniFqP-pRp-VNZgGHNjPkD9X_RA8VVwoo7qH7f0',
    'sender': 'APA91bFGKwonvHaVbXueKg6jWhTZRkKCKfYc3u5vo8R0e54iDFiAUKXVc2maus2PhAwpYdZm4vs6y7BKh0GygnSU0UpMNEBHMBqaT84tZCtcg79OWy-WrT0PVkJRDE3qDZyLSQfWsV0I4LL8QyMcxg7q-m3hmDxT-yzbmK0hg5Ui7-rWbwri85k'
}


def check_id(friend_id):
    for key in ids:
        if key == friend_id:
            return True
    return False
