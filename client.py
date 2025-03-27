from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

html_content="""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Get and Insert</title>
</head>

<body>
    <form>
        <label for="Input">Input:</label>
        <input type="string" name="Input" />

    </form>

    <button onclick="submit()" id="insert">Insert</button>
    <button onclick="get()">Get</button>
    <div></div>
</body>
<script>

    const form = document.querySelector("form");
    const input = document.querySelector("input");
    const div = document.querySelector("div");
    function insert(e) {
        fetch("http://34.132.200.230:9567/insert/" + input.value).then(response => response.json()).then((response) => {
            div.innerHTML = JSON.stringify(response)
        })
    }

    function get(e) {
        fetch("http://34.132.200.230:9567/search/" + input.value).then(response => response.json()).then((response) => {
            div.innerHTML = JSON.stringify(response)
        })
    }

    document.getElementById("insert").addEventListener("click", insert);
</script>

</html>"""

app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return HTMLResponse(content=html_content,  status_code=200)
