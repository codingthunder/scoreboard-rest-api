# scoreboard-rest-api
Api for your scoreboard to use in games and such.

# How to use:

Still a work in progress. If you aren't familiar with python environments, follow this instruction (on Windows. Mac and Linux users, you're on your own):

1. Clone repo to local directory.
```
git clone <git-url>
cd scoreboard-rest-api
```
2. Set up virtual environment (on Windows. Mac and Linux users, you're on your own):
```
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```
3. Run the program with uvicorn, not directly with python. Use `ctrl + c` to exit program.
    1. Run Hello World just to be sure FastAPI works.
    `uvicorn HelloWorld:hello_api --reload`
    2. Full program is the following command.
    `uvicorn scoreboard-api.main:rest_api --reload`
    3. To see the API docs, go to:
    `/docs`