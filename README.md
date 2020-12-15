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
        - POST /join : Sign up Dream service
        - POST /login : Sign in Dream service
        - GET /email : E-mail duplication check

    2. report
        - POST /regist : post violence report
        - GET /report : read one report
        - POST /empathy : click report empathy
        - POST /support : support violence report
