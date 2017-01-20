import sqlite3


class SQLighter:
    def __init__(self, database):
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    # метод выбора записи проекта
    def select_project(self, id):
        with self.connection:
            return self.cursor.execute("SELECT project_name, project_manager, begin_date, deadline, end_date, comments FROM projects WHERE id = ?", (id,)).fetchall()

    # метод выборки всех проектов таблицы projects
    def select_all_projects(self):
        with self.connection:
            return self.cursor.execute("SELECT * FROM projects").fetchall()

    def close(self):
        self.connection.close()
