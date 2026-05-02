<p align="center">
  <a href="https://asqav.com"><img src="https://asqav.com/logo-text-white.png" alt="asqav" width="150"></a>
</p>

# Asqav + CrewAI Example

Add governance and audit trails to CrewAI multi-agent teams.

## Data handling

This example uses the `asqav` Python SDK. By default, the SDK auto-detects the deployment:

- **Asqav cloud (`*.asqav.com`):** the SDK hashes your action context locally and sends only the hash plus a small metadata bag (action_type, agent_id, session_id, model_name, tool_name). Raw prompts and tool arguments never leave your infrastructure.
- **Self-hosted:** the SDK sends the full context so the server can run policy checks, PII redaction, and richer audit views.

Override per call:

```python
import asqav

asqav.init(api_key="sk_...", base_url="https://api.asqav.com", mode="hash-only")
```

This is GDPR-aware data minimization by default for cloud deployments. See [docs/fingerprint-spec.md](https://github.com/jagmarques/asqav-sdk/blob/main/docs/fingerprint-spec.md) in the SDK repo for the fingerprint spec and conformance vectors.

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

Full trace of your multi-agent workflow. Every event linked to the previous one. If an agent misbehaves or results get tampered with, the audit trail shows it.

## How it works

```python
from asqav.extras.crewai import AsqavCrewHook

hook = AsqavCrewHook()
crew = Crew(agents=[...], tasks=[...])

# Attach the hook via callbacks
crew.kickoff(step_callback=hook.on_step, task_callback=hook.on_task)
```

Your crew runs exactly the same. You just get a verifiable record of everything that happened.

## Requirements

- Python 3.10+
- OpenAI API key (for CrewAI agents)
- asqav API key (free tier at [asqav.com](https://asqav.com))
