## How to start?
### Local setup
1. Enter root folder
2. Create a virtual environment
- python3 -m venv ./venv
3. Activate the virtual environment
- source ./venv/bin/activate
4. Install dependency
- pip install -r requirements.txt
5. python manage.py runserver

### docker compose setup
1. docker compose up
2. (Optional)docker-compose exec web python manage.py migrate

## I/O examples
- `/signup/`, testing request:
    
    ```bash
    curl --location 'http://127.0.0.1:8000/signup/' \
    --data-raw '{
        "email": "test@test.com",
        "password": "123"
    }'
    ```
    
    - Expected server response: {id, email} of the user
- `/signin/` , testing request:
    
    ```bash
    curl --location 'http://127.0.0.1:8000/signin/' \
    --data-raw '{
        "email": "test@test.com",
        "password": "123"
    }'
    ```
    
    - Expected server response: dict of {access_token, refresh_token}
- `/me/`, testing request:
    
    ```bash
    curl --location 'http://127.0.0.1:8000/me/' \
    --header 'Authorization: Bearer <access_token_from_signin>'
    ```
    
    - Expected server response: dict of {id, email} that associated with the token.