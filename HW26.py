def skip(condition=False, reason=""):
    def skip_(func):
        def wrapper(*args, **kwargs):
            if condition is False:
                return func(*args, **kwargs)
            if condition:
                return print(f'{reason}')

        return wrapper

    return skip_


@skip(condition=True, reason='Skipped because of JIRA-123 bug')
def test_two_plus_two():
    assert 2 + 2 == 5
