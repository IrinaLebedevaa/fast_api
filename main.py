
from fastapi import FastAPI, Path, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import PlainTextResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


import model


app = FastAPI()  # объект приложения с помощью конструктора FstAPI из пакета
templates = Jinja2Templates(directory="templates")

@app.get("/")  # декоратор определяет путь, запросы по которому будет обрабатывать ф
def read_root():  #функция, которая обрабатывает запросы
    html_content = "<h2>Hello VODOLEY!</h2>"
    return HTMLResponse(content=html_content)

@app.get("/about")  #http://127.0.0.1:8000/about
def about():
    html_content = "<h3>About Vodoley????</h3>"
    return HTMLResponse(content=html_content)  #content задает отправляемые данные

@app.get("/text", response_class = PlainTextResponse)
def root_text():
    return "Vodoley PlainTextResponse beee"

@app.get("/eee")
def root_html():
    return FileResponse("templates/index.html", media_type="text/html")

@app.get("/users/{name}/{alone}/{stage_fear}/{social_event}/{going}/{grained}/{friends}/{post}")
def users(name: str,
          alone: int,
          stage_fear: int,
          social_event: int,
          going: int,
          grained: int,
          friends: int,
          post: int,
          request: Request
          ):
    temp = model.personality(alone, stage_fear, social_event, going, grained, friends, post)
    result = temp.to_dict()[0]
    return templates.TemplateResponse("index.html", {
        "request": request,      # обязательно
        "name": name,
        "prediction": result
    })
    #return HTMLResponse(f'{name} - вы {temp.to_dict()[0]}')
