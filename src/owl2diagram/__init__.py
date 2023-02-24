__author__ = "Jhon Toledo"
__credits__ = ["Jhon Toledo"]
__copyright__ = "Copyright © 2023 Jhon Toledo"

__license__ = "Apache-2.0"
__maintainer__ = "Jhon Toledo"
__email__ = "ja.toledo@upm.es"

# __init__.py

from importlib import resources
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

# Version of the owl2diagram package
__version__ = "1.0.0"

# Read URL of the Real Python feed from config file
#_cfg = tomllib.loads(resources.read_text("reader", "config.toml"))
#URL = _cfg["feed"]["url"]