# base_project

## Configuración General

Versión de Python: python3.6

#### Crear aplicación de Oauth2 Toolkit: 
- Endpoint - /api/v1/applications/
  - Client type -> "Confidential"
  - Authorization grant type -> "Resource owner password-based"

#### Configurar CLIENT_ID de Oauth2 Toolkit
```python
# base_project/base_project/settings.py

# Agregar Client_id generado por Oauth2 Toolkit - /api/v1/applications/
OAUTH2_CLIENT_ID = ''
```

#### Configuración de EMAIL_HOST
```python
# base_project/base_project/settings.py

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''  # -> Email address
EMAIL_HOST_PASSWORD = ''  # -> Email password
EMAIL_PORT = 587
```

### User
| Endpoint | Parameters | Method | Response | Description | 
| --- | --- | --- | --- | --- |
| /api/v1/user/ | <ul><li>email</li><li>first_name</li><li>last_name</li><li>password</li></ul> | POST | <ul><li>detail</li></ul> | Registro de usuario |
| /api/v1/user/verify_email/ | <ul><li>token</li></ul> | POST | <ul><li>detail</li></ul> | Verificar email |
| /api/v1/user/restore_password/ | <ul><li>email</li></ul> | POST | <ul><li>detail</li></ul> | Recuperar contraseña |
| /api/v1/user/new_password/ | <ul><li>password_1</li><li>password_2</li><li>token</li></ul> | POST | <ul><li>detail</li></ul> | Nueva contraseña |

### Auth
| Endpoint | Parameters | Method | Response | Description | 
| --- | --- | --- | --- | --- |
| /api/v1/login/ | <ul><li>client_id</li><li>client_secret</li><li>grant_type --> "password"</li><li>username (email)</li><li>password</li></ul> | POST | <ul><li>access_token</li><li>expires_in</li><li>token_type</li><li>scope</li><li>refresh_token</li></ul> | Login de usuario |
