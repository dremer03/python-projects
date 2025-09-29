from fastapi import FastAPI, Path
from fastapi.responses import HTMLResponse,PlainTextResponse, FileResponse, RedirectResponse    
import os 


app = FastAPI()
 

@app.get("/", response_class=HTMLResponse)
def response_root():
    with open('web1.html', 'r',encoding='UTF-8') as file:
        data = file.read()
    return HTMLResponse(content=data)


@app.get("/html",response_class=HTMLResponse)
def response_root():
    with open('web.html', 'r',encoding='UTF-8') as file:
        data = file.read()
    return HTMLResponse(content=data)


@app.get("/link", response_class=RedirectResponse)
def response_root():
    return RedirectResponse('https://ru.wikipedia.org/wiki/%D0%91%D0%B8%D1%82%D0%BA%D0%BE%D0%B9%D0%BD', status_code=302)



@app.get("/key")
def response_root():
    path = os.getcwd()
    finall_path = os.path.join(path, "res.html")
    return FileResponse(finall_path, filename='crypto_key.html',  media_type="application/octet-stream")

