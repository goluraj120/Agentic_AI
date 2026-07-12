from Prompt.learning_prompt import learning_prompt
from Prompt.notes_prompt import notes_prompt
from Prompt.interview_prompt import interview_prompt
from Prompt.compare_prompt import compare_prompt
from Prompt.coding_prompt import coding_prompt


PROMPTS = {
    "learning": learning_prompt,
    "notes": notes_prompt,
    "interview": interview_prompt,
    "compare": compare_prompt,
    "coding": coding_prompt,
}