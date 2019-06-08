#!/usr/bin/env python3
import psycopg2


def run_query(query):
    """Connects to the database, runs the query passed to it,
    and returns the results"""

    db = psycopg2.connect(
        user="postgres",
        password="Abc123",
        host="127.0.0.1",
        port="5432",
        database="news"
    )

    cr = db.cursor()
    cr.execute(query)
    rows = cr.fetchall()
    db.close()
    return rows


def get_top_three_articles():

    # Prepare top three most read articles query
    query = """
        SELECT articles.title, COUNT(*) AS num
        FROM articles
        JOIN log
        ON log.path = concat('/article/', articles.slug)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3;
    """
    # Go to execute query
    results = run_query(query)

    # Print output on the screen
    print('\nMOST POPULAR THREE ARTICLES OF ALL TIME:')
    counter = 1
    for i, (article, view) in enumerate(results, 1):
        print("[{}] {} -- {} views".format(i, article, view))


def get_popular_article_authors():

    # Prepare most popular authors of all time query
    query = """
        SELECT authors.name, COUNT(*) AS num
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON log.path = concat('/article/', articles.slug)
        GROUP BY authors.name
        ORDER BY num DESC
        ;
    """

    # Go to execute query.
    results = run_query(query)

    # Print output on the screen.
    print('\nMOST POPULAR ARTICLE AUTHORS OF ALL TIME:')
    counter = 1

    for i, (author, view) in enumerate(results, 1):
        print("[{}] {} -- {} views".format(i, author, view))


def get_days_with_errors():

    # Prepare days with more than 1% errors query.
    query = """
        SELECT total.day,
          ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
        FROM (
          SELECT date_trunc('day', time) "day", count(*) AS error_requests
          FROM log
          WHERE log.status != '200 OK'
          GROUP BY day
        ) AS errors
        JOIN (
          SELECT date_trunc('day', time) "day", count(*) AS requests
          FROM log
          GROUP BY day
          ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
        ORDER BY percent DESC;
    """

    # Go to execute query.
    results = run_query(query)

    # Print output on the screen.
    print('\nDAYS WITH MORE THAN 1% OF ERRORS:')

    for i in results:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1]*100, 1)) + "%" + " errors"
        # print(date + " — " + errors)
        print("{} -- {}".format(date, errors))
