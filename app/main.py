from fastapi import FastAPI

app = FastAPI()  # <-- Make sure this variable is named 'app'

@app.get("/")
def read_root():
    return {"message": "Hello LMS!"}
