## Oxford.py – A simple wrapper for the Oxford API.

#### What is this package for?

This package is a wrapper for the Oxford API. 
Why? The Oxford API returns large amount of `dict` which hard to read, so we decided to simplify it for the users. 
(Get your API key and App ID from https://developer.oxforddictionaries.com/)

#### Usage
The package provides 2 classes, `SyncClient` and `AsyncClient`. 
The methods for the `AsyncClient` class are asynchronous and the methods for the `SyncClient` class are synchronous, but the same.
If the `debug` variable is set to true when creating the `SyncClient` or `AsyncClient` object, the package will print the parsed api response to the console.

Synchronous Example:
```python
from oxford import SyncClient

client = SyncClient("your_app_id", "your_app_key", language="en-gb")

def main():
    definition = client.define("People")[0]  # so we get the first definition
    print(definition)

main()
```

Asynchronous Example:
```python
from oxford import AsyncClient
import asyncio

client = AsyncClient("your_app_id", "your_app_key", language="en-gb")


async def main():
    definitions = await client.define("People")
    definition = definitions[0]  # so we get the first definition
    print(definition)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

```

#### Documentation

`SyncClient.api_request`
This returns the whole massive API response wrapped in a `dict`, so if you want to work with this you can.

`SyncClient.get_word_definition(word: str)` (or `SyncClient.define(word: str)`)
This returns an array with all definitions of the word.

`SyncClient.get_word_examples(word: str)`
This returns an array with example phrases and/or sentences of the word.

`SyncClient.get_audio_file(word: str)`
This returns an url to an audio file containing the word's pronunciation.

`SyncClient.get_synonyms(word: str)`
This returns an array with synonyms of the word.

`WordNotFoundException`
This exception is thrown if the word is not found in the dictionary (or the server returns a 404). If debug is set to true, the server response will be printed to the console.

`HttpException`
This exception is thrown if the server returns anything other than 404 or 200 together with a message to help with debugging. If debug is set to true, the server response will be printed to the console.


[This package is open source. Contribute here.](https://github.com/ProjectsWithPython/Oxford.py)