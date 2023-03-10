import pytest

@pytest.fixture
def apple_device():
    device = {'name': 'iPhone', 'color': 'silver', 'capacity': '64GB'}
    return device

def test_apple_device(apple_device):
    assert apple_device['name'] == 'iPhone'
    assert apple_device['color'] == 'silver'
    assert apple_device['capacity'] == '64GB'

import pytest
from unittest.mock import Mock

@pytest.fixture
def apple_id():
    id = {'username': 'testuser', 'password': 'testpass'}
    return id

@pytest.fixture
def apple_music_service(apple_id):
    service = Mock()
    service.is_connected.return_value = True
    return service

def test_apple_music_service(apple_music_service):
    assert apple_music_service.is_connected() == True

@pytest.fixture
def apple_id():
    id = {'username': 'testuser', 'password': 'testpass'}
    return id

@pytest.fixture
def apple_music_service(apple_id):
    service = AppleMusicService(apple_id)
    service.connect()
    return service

def test_apple_music_service(apple_music_service):
    assert apple_music_service.is_connected() == True

    
# at the very end of it to run the pytest outside
!pytest test_fixtures.py
