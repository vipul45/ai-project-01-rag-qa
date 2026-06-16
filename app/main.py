from fastapi import FastAPI
app = FastAPI(title='RAG Q&A Service')

@app.get('/')
def root():
    return {'message': 'RAG Service ready!'}
