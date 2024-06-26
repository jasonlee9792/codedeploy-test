from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI()

    @app.get("/health-check")
    def heatlh_check():
        return "I'm good"
    
    @app.get("/test")
    def test():
        return {"result": "oauthquake-v6"}

    return app
    
app = create_app()