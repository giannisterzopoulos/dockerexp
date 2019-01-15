
class SpecificRouter:
    """
    A router to control all database operations on models in the
    user application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read user models go to users_db.
        """
        # print('------')
        # print(model._meta.model_name)
        # if model._meta.app_label == 'employees':
        if model._meta.model_name == 'employee':
            return 'specific'
        return None
        # ProgrammingError: relation "employees_employee" does not exist
        # LINE 1: ...irst_name", "employees_employee"."last_name" FROM "employees...

    def db_for_write(self, model, **hints):
        """
        Attempts to write user models go to users_db.
        """
        # if model._meta.app_label == 'employees':
        if model._meta.model_name == 'employee':
            return 'specific'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the user app is involved.
        """
        # if obj1._meta.app_label == 'employees' or \
        #    obj2._meta.app_label == 'employees':
        if obj1._meta.model_name == 'employee' or \
           obj2._meta.model_name == 'employee':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth app only appears in the 'users_db'
        database.
        """
        # if app_label == 'employees':
        if model_name == 'employee':
            return db == 'specific'
        return None
