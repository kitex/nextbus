## This is python program to consume rest API from https://svc.metrotransit.org/

### Install Application:

- Create virtual environment
```python -m venv env```

- Activate virtual environment (Windows)
``` .\env\Scripts\activate```

- Install requirements using requirement.txt
```pip install -r .\requirement.txt```

### To run this program please use:

# From Metro Blue Line to Target Field Station Platform 1 south direction

```python .\nextbus.py "METRO Blue Line" "Target Field Station Platform 1" "south"```

# From Airport Shuttle to MSP Airport Terminal 2 - Humphrey north direction
```python .\nextbus.py "Airport Shuttle" "MSP Airport Terminal 2 - Humphrey" "north"```

### Unit Test are present within test folder
## Running unit test for API response and sample for parse function for various datetime string value

```nosetests --verbosity=2 .\test\test_nextbus.py```

It contains two test cases
- Test case to test 3rd party API response is okay
- Test case for date time parser

It is not exhaustive list of test cases. 
### Todo 
- Test cases for json response for all external components
- Target.sql contains GTFS data schema that can be used to plot over GIS