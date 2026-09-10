from fastapi import APIRouter
from pydantic import BaseModel
from sqlalchemy import text
import pandas as pd

from backend.database import engine
from backend.services.agent_workflow import AgentWorkflow


router = APIRouter(prefix="/api", tags=["Analysis"])


class AnalysisRequest(BaseModel):
    query: str


@router.post("/analyze")
def analyze_business_query(request: AnalysisRequest):

    workflow = AgentWorkflow()

    # Understand the business question
    intent = workflow.query_agent.understand(request.query)

    # Generate SQL from the business question
    sql_result = workflow.sql_agent.generate(intent)

    # Execute generated SQL against PostgreSQL
    with engine.connect() as connection:
        result = connection.execute(text(sql_result.query))

        data = pd.DataFrame(
            result.fetchall(),
            columns=result.keys(),
        )

    # Continue the agent workflow using database results
    analysis_result = workflow.analysis_agent.analyze(data)

    return {
        "query": request.query,
        "sql": sql_result.query,
        "sql_explanation": sql_result.explanation,
        "analysis": analysis_result.metrics,
        "data": data.to_dict("records"),
    }