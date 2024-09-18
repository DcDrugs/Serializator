# Serializator

Serializator is a Python library for serialization of code written in python for its subsequent transfer in a convenient json/xml format.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Serializator.

```bash
pip install https://github.com/DcDrugs/Serializator/archive/master.zip
```

## Usage

```python
from factory.factory import serializer


# returns 'seriqlizer'
sl = serializer.get_parser("yaml")

def hello():
    print("Hello, World!")

# create JSON object from function
j_func = parser.dumps(hello)

f = parser.loads(j_func)

# call func
f()
# >>> hello
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
