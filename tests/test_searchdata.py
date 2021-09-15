from unittest import mock

import pytest

from searchdata import SearchdataLocations, SearchdataGoogleSearch

@pytest.fixture(scope='module')
def googleSearch():
    return SearchdataGoogleSearch(api_key='API_KEY')


@pytest.fixture(scope='module')
def locations():
    return SearchdataLocations()


@mock.patch('webscrapingapi.client.request')
def test_locations(mock_request, client):
    '''It should make a GET request with the locations api url and API key'''
    googleSearch.execute("test", 10)

    mock_request.assert_called_with(
        'GET',
        'https://locations.searchdata.io/'
        '?api_key=API_KEY',
        data=None,
        headers={},
    )
    

@mock.patch('webscrapingapi.client.request')
def test_get(mock_request, client):
    '''It should make a GET request with the url and API key'''
    googleSearch.execute()

    mock_request.assert_called_with(
        'GET',
        'https://api.searchdata.io/v1'
        '?api_key=API_KEY',
        data=None,
        headers={},
    )


@mock.patch('webscrapingapi.client.request')
def test_get_with_params(mock_request, client):
    '''It should add parameters to the url'''
    googleSearch.set_q("test")
    googleSearch.execute()

    mock_request.assert_called_with(
        'GET',
        'https://api.searchdata.io/v1'
        '?q=test&api_key=API_KEY',
        data=None,
        headers={},
    )