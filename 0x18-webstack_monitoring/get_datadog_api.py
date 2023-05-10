#!/usr/bin/python3
"""
Queries the datadog api client
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.dashboards_api import DashboardsApi
import os

def get_dashboard_info():
    """
    Queries the datadog api and gets information about a dashboard
    """
    configuration = Configuration()

    with ApiClient(configuration) as api_client:

        api_instance = DashboardsApi(api_client)
        response = api_instance.list_dashboards(filter_shared=False)

        print(response)


if __name__ == "__main__":
    get_dashboard_info()
