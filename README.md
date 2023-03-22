# opml-for-mastodon

Follow mastodon accounts in an RSS reader.  Convert CSV of accounts followed into OPML.

## Usage

1. [Download accounts followed as a CSV.](https://docs.joinmastodon.org/user/moving/#export)  (Settings -> Import and export -> Data export)

2. Run the script in the same directory as the CSV file

```
python3 opml-for-mastodon.py
```

## Notes

- CSV file should be named 'following_accounts.csv'
- Don't remove the header of the CSV
