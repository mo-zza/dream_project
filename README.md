# dream_api

## This API is project Dream of Dream Hi

1. install
    **/
    apt install -y python3.7
    apt install -y python3-pip
    /*

    **/
    pip3 install flask, flask_mail, pymongo
    /*

2. use_case
- /health : API server Health check
    1. user
        - POST /login : Login Dream DApp
        - GET /user : Create user

    2. report
        - POST /regist : Report violence
        - POST /modify : Update or Change report status

3. comment
- Back-end developer said 'This is not REST API. This API is 'HTTP API'. Because not clean. and not description easier