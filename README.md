# asqav + CrewAI Example

Add governance and audit trails to CrewAI multi-agent teams.

## What this does

Hooks into a CrewAI crew using `AsqavCrewHook`. Every agent action, task handoff, and tool call across your entire team gets logged to an immutable audit trail - you see exactly which agent did what and when.

## Quick start

```bash
pip install -r requirements.txt
cp .env.example .env
# Add your keys to .env
python main.py
```

## What you get

```
[asqav] Crew session started: b]2e7...
[asqav] Agent: Researcher - task_start: "Find recent AI governance frameworks"
[asqav] Agent: Researcher - tool_use: search_internet
[asqav] Agent: Researcher - task_complete (1247 tokens)
[asqav] Agent: Writer - task_start: "Summarize findings"
[asqav] Agent: Writer - task_complete (832 tokens)
[asqav] Crew finished: 5 events across 2 agents, chain integrity: valid
```

Full trace of your multi-agent workflow. Every event hash-chained. If an agent misbehaves or results get tampered with, the audit trail shows it.

## How it works

```python
from asqav.integrations.crewai import AsqavCrewHook

hook = AsqavCrewHook()
crew = Crew(agents=[...], tasks=[...])

# One line - attach the hook
crew.kickoff(hooks=[hook])
```

Your crew runs exactly the same. You just get a tamper-evident record of everything that happened.

## Requirements

- Python 3.10+
- OpenAI API key (for CrewAI agents)
- asqav API key (free tier at [asqav.com](https://asqav.com))
