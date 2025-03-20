import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("api"))

def generate_tasks(project_name: str, location: str) -> list:
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"""
    Generate a detailed construction task list for building a {project_name} in {location}.
    Return only a comma-separated list of tasks, no explanations.
    """
    
    response = model.generate_content(prompt)
    return [task.strip() for task in response.text.split(",") if task.strip()]


# #bonus:
# import asyncio
# from sqlalchemy.orm import Session

# async def simulate_task_completion(db: Session):
#     while True:
#         await asyncio.sleep(10)
#         # Get random pending task and mark as completed
#         task = db.query(models.Task).filter(
#             models.Task.status == "pending"
#         ).first()
        
#         if task:
#             task.status = "completed"
#             db.commit()