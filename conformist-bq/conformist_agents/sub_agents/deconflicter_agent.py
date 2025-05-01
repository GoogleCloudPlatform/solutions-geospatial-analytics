from google.adk.agents import LlmAgent
from .. import MODEL
from .deconflicter_prompt import PROMPT as DECONFLICTER_PROMPT

DeconflicterAgent = LlmAgent(
    name="DeconflicterAgent",
    model=MODEL,
    description=(
        "Reconcile results from embedding comparison and mapper output"
    ),
    instruction=DECONFLICTER_PROMPT
)
