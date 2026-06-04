# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

A Python learning project following a video course on working with the Anthropic Claude API. The course progresses from basic API calls through multi-turn conversations, tool use, RAG pipelines, MCP servers, and agent architectures.

## Commands

```bash
# Run the main script
uv run main.py

# Install dependencies
uv sync

# Inspect an MCP server during development
mcp dev server.py
```

Python 3.14+ is required (`requires-python = ">=3.14"` in `pyproject.toml`).

## Architecture

**`docs/notes.xml`** is the primary reference resource for this project. It contains structured XML course notes designed to be included as context in Claude prompts (system or user messages). The `<critical>` block at the top instructs how to use the notes.

The course curriculum covered in the notes (in order):
1. Claude model families and API access
2. Making requests, multi-turn conversations, system prompts, temperature, streaming
3. Controlling output (prefilling assistant messages, stop sequences, structured data)
4. Prompt evaluation workflows and grading (model-based and code-based graders)
5. Prompt engineering techniques (clarity, specificity, XML tags, few-shot examples)
6. Tool use — schemas, multi-turn tool loops, parallel tool calls (batch tool), structured data extraction via tools
7. Built-in tools — text editor tool, web search tool
8. RAG pipelines — chunking strategies, text embeddings (Voyage AI), vector indexes, BM25 lexical search, hybrid search with Reciprocal Rank Fusion, reranking, contextual retrieval
9. Extended thinking, vision (images/PDFs), citations, prompt caching, Files API, code execution
10. MCP — servers, clients, resources, prompts, MCP Inspector (`mcp dev`)
11. Claude Code usage patterns (init, memory, parallel worktrees, automated debugging)
12. Computer use
13. Workflows vs agents — chaining, parallelization, routing, evaluator-optimizer patterns

## Key Patterns from the Course

**Tool use loop** (`stop_reason == "tool_use"`): call Claude → append assistant response → execute tools → append tool results as user message → repeat until `stop_reason != "tool_use"`.

**Structured output**: prefill assistant message with ` ```json` + stop sequence ` ``` ` to get raw JSON without commentary.

**Prompt caching**: add `"cache_control": {"type": "ephemeral"}` to tool schemas (last tool in list) and/or system prompt blocks. Requires ≥1024 tokens to cache; max 4 breakpoints per request.

**RAG retrieval order**: vector search + BM25 in parallel → Reciprocal Rank Fusion merge → optional LLM reranker → inject top-K chunks into prompt.

**MCP tools**: use `@mcp.tool` decorator with typed parameters and `Field()` descriptions; SDK auto-generates JSON schemas. Test servers with `mcp dev server.py`.
