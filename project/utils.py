from django.db import connection
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers.sql import PostgresConsoleLexer
from sqlparse import format


def show_queries(qs):
    """Prints queries"""
    loop = 1
    for qs in connection.queries:
        print(f"QUERY {loop}")
        sqlformatted = format(qs["sql"], reindent=True)
        print(
            highlight(
                sqlformatted, PostgresConsoleLexer(), TerminalFormatter()
            )
        )
        loop += 1
