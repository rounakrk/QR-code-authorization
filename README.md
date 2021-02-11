# QR-code-authorization
Here with the help of pyzbar library, we are detecting the data present in the qrcode or barcode and in another file with the help of qrcode library we are generating qr codes.<br>
Here you can create your own virtual environment and install all the libraries into it. I will uploading the requirements.txt after the front end is being taken care of.<br>

This code will create and enable the virtual environment created.<br>
```
$ python -m venv qr_env
$ source rq_env\Scripts\activate
```

And with the help of cryptography library, which is used for the encryption and decryption for the employee information like password.<br>
```
$ pip install cryptography
```

And for handling and storing the data we are using POSTGRESQL database and psycopg2 library in python to get connected and perform the database operation.<br>
```
$ pip install psycopg2
```

For importing the library<br>
```Python
# for handling postgresql database operations
import psycopg2

#for encryption and decryption
import cryptography
from cryptography.fernet import Fernet #here I am using Fernet for encrytion and decryption you cann use some other methods too.
```

### The database columns used are
* EMP_ID (PK)
* NAME
* EMAIL
* PASSWORD
* PASSKEY

I will be attaching all the links for sources and materials to know about these packages and library as I will progressed.<br>
For any queries reach out to me in [Linkedin](https://www.linkedin.com/in/rounakrk/)
