# Assignment 4

## Dependencies

All dependencies are listed in the [requirements.txt](requirements.txt) file and can be installed in the following way:

```
python3 -m pip install -r requirements.txt
```

## Running

The assignment consist mainly of 3 files, which depend on the other files. These are:

- [time_planner.py](time_planner.py) - Fetches skiing events from wikipedia, displays them and can generate these tables in markdown.
- [fetch_player_statistics.py](fetch_player_statistics.py) - Fetches NBA player statistics and plots it into nice little graphs.
- [wiki_race_challenge.py](wiki_race_challenge.py) - TODO
- [collect_dates.py](collect_dates.py) - TODO

## Testing

The code includes a couple of unit tests that it should be passing. In order to run these run the following command:

```
pytest -vv tests
```
