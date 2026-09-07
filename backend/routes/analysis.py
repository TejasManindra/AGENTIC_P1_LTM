import pandas as pd

from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.agent_workflow import AgentWorkflow


router = APIRouter(prefix="/api", tags=["Analysis"])


class AnalysisRequest(BaseModel):
    query: str


@router.post("/analyze")
def analyze_business_query(request: AnalysisRequest):
    data = pd.DataFrame(
        {
            "region": ["South", "North", "West"],
            "profit": [3981.50, 2450.75, 3120.25],
        }
    )

    workflow = AgentWorkflow()

    result = workflow.run(
        business_query=request.query,
        data=data,
    )

    return {
        "query": result["query"],
        "sql": result["sql"].query,
        "analysis": result["analysis"].metrics,
        "insights": result["insights"].insights,
        "recommendations": (
            result["recommendations"].recommendations
        ),
    }