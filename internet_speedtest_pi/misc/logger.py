from __future__ import annotations

import sys

from pathlib import Path, PurePath
from typing import TextIO

import loguru

from loguru import logger as base_logger

from internet_speedtest_pi.config.config import settings


def setup_logger(
    logger: loguru.Logger = base_logger,  # pylint: disable=E1101
    add_stream_handler: bool = True,
    stream_handler_level: str = "INFO",
    stream_handler_out: TextIO = sys.stderr,
    add_file_handler: bool = True,
    file_handler_level: str = "DEBUG",
    file_handler_file: str | PurePath | None = None,
) -> loguru.Logger:  # pylint: disable=E1101
    """Setup a logger. Removes all existing handlers and adds either or both a
    StreamHandler and a FileHandler if specified.

    :param logger: Base logger to setup. Defaults to the standard loguru logger
    :param add_stream_handler: Adds a StreamHandler if True. Defaults to True
    :param stream_handler_level: Set StreamHandler level. Defaults to "INFO"
    :param stream_handler_out: Set StreamHandler Output. Defaults to sys.stderr
    :param add_file_handler: Adds a FileHandler if True. Defaults to True
    :param file_handler_level: Set FileHandler level. Defaults to "DEBUG"
    :param file_handler_file: Set FileHandler log file. If None a log file is created in
    the base directory. The log file name can be set in the config settings.toml.
    :return: logger with handlers if specified
    """
    logger.remove()

    if add_stream_handler:
        logger.add(stream_handler_out, level=stream_handler_level)

    if add_file_handler:
        if file_handler_file is None:
            file_handler_file = (
                Path(__file__).resolve().parents[2] / settings.logging["file"]
            )

        logger.add(file_handler_file, level=file_handler_level)

    logger.debug("Setup logger.")

    return logger


if __name__ == "__main__":
    logger = setup_logger()
