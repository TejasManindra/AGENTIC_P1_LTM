from backend.agents.query_understanding import (
    QueryUnderstandingAgent,
)
from backend.agents.sql_generation import (
    SQLGenerationAgent,
)
from backend.agents.data_analysis import (
    DataAnalysisAgent,
)
from backend.agents.visualization import (
    VisualizationAgent,
)
from backend.agents.insight_generation import (
    InsightGenerationAgent,
)
from backend.agents.recommendation import (
    RecommendationAgent,
)


class AgentWorkflow:
    def __init__(self):
        self.query_agent = QueryUnderstandingAgent()
        self.sql_agent = SQLGenerationAgent()
        self.analysis_agent = DataAnalysisAgent()
        self.visualization_agent = VisualizationAgent()
        self.insight_agent = InsightGenerationAgent()
        self.recommendation_agent = RecommendationAgent()

    def run(self, business_query, data):
        intent = self.query_agent.understand(
            business_query
        )

        sql_result = self.sql_agent.generate(intent)

        analysis_result = self.analysis_agent.analyze(
            data
        )

        figure = self.visualization_agent.create_bar_chart(
            data=data,
            x_column="region",
            y_column="profit",
            title="Profit by Region",
        )

        insight_result = self.insight_agent.generate(
            data=data.to_dict("records"),
            dimension="region",
            metric="profit",
        )

        recommendation_result = (
            self.recommendation_agent.recommend(
                insight_result.insights
            )
        )

        return {
            "query": business_query,
            "intent": intent,
            "sql": sql_result,
            "analysis": analysis_result,
            "figure": figure,
            "insights": insight_result,
            "recommendations": recommendation_result,
        }