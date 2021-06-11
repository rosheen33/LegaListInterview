import datetime

import psycopg2
from legalist.items import QuotesItem


class LegalistPipeline:

    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'
        password = 'postgres'
        database = 'legalist'
        port = '5433'
        self.connection = psycopg2.connect(
            host=hostname,
            user=username,
            password=password,
            dbname=database,
            port=port
        )
        self.cur = self.connection.cursor()
        self.create_tables(self.connection, self.curr)

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        if type(item) == QuotesItem:
            self.insert_in_table(item, self.connection, self.curr)
        return item

    def insert_in_table(self, quote, conn, cur):
        command = """ 
        INSERT INTO quotes_js (text, url, author, author_url, tags, updated_at)
        VALUES ('{}', '{}', '{}', '{}', ARRAY{}, '{}')
        """
        try:
            command = command.format(
                quote['text'].replace("'", '"').replace('”', '"').replace('“', '"'),
                quote['url'],
                quote['author'].replace("'", '"'),
                quote.get('author_url'),
                quote.get('tags', ['']),
                datetime.datetime.now().strftime("%m-%d-%Y, %H:%M:%S.%f")
            )
            cur.execute(command)
            # close communication with the PostgreSQL database server
            cur.close()
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def create_tables(self, conn, cur):
        """
        Create tables in the PostgreSQL database.
        Due to the shortage of time I am only creating one table here.
        But surely it can be updated and we can make separate entities for
        tags and author. Below is the basic idea of it.

        """

        commands = (
            """
            CREATE TABLE quotes
            (
                qid SERIAL NOT NULL,
                text "text" NOT NULL,
                url "text" NOT NULL,
                author "text" NOT NULL,
                author_url "text",
                tags "text"[],
                created_at timestamp default current_timestamp,
                updated_at timestamp,
                PRIMARY KEY (qid),
            )
            """,
            # """
            # CREATE TABLE quotes
            # (
            #     qid SERIAL NOT NULL,
            #     text "text" NOT NULL,
            #     url "text" NOT NULL,
            #     author "text" NOT NULL,
            #     author_url "text",
            #     tags "text"[],
            #     created_at timestamp default current_timestamp,
            #     updated_at timestamp,
            #     PRIMARY KEY (qid),
            #     CONSTRAINT fk_aid
            #       FOREIGN KEY(aid)
            #       REFERENCES author(aid)
            #     CONSTRAINT fk_tid
            #       FOREIGN KEY(tid)
            #       REFERENCES tag(tid)
            # )
            # """,
            # """
            # CREATE TABLE author
            # (
            #     aid SERIAL NOT NULL,
            #     author "text" NOT NULL,
            #     author_url "text",
            #     created_at timestamp default current_timestamp,
            #     updated_at timestamp,
            #     PRIMARY KEY (aid)
            # )
            # """,
            # """
            # CREATE TABLE tag
            # (
            #     tid SERIAL NOT NULL,
            #     tag_text "text"[],
            #     created_at timestamp default current_timestamp,
            #     updated_at timestamp,
            #     PRIMARY KEY (tid)
            # )
            # """,
        )
        try:
            for command in commands:
                cur.execute(command)
            # commit the changes
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
