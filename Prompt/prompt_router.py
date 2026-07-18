from Prompt.Teacher_prompt.learning_prompt import learning_prompt
from Prompt.Teacher_prompt.coding_prompt import coding_prompt
from Prompt.Teacher_prompt.interview_prompt import interview_prompt
from Prompt.Teacher_prompt.notes_prompt import notes_prompt
from Prompt.Teacher_prompt.compare_prompt import compare_prompt
from Prompt.quiz_prompt import quiz_prompt


PROMPTS = {
    "learning": learning_prompt,
    "notes": notes_prompt,
    "interview": interview_prompt,
    "compare": compare_prompt,
    "coding": coding_prompt,
    "quiz": quiz_prompt,
    
}