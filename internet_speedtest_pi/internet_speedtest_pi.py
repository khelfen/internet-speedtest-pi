from __future__ import annotations

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

from collections import OrderedDict
from time import perf_counter

import loguru
import speedtest

from internet_speedtest_pi.misc.data_logger import data_logger
from internet_speedtest_pi.misc.logger import setup_logger

logger: loguru.Logger = setup_logger()  # pylint: disable=E1101


def run_speedtest() -> None:
    try:
        logger.info("Running Speedtest...")

        t0 = perf_counter()

        logger.debug("Setup Speedtest...")
        test = speedtest.Speedtest()

        results_dict = {}

        logger.debug("Run download Speedtest...")
        results_dict["download_speed"] = test.download()

        logger.debug("Run upload Speedtest...")
        results_dict["upload_speed"] = test.upload()

        # get other relevant results
        results_dict.update(
            {
                # get ping in ms
                "ping": test.results.ping,
                # get timestamp
                "timestamp": test.results.timestamp,
                # get client ip
                "client_ip": test.results.client["ip"],
                # get server name & url
                "server_name": test.results.server["name"],
                "server_url": test.results.server["url"],
            }
        )

        # assure results always have the same order
        ordered_results_dict = OrderedDict(sorted(results_dict.items()))

        t1 = perf_counter() - t0

        logger.info(f"Finished Speedtest in {t1:.2f} seconds.")

        data_logger(data_dict=ordered_results_dict)

        logger.info("Finished successfully!")

    except Exception:
        # TODO: Implement automatic E-Mail to inform about error
        logger.exception("Failed run with the following exception:")
