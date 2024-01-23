import pytest
import sys

# Append the specific path to the system path
sys.path.append('/opt/python')

def test_pyodbc_import():
    """
    Test to check if the pyodbc module can be imported successfully.
    """
    try:
        import pyodbc
    except ImportError:
        pytest.fail("Failed to import pyodbc")

def test_pyodbc_version():
    """
    Test to verify that the pyodbc version attribute is accessible.
    """
    import pyodbc
    assert hasattr(pyodbc, 'version'), "pyodbc has no attribute 'version'"

def test_pyodbc_drivers_contains_sql_server():
    """
    Test to verify that "SQL Server" is in the list of drivers returned by pyodbc.drivers().
    """
    import pyodbc
    assert callable(pyodbc.drivers), "pyodbc.drivers is not callable"
    drivers = pyodbc.drivers()
    assert isinstance(drivers, list), "pyodbc.drivers() did not return a list"
    assert any("SQL Server" in driver for driver in drivers), "'SQL Server' not found in any of the pyodbc drivers"