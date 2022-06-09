from datetime import datetime
from AbsDate import AbsDate
from AbsTime import AbsTime
from RelTime import RelTime

class Migration:
    tables = {}

    def __init__(self):
        pass

    def add_table(self, name, columns):
        """Add a table"""
        self.tables[name] = MigrationTable(name, columns)
        return self.tables[name]

    def create_files(self, name):
        raise Exception("create_files need to be implemented in subclass")


class MigrationTable:
    def __init__(self, name, columns_default):
        self.name = name
        self.columns_required_default = []
        for column_default in columns_default:
            if isinstance(column_default, str):
                self.columns_required_default.append((column_default, True, None))
            else:
                column, default = column_default
                self.columns_required_default.append((column, False, default))
        self.rows = []


    def add_row(self, values):
        values = values.copy()
        for column, required, default in self.columns_required_default:
            column = column[1:]
            if required and not column in values:
                raise Exception("Missing value for column %s in table %s" % (column, self.name))
            if (not column in values) and (not required):
                values[column] = default

            columns = [column[1:] for column, _, _ in self.columns_required_default]
            for name in values:
                if not name in columns:
                    raise Exception("Value for non-existing column %s in table %s" % (name, self.name))

        self.rows.append(values)


    def __str__(self):
        return "The migration table format has to be specified in a subclass"


class MigrationScriptTable(MigrationTable):
    def __str__(self):
        lines = []

        for values in self.rows:
            parts = []
            for column, _, _ in self.columns_required_default:
                column = column[1:]
                parts.append("'%s': %s" % (column, self.to_str(values[column])))
            lines.append("    ops.append(fixrunner.createOp('%s', 'N', {%s}))" % (self.name, ', '.join(parts)))
        return '\n'.join(lines + [''])

    def to_str(self, value):
        if isinstance(value, str):
            return "'%s'" % value
        elif isinstance(value, AbsDate):
            return "(int(AbsTime('%s'))/24/60)" % value
        elif isinstance(value, AbsTime):
            return "int(AbsTime('%s'))" % value
        elif isinstance(value, RelTime):
            return "int(RelTime('%s'))" % value
        else:
            return str(value)


class MigrationScript(Migration):
    def add_table(self, name, columns):
        """Add a table"""
        self.tables[name] = MigrationScriptTable(name, columns)
        return self.tables[name]

    def create_files(self, name):
        myfile = open(name + '.sh', "w+")
        myfile.write(str(self))
        myfile.close()

    def __str__(self):
        lines = []

        lines.append('#!/bin/env python')
        lines.append('')
        lines.append('')
        lines.append('"""')
        lines.append('Migration script generated by generate_migration.py')
        lines.append('"""')
        lines.append('')
        lines.append('')
        lines.append('import adhoc.fixrunner as fixrunner')
        lines.append('from AbsTime import AbsTime')
        lines.append('from RelTime import RelTime')
        lines.append('')
        lines.append("__version__ = '%s'" % datetime.now())
        lines.append('')
        lines.append('@fixrunner.once')
        lines.append('@fixrunner.run')
        lines.append('def fixit(dc, *a, **k):')
        lines.append('    ops = []')
        lines.append('')
        for name in self.tables:
            lines.append(str(self.tables[name]))
        lines.append('')
        lines.append('    return ops')
        lines.append('')
        lines.append('')
        lines.append("fixit.program = 'generate_migration.py (%s)' % __version__")
        lines.append("if __name__ == '__main__':")
        lines.append('    fixit()')

        return '\n'.join(lines + [''])


class MigrationEtablesTable(MigrationTable):
    def __str__(self):
        lines = []
        lines.append(str(len(self.columns_required_default)))
        for column, _, _ in self.columns_required_default:
            lines.append('%s "%s",' % (column, column[1:]))
        lines.append('')

        for values in self.rows:
            parts = []
            for column, _, _ in self.columns_required_default:
                column = column[1:]
                parts.append(self.to_str(values[column]))
            lines.append(', '.join(parts) + ';')
        return '\n'.join(lines + [''])

    def to_str(self, value):
        if value == None:
            return 'VOID'
        elif isinstance(value, str):
            return '"%s"' % value
        elif isinstance(value, bool):
            return str(value).upper()
        else:
            return str(value)


class MigrationEtables(Migration):
    def add_table(self, name, columns):
        """Add a table"""
        self.tables[name] = MigrationEtablesTable(name, columns)
        return self.tables[name]

    def __str__(self):
        lines = []
        for name in self.tables:
            lines.append("=== %s.etab ===" % name)
            lines.append(str(self.tables[name]))
        return '\n'.join(lines + [''])


def add_test_data(migration):
    test_table = migration.add_table("test_table", ("Aabstime",
                                                    "Rreltime",
                                                    ("Iinteger", None),
                                                    "Sstring",
                                                    "Bboolean"))
    test_table.add_row({'abstime' : AbsTime("1JAN2019"),
                        'reltime' : RelTime(0),
                        'string' : 'Hej hopp',
                        'boolean' : True})

    test_table.add_row({'abstime' : AbsTime("1JAN2020"),
                        'reltime' : RelTime(1, 0),
                        'string' : 'Hej hopp 2',
                        'boolean' : False,
                        'integer' : 42})


def main():
    """Test function"""
    migration = MigrationScript()
    add_test_data(migration)
    print migration

    migration = MigrationEtables()
    add_test_data(migration)
    print migration


if __name__ == "__main__":
    main()