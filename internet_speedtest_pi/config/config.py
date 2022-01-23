from pathlib import Path

from dynaconf import Dynaconf

settings_files=['settings.toml', '.secrets.toml']
settings_files = [
    Path(__file__).resolve().parent / file for file in settings_files
]

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=settings_files,
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
