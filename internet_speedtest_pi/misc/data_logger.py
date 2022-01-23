from __future__ import annotations

from csv import DictWriter, reader, writer
from pathlib import Path

import loguru

from internet_speedtest_pi.config.config import settings
from internet_speedtest_pi.misc.logger import setup_logger

logger: loguru.Logger = setup_logger()  # pylint: disable=E1101


def data_logger(data_dict: dict, file_path: str | Path | None = None) -> None:
    """
    Append results to CSV file. Generates a new CSV file if CSV is not existing.

    :param data_dict: Dictionary with headers as keys and data as values
    :param file_path: Path to CSV file
    """
    logger.debug("Setting up file path...")

    if file_path is None:
        file_path = Path(__file__).resolve().parents[2] / settings.data_logging["file"]

    if not isinstance(file_path, Path):
        file_path = Path(file_path).resolve()

    file_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = list(data_dict.keys())

    logger.debug("Assuring header...")

    assure_header(file_path=file_path, header=fieldnames)

    logger.debug(f"Writing results into file {file_path}...")

    with open(file_path, "a") as file:
        dict_writer = DictWriter(file, fieldnames=fieldnames)

        dict_writer.writerow(data_dict)

    logger.info(f"Wrote results into file {file_path}.")


def assure_header(
    file_path: Path,
    header: list,
) -> None:
    """
    Assures that the CSV file has the desired header

    :param file_path: Path to CSV file
    :param header: Desired header
    """
    # assure CSV file exists
    if not file_path.is_file():
        with open(file_path, "w") as _:
            logger.info(f"Created CSV file {file_path}.")

    # get data from CSV file
    with open(file_path, "r", newline="") as file:
        reader_file = reader(file)
        data = [line for line in reader_file]

    # return if header is already correct
    if data and data[0] == header:  # type:ignore
        logger.debug(f"Header in CSV file {file_path} already correct.")
        return

    # add header if missing
    with open(file_path, "w", newline="") as file:
        writer_file = writer(file)
        writer_file.writerow(header)

        if data:
            writer_file.writerows(data)  # type:ignore

    logger.info(f"Added header to CSV file {file_path}.")
