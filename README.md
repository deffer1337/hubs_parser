# Hub parser from habr.com

### How to use it?
1. You should create a **.env** file in the src directory  like .env.example in root directory
2. Activate virtual env via pipenv
3. You should **make createsuperuser** for django admin
4. Create a hub via django admin. Use **make build** and then **make web**
5. Finally **make run_hubs_parser**