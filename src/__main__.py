import uvicorn

def main():
    uvicorn.run(
        app="src.server:app",
        host="0.0.0.0",
        port=8085
    )

if __name__ == '__main__':
    main()