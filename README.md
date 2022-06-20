# sheety-sdk

This is a python library for working with sheety https://sheety.co/docs/requests

Setup your sheety account and then initialize your sheety api providing url and credentials.
With this library you can easily:
- retrieve data (get_data method)
- add new rows (add_data method, accepts keyword arguments: use column names as keys)
- modify rows (edit_data method, accepts row_id and kwargs)
- delete rows (delete_data method, accepts row_id)
