"""Self-check: partial GraphQL responses (null nodes) must not crash the build."""
import os

os.environ.setdefault('ACCESS_TOKEN', 'test')
os.environ.setdefault('USER_NAME', 'test')

import today


def test_stars_counter_skips_null_nodes():
    edges = [
        {'node': {'stargazers': {'totalCount': 3}}},
        {'node': None},  # GitHub returned an error for this repo
        {'node': {'stargazers': {'totalCount': 4}}},
    ]
    assert today.stars_counter(edges) == 7
    assert today.stars_counter([]) == 0


if __name__ == '__main__':
    test_stars_counter_skips_null_nodes()
    print('ok')
