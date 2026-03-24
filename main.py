from fastapi import FastAPI, Path, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.responses import PlainTextResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import model


app = FastAPI()  # объект приложения с помощью конструктора FstAPI из пакета
templates = Jinja2Templates(directory="templates")


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


@app.post("/result", response_class=HTMLResponse)
def predict(
    request: Request,
    name: str = Form(default=5),
    alone: int = Form(default=1),
    stage_fear: int = Form(default=5),
    social_event: int = Form(default=5),
    going: int = Form(default=5),
    grained: int = Form(default=1),
    friends: int = Form(default=5),
    post: int = Form(default=5)
):
    result = model.personality(alone, stage_fear, social_event, going, grained, friends, post)
    prediction = result.to_dict()[0]

    if "Introvert" in prediction:
        return templates.TemplateResponse("introvert.html", {
            "request": request,
            "name": name,
            "description": "Ты черпаешь энергию в тишине и уединении. Ты глубоко осмысливаешь и предпочитаешь качественные связи."
        })
    elif "Extrovert" in prediction:
        return templates.TemplateResponse("extrovert.html", {
            "request": request,
            "name": name,
            "description": "Ты получаешь заряд от общения, быстро адаптируешься и легко находишь общий язык с окружающими."
        })
