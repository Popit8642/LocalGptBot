from ollama import chat

import database.models as db_model
from database.database_main import session_factory


MODEL = "llama3.2"
MAX_HISTORY = 10

def ask(user_id, text):
    with session_factory() as session:
        history = session.query(db_model.UserMessages).filter_by(user_id=user_id).order_by(db_model.UserMessages.id.desc()).limit(MAX_HISTORY).all()
        history = [{"role": m.role, "content": m.content} for m in reversed(history)]

        if not history:
            history = [{"role": "system", "content": "Ты полезный ассистент. Отвечай кратко."}]

        session.add(db_model.UserMessages(user_id=user_id, role="user", content=text))

        response = chat(model=MODEL, messages=history + [{"role": "user", "content": text}])
        answer = response.message.content

        session.add(db_model.UserMessages(user_id=user_id, role="assistant", content=answer))
        session.commit()
    
        return answer