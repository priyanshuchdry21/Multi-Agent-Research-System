import importlib
import os
import unittest
from unittest.mock import patch

import pipeline


class AgentsInitializationTests(unittest.TestCase):
    def test_import_agents_without_model_env_uses_default(self):
        with patch.dict(os.environ, {}, clear=False):
            os.environ.pop("GENAI_MODEL", None)
            import agents
            importlib.reload(agents)
            self.assertTrue(hasattr(agents, "llm"))

    def test_pipeline_falls_back_when_model_call_fails(self):
        class FakeAgent:
            def invoke(self, *_args, **_kwargs):
                raise RuntimeError("quota exhausted")

        class FakeChain:
            def invoke(self, *_args, **_kwargs):
                return "fallback report"

        with patch.object(pipeline, "build_search_agent", return_value=FakeAgent()), \
             patch.object(pipeline, "build_reader_agent", return_value=FakeAgent()), \
             patch.object(pipeline, "writer_chain", FakeChain()), \
             patch.object(pipeline, "critic_chain", FakeChain()):
            state = pipeline.run_research_pipeline("AI")

        self.assertIn("search_results", state)
        self.assertIn("scraped_content", state)
        self.assertIn("report", state)
        self.assertIn("feedback", state)
        self.assertIn("fallback", state["report"].lower())


if __name__ == "__main__":
    unittest.main()
