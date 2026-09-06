def test_login(client):
    response = client.post('/auth/login', data={'email': 'test@example.com', 'password': 'password'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Dashboard' in response.data

def test_login_invalid(client):
    response = client.post('/auth/login', data={'email': 'test@example.com', 'password': 'wrong'}, follow_redirects=True)
    assert b'Invalid email or password' in response.data

def test_logout(client):
    client.post('/auth/login', data={'email': 'test@example.com', 'password': 'password'})
    response = client.get('/auth/logout', follow_redirects=True)
    assert b'You have been logged out.' in response.data

