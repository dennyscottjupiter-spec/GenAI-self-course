# 🧠 The Complete Generative AI Roadmap
### *For the Motivated Non-Developer — A Step-by-Step Path from Zero to Fluent Generalist*

---

## How This Roadmap Is Built

This outline is split into **two tracks**:

- **Track A — Evergreen Core (Parts I–XV)** — Stable concepts that age slowly. The backbone you study once and carry forever.
- **Track B — Current Landscape (Parts XVI–XIX)** — Named models, tools, and frontier topics. Expect to refresh this section once a year.

**Sequencing logic:** each Part builds on the previous one. You can safely skip any leaf whose number you don't care about (e.g., skip `7.4.1.1` and go to `7.4.2`) without losing the thread.

**Depth convention:** up to four levels of nesting (e.g., `7.4.1.1`). Every leaf is atomic — one idea per bullet.

---

# 🟢 TRACK A — EVERGREEN CORE

---

## Part I — What AI Actually Is (And Isn't)

### 1. Defining Intelligence
- 1.1 Human intelligence — what it actually does
  - 1.1.1 Reasoning, memory, perception, learning
  - 1.1.2 Generalization — the ability to handle the unseen
  - 1.1.3 Embodiment, emotion, intuition (the parts AI lacks)
- 1.2 Machine intelligence — what it actually does
  - 1.2.1 Pattern matching at massive scale
  - 1.2.2 Statistical prediction vs. true understanding
  - 1.2.3 Why "intelligence" is a loaded word in AI discourse
- 1.3 Why this distinction matters in daily use of AI

### 2. Types of AI Systems
- 2.1 Narrow AI vs. General AI vs. Superintelligence
  - 2.1.1 Why today's AI is narrow (even when it feels general)
  - 2.1.2 AGI definitions — why there's no consensus
  - 2.1.3 Superintelligence — speculative but taken seriously
- 2.2 Symbolic AI vs. Statistical (Connectionist) AI
  - 2.2.1 The rule-based paradigm
  - 2.2.2 The learning paradigm
  - 2.2.3 Neuro-symbolic hybrids
- 2.3 The learning paradigms
  - 2.3.1 Supervised learning
  - 2.3.2 Unsupervised learning
  - 2.3.3 Self-supervised learning (the secret behind LLMs)
  - 2.3.4 Reinforcement learning
- 2.4 Where Generative AI sits in this map

### 3. A Compact History of AI
- 3.1 Pre-2012 — rule-based systems and early ML
- 3.2 2012–2017 — the deep learning revolution
  - 3.2.1 AlexNet and why GPUs changed everything
  - 3.2.2 The ImageNet moment
- 3.3 2017–2022 — the transformer era
  - 3.3.1 "Attention Is All You Need"
  - 3.3.2 BERT, GPT-2, GPT-3 — scaling wins
- 3.4 2022–present — the generative mainstream
  - 3.4.1 ChatGPT as the inflection point
  - 3.4.2 The tool, agent, and multimodal expansions

### 4. Data — The Fuel of AI
- 4.1 What counts as data
  - 4.1.1 Structured vs. unstructured
  - 4.1.2 Text, image, audio, video, sensor data
- 4.2 The training data pipeline
  - 4.2.1 Collection, filtering, deduplication
  - 4.2.2 Labeling and annotation
  - 4.2.3 Synthetic data (when real data isn't enough)
- 4.3 Data quality vs. data quantity
- 4.4 Bias in data and how it propagates into models

---

## Part II — How AI Actually Learns

### 5. Machine Learning Essentials
- 5.1 What a "model" is (the recipe analogy)
- 5.2 The training loop
  - 5.2.1 Loss functions — the scoreboard
  - 5.2.2 Gradient descent — how the model improves
  - 5.2.3 Epochs, batches, iterations
- 5.3 Evaluation discipline
  - 5.3.1 Training vs. validation vs. test splits
  - 5.3.2 Overfitting and underfitting
  - 5.3.3 Why generalization is the whole point
- 5.4 Features, labels, and targets — the vocabulary

### 6. Neural Networks — The Core Engine
- 6.1 The artificial neuron
- 6.2 Layers: input, hidden, output
- 6.3 How a network learns
  - 6.3.1 Forward pass
  - 6.3.2 Backpropagation (conceptual)
  - 6.3.3 Weights and biases — what actually gets tuned
- 6.4 Activation functions (why non-linearity matters)
  - 6.4.1 ReLU, sigmoid, tanh, softmax — intuition only
- 6.5 Depth and width — why "deep" learning is deep

### 7. Key Architectures (Conceptual)
- 7.1 Feedforward networks — the simplest case
- 7.2 Convolutional Neural Networks (CNNs) — built for images
  - 7.2.1 Filters and feature maps
  - 7.2.2 Pooling
  - 7.2.3 Why CNNs won vision before transformers
- 7.3 Recurrent Neural Networks (RNNs, LSTMs, GRUs)
  - 7.3.1 Sequence processing
  - 7.3.2 Vanishing gradients — why RNNs struggle
- 7.4 Transformers — the architecture that changed everything
  - 7.4.1 The attention mechanism
    - 7.4.1.1 Query, key, value intuition
    - 7.4.1.2 What "attention" really attends to
  - 7.4.2 Self-attention vs. cross-attention
  - 7.4.3 Multi-head attention
  - 7.4.4 Positional encoding — giving order to tokens
  - 7.4.5 Encoder-only, decoder-only, encoder-decoder
  - 7.4.6 Why transformers beat everything before them

---

## Part III — What Makes AI "Generative"

### 8. Generative vs. Discriminative
- 8.1 Predicting a label vs. producing new content
- 8.2 The probability-distribution mindset
- 8.3 Sampling — why the same prompt gives different answers
- 8.4 Deterministic vs. stochastic outputs

### 9. Core Generative Architectures
- 9.1 Autoregressive models (the GPT family)
  - 9.1.1 Next-token prediction as one task to rule them all
  - 9.1.2 Left-to-right generation
- 9.2 Variational Autoencoders (VAEs)
  - 9.2.1 Encoding and decoding
  - 9.2.2 The latent space
- 9.3 Generative Adversarial Networks (GANs)
  - 9.3.1 Generator vs. discriminator
  - 9.3.2 What GANs excel at and fail at
- 9.4 Diffusion models
  - 9.4.1 Forward process — adding noise
  - 9.4.2 Reverse process — learned denoising
  - 9.4.3 Latent diffusion (why Stable Diffusion is fast)
  - 9.4.4 Why diffusion dominates image generation
- 9.5 Flow-based models — a brief overview
- 9.6 Hybrid approaches (diffusion + transformers)

### 10. Tokens, Embeddings, and Latent Space
- 10.1 Tokens and tokenization
  - 10.1.1 Why text gets split
  - 10.1.2 Byte-pair encoding — conceptual
  - 10.1.3 Tokens ≠ words (and why it matters)
- 10.2 Vector embeddings
  - 10.2.1 Meaning as coordinates
  - 10.2.2 Distance and similarity
  - 10.2.3 The universal role of embeddings
- 10.3 The latent space intuition
- 10.4 Why everything — text, image, audio — lives in the same math

---

## Part IV — How Generative Models Are Trained

### 11. The Training Pipeline
- 11.1 Pre-training
  - 11.1.1 Dataset scale (trillions of tokens)
  - 11.1.2 Compute requirements
  - 11.1.3 What the model actually learns here
- 11.2 Fine-tuning
  - 11.2.1 Supervised fine-tuning (SFT)
  - 11.2.2 Instruction tuning
  - 11.2.3 Domain adaptation
- 11.3 Alignment (the "make it helpful and safe" stage)
  - 11.3.1 Why base models are hard to use directly
  - 11.3.2 RLHF — Reinforcement Learning from Human Feedback
    - 11.3.2.1 Collecting human preferences
    - 11.3.2.2 Training a reward model
    - 11.3.2.3 PPO (conceptual)
  - 11.3.3 DPO — Direct Preference Optimization
  - 11.3.4 Constitutional AI (Anthropic's approach)
  - 11.3.5 AI-assisted and RLAIF methods
- 11.4 Parameter-efficient fine-tuning (PEFT)
  - 11.4.1 LoRA — Low-Rank Adaptation
  - 11.4.2 QLoRA
  - 11.4.3 Adapters and prefix tuning

### 12. Parameters, Weights, and Scale
- 12.1 What "7B", "70B", "405B" actually mean
- 12.2 Emergent abilities with scale
- 12.3 Scaling laws (Chinchilla and beyond) — conceptual
- 12.4 Mixture-of-Experts (MoE) — getting more model for less compute
- 12.5 Parameter efficiency vs. raw size
- 12.6 Why bigger isn't always better anymore

---

## Part V — Large Language Models (LLMs)

### 13. What an LLM Is
- 13.1 Next-token prediction as the single objective
- 13.2 Why that objective generalizes to everything
- 13.3 Model variants
  - 13.3.1 Base models
  - 13.3.2 Instruct models
  - 13.3.3 Chat models
  - 13.3.4 Reasoning models ("thinking" models)
- 13.4 Context windows
  - 13.4.1 What the context window contains
  - 13.4.2 Short vs. long context tradeoffs
  - 13.4.3 Needle-in-a-haystack evaluation
  - 13.4.4 Why context ≠ memory
- 13.5 Sampling parameters
  - 13.5.1 Temperature
  - 13.5.2 Top-p (nucleus sampling)
  - 13.5.3 Top-k
  - 13.5.4 Repetition penalties and stop sequences

### 14. What LLMs Know (And Don't)
- 14.1 Knowledge cutoffs
- 14.2 Hallucination
  - 14.2.1 Why it happens mechanically
  - 14.2.2 Confident vs. uncertain hallucination
  - 14.2.3 Detection strategies
- 14.3 In-context learning
  - 14.3.1 Few-shot examples
  - 14.3.2 Why "teaching in the prompt" works
- 14.4 Emergent abilities — and skepticism about them
- 14.5 The reasoning-vs-pattern-matching debate

### 15. Model Families (Evergreen Categories)
- 15.1 Closed-source frontier models
- 15.2 Open-weight models
- 15.3 Small language models (SLMs)
- 15.4 Reasoning-native models (test-time compute)
- 15.5 Multimodal-native models
- 15.6 Coding-specialized models
- 15.7 Domain-specialized models (medical, legal, scientific)

---

## Part VI — Multimodal AI

### 16. The Multimodal Shift
- 16.1 Why modalities are converging
- 16.2 Unified representation spaces
- 16.3 The path toward any-to-any models

### 17. Vision-Language Models
- 17.1 How images become tokens
- 17.2 CLIP and contrastive learning (conceptual)
- 17.3 Visual reasoning capabilities
- 17.4 OCR, chart reading, document understanding

### 18. Audio AI
- 18.1 Speech-to-text (ASR)
- 18.2 Text-to-speech (TTS)
- 18.3 Voice cloning — how it works
- 18.4 Real-time voice agents
- 18.5 Music generation (conceptual)

### 19. Video AI
- 19.1 Text-to-video generation
- 19.2 Image-to-video animation
- 19.3 Video editing and enhancement
- 19.4 Deepfakes — technical reality and societal impact

### 20. Image Generation Deep Dive
- 20.1 How diffusion generates images, step by step
- 20.2 Prompting for images
  - 20.2.1 Subject, style, composition, lighting, mood
  - 20.2.2 Negative prompting
  - 20.2.3 Guidance scale (CFG)
- 20.3 Image-to-image workflows
- 20.4 Inpainting and outpainting
- 20.5 ControlNet and guided generation
- 20.6 LoRA adapters for style and subject consistency
- 20.7 Seeds and reproducibility

---

## Part VII — The Craft of Prompt Engineering

### 21. Prompting Fundamentals
- 21.1 Why prompting is a real skill
- 21.2 Anatomy of a strong prompt
  - 21.2.1 Context
  - 21.2.2 Instruction
  - 21.2.3 Input data
  - 21.2.4 Output format
  - 21.2.5 Constraints and success criteria
- 21.3 System prompts vs. user prompts
- 21.4 The model's-eye view — what the AI actually "sees"
- 21.5 Token economics — why concision matters

### 22. Core Prompting Techniques
- 22.1 Zero-shot prompting
- 22.2 Few-shot prompting
  - 22.2.1 Example selection
  - 22.2.2 Example ordering
  - 22.2.3 Diversity in examples
- 22.3 Role and persona prompting
  - 22.3.1 Expert identities
  - 22.3.2 Risks of role prompting
- 22.4 Chain-of-thought (CoT)
  - 22.4.1 "Let's think step by step"
  - 22.4.2 When CoT helps — and when it hurts
- 22.5 Tree-of-thought
- 22.6 ReAct — reasoning + action interleaved
- 22.7 Self-consistency — vote across samples
- 22.8 Self-critique and reflection

### 23. Advanced Prompt Strategies
- 23.1 Prompt chaining
  - 23.1.1 Breaking tasks into stages
  - 23.1.2 Passing outputs between steps
  - 23.1.3 Map-reduce patterns over long inputs
- 23.2 Structured-output prompting
  - 23.2.1 JSON mode
  - 23.2.2 XML tags for robust structure
  - 23.2.3 Schema-constrained generation
- 23.3 Negative prompting — telling AI what *not* to do
- 23.4 Iterative refinement
  - 23.4.1 Treating prompts as drafts
  - 23.4.2 A/B testing prompts
- 23.5 Meta-prompting
  - 23.5.1 Using AI to improve your prompts
  - 23.5.2 Automated prompt optimization loops
- 23.6 Prompt compression and summarization

### 24. Prompt Patterns by Task
- 24.1 Writing and editing
- 24.2 Summarization (extractive vs. abstractive)
- 24.3 Research and synthesis
- 24.4 Decision support and tradeoff analysis
- 24.5 Brainstorming and ideation
- 24.6 Code assistance (as a non-developer)
- 24.7 Creative writing and storytelling
- 24.8 Analysis, evaluation, and critique
- 24.9 Teaching and explanation
- 24.10 Translation and localization

### 25. Provider-Specific Conventions
- 25.1 OpenAI prompting conventions
- 25.2 Anthropic (Claude) prompting conventions
  - 25.2.1 XML tags as first-class citizens
  - 25.2.2 Long-context best practices
  - 25.2.3 Prefilling assistant responses
- 25.3 Google Gemini conventions
- 25.4 Open-source model conventions (chat templates)

### 26. Prompt Security and Failure Modes
- 26.1 Prompt injection
  - 26.1.1 Direct injection
  - 26.1.2 Indirect injection (via retrieved content)
- 26.2 Jailbreaks
- 26.3 Data exfiltration via prompts
- 26.4 Defensive prompting patterns
- 26.5 Limits of guardrails

---

## Part VIII — Retrieval and Memory (RAG)

### 27. The Memory Problem
- 27.1 Why LLMs forget between sessions
- 27.2 Knowledge cutoffs as a hard constraint
- 27.3 Context window as workspace, not memory

### 28. RAG Fundamentals
- 28.1 What RAG is — retrieve then generate
- 28.2 When to use RAG vs. fine-tuning vs. long context
- 28.3 Core components of a RAG system

### 29. Embeddings and Vector Search
- 29.1 Embedding models (what they are, how they're chosen)
- 29.2 Vector databases
  - 29.2.1 What they do, conceptually
  - 29.2.2 Approximate nearest-neighbor search
- 29.3 Chunking strategies
  - 29.3.1 Fixed-size vs. semantic chunking
  - 29.3.2 Overlap and windowing
  - 29.3.3 Hierarchical chunking
- 29.4 Hybrid search (vector + keyword)
- 29.5 Re-ranking

### 30. Advanced RAG Patterns
- 30.1 Agentic RAG
- 30.2 GraphRAG
- 30.3 Hierarchical / multi-hop retrieval
- 30.4 Query rewriting and expansion
- 30.5 Self-reflective RAG
- 30.6 Contextual retrieval

### 31. Building a "Chat with Your Documents" System (Conceptual)
- 31.1 Document ingestion pipeline
- 31.2 Indexing
- 31.3 Query pipeline
- 31.4 Response synthesis with citations
- 31.5 Evaluation — retrieval quality vs. answer quality

---

## Part IX — Fine-Tuning and Customization

### 32. When Customization Makes Sense
- 32.1 Prompting vs. RAG vs. fine-tuning — decision tree
- 32.2 Cost, complexity, and maintenance tradeoffs

### 33. Fine-Tuning, Conceptually
- 33.1 Full fine-tuning
- 33.2 Parameter-efficient fine-tuning (LoRA, QLoRA)
- 33.3 Domain adaptation vs. instruction tuning
- 33.4 What fine-tuning teaches well (style, format, tone)
- 33.5 What fine-tuning teaches *badly* (factual knowledge)

### 34. No-Code Customization
- 34.1 Custom GPTs (OpenAI)
- 34.2 Claude Projects and Project knowledge
- 34.3 Gemini Gems
- 34.4 System prompts as "poor-man's fine-tuning"
- 34.5 Uploading reference documents vs. RAG vs. fine-tuning

### 35. Distillation (Conceptual)
- 35.1 What model distillation is
- 35.2 Using large models to train small ones
- 35.3 Why distilled models are everywhere now

---

## Part X — Agentic AI (Deep Dive)

### 36. From Chatbots to Agents
- 36.1 What makes an AI "agentic"
- 36.2 The agent loop — perceive, think, act, observe
- 36.3 The autonomy spectrum
- 36.4 Agent vs. workflow vs. pipeline — the distinctions

### 37. Tool Use (Function Calling)
- 37.1 What tool use means mechanically
- 37.2 Function-calling interfaces
- 37.3 Tool descriptions as specifications
- 37.4 Parallel vs. sequential tool calls
- 37.5 Error handling and retries
- 37.6 Tool design — writing tools agents can actually use

### 38. Agent Memory
- 38.1 Short-term (in-context) memory
- 38.2 Long-term memory architectures
  - 38.2.1 Vector-store memory
  - 38.2.2 Summary-based memory
  - 38.2.3 Episodic memory
  - 38.2.4 Structured (graph) memory
- 38.3 Memory hygiene and selective forgetting

### 39. Planning and Reasoning in Agents
- 39.1 Plan-then-execute
- 39.2 ReAct-style interleaved reasoning
- 39.3 Reflection and self-correction
- 39.4 Hierarchical planning
- 39.5 When *not* to plan (reactive agents)

### 40. Multi-Agent Systems
- 40.1 Why one agent isn't always enough
- 40.2 Orchestrator-worker pattern
- 40.3 Peer collaboration
- 40.4 Debate and adversarial patterns
- 40.5 Handoffs and shared state
- 40.6 Multi-agent failure modes (cascading hallucinations, loops)

### 41. Model Context Protocol (MCP)
- 41.1 What MCP is and why it exists
- 41.2 MCP servers vs. clients vs. hosts
- 41.3 Core primitives
  - 41.3.1 Tools
  - 41.3.2 Resources
  - 41.3.3 Prompts
- 41.4 Building an MCP server (conceptual)
- 41.5 Consuming MCP servers from apps
- 41.6 MCP vs. traditional function calling
- 41.7 The emerging MCP ecosystem

### 42. Computer Use Agents
- 42.1 What "computer use" means
- 42.2 Screen perception (vision-based UI understanding)
- 42.3 Mouse and keyboard control
- 42.4 Browser-use agents vs. full-desktop agents
- 42.5 Limits, risks, and sandboxing

### 43. Coding Agents (CLI and IDE)
- 43.1 What Claude Code is
  - 43.1.1 Terminal-native agentic workflows
  - 43.1.2 File-system awareness and repo navigation
  - 43.1.3 Plan mode vs. execution mode
  - 43.1.4 Subagents and delegation
  - 43.1.5 Hooks and slash commands
- 43.2 The CLI coding agent family
  - 43.2.1 Aider
  - 43.2.2 Cline / Roo Code
  - 43.2.3 Codex CLI
  - 43.2.4 OpenHands
- 43.3 The IDE coding agent family
  - 43.3.1 Cursor
  - 43.3.2 GitHub Copilot
  - 43.3.3 Windsurf
  - 43.3.4 Zed AI
- 43.4 CLI vs. IDE — when each wins
- 43.5 Working style patterns (pair programming, autonomous, review-only)

### 44. SKILL.md and the Skills Paradigm
- 44.1 What a "skill" is in this paradigm
- 44.2 The SKILL.md format
  - 44.2.1 Frontmatter — name and description
  - 44.2.2 The description as router — how skills get triggered
  - 44.2.3 Body structure and conventions
  - 44.2.4 Referenced files and resources
- 44.3 Skill discovery and triggering logic
- 44.4 Skills vs. prompts vs. fine-tuning — the right tool for the job
- 44.5 Composable skills (calling skills from skills)
- 44.6 Public skills vs. personal skills vs. team skills
- 44.7 Designing good skills
  - 44.7.1 Scope and boundaries
  - 44.7.2 Writing the description for triggering
  - 44.7.3 Avoiding scope creep
- 44.8 The skill ecosystem

### 45. Agent Evaluation
- 45.1 Task completion benchmarks
- 45.2 Coding benchmarks (SWE-bench family)
- 45.3 Computer-use benchmarks (OSWorld family)
- 45.4 Trajectory analysis
- 45.5 Failure-mode taxonomy
- 45.6 Cost, latency, and reliability metrics

---

## Part XI — Running AI Locally

### 46. Why Run AI Locally
- 46.1 Privacy and data sovereignty
- 46.2 Cost (no per-token pricing)
- 46.3 Offline capability
- 46.4 Full customization and control
- 46.5 Honest limits vs. frontier models

### 47. Open-Weight vs. Open-Source (The Distinction That Matters)
- 47.1 Open weights (you can run it)
- 47.2 Open source code (you can modify it)
- 47.3 Open training data (you can reproduce it)
- 47.4 Licensing
  - 47.4.1 Apache 2.0, MIT, BSD — truly open
  - 47.4.2 Llama license and restrictions
  - 47.4.3 "Open-washing" — when "open" isn't

### 48. Quantization
- 48.1 What quantization does
- 48.2 Precision levels — FP16, FP8, INT8, INT4, INT2
- 48.3 GGUF format
- 48.4 Quality vs. size tradeoffs (perplexity curves)
- 48.5 Mixed-precision approaches

### 49. Local Inference Stacks
- 49.1 llama.cpp (the foundation)
- 49.2 Ollama
  - 49.2.1 Installation and first run
  - 49.2.2 Model library and pulling models
  - 49.2.3 Modelfiles
  - 49.2.4 OpenAI-compatible API
  - 49.2.5 Context window configuration
  - 49.2.6 Multi-model workflows
- 49.3 LM Studio — GUI-first local AI
- 49.4 Text Generation WebUI (oobabooga)
- 49.5 vLLM — for serious throughput
- 49.6 MLX — Apple Silicon native
- 49.7 Exo and distributed local inference

### 50. Hardware Considerations
- 50.1 GPU memory as the primary constraint
- 50.2 Consumer GPUs
  - 50.2.1 NVIDIA (CUDA ecosystem)
  - 50.2.2 AMD (ROCm)
  - 50.2.3 Intel Arc
- 50.3 Apple Silicon — unified memory advantage
- 50.4 CPU-only inference
- 50.5 Edge devices (Raspberry Pi, Jetson)
- 50.6 Cloud GPU rentals (RunPod, Vast, Lambda)
- 50.7 Rule-of-thumb sizing (parameters × quantization → VRAM)

### 51. Open Model Families (Evergreen Categories)
- 51.1 Meta — Llama family
- 51.2 Mistral — Mistral and Mixtral lineages
- 51.3 Alibaba — Qwen family
- 51.4 Microsoft — Phi family (small models)
- 51.5 Google — Gemma family
- 51.6 DeepSeek family
- 51.7 Specialized open models
  - 51.7.1 Coding-specialized
  - 51.7.2 Vision-specialized
  - 51.7.3 Multilingual-specialized
  - 51.7.4 Reasoning-specialized

### 52. Local AI Workflows
- 52.1 Privacy-first personal assistant
- 52.2 Offline coding assistant
- 52.3 Local RAG over personal documents
- 52.4 Self-hosted agents
- 52.5 Hybrid routing (local for private, cloud for hard)
- 52.6 Local fine-tuning workflows

### 53. Self-Hosting the Full Stack
- 53.1 Docker and Docker Compose for AI
- 53.2 Open WebUI as the frontend
- 53.3 Reverse proxies and authentication
- 53.4 Monitoring and logging
- 53.5 Backups and model versioning
- 53.6 Secure remote access (Tailscale, Wireguard, Cloudflare Tunnel)
- 53.7 Home-lab patterns (Proxmox, bare metal, mini-PCs)

---

## Part XII — AI for Creators and Builders

### 54. AI for Writing
- 54.1 Long-form drafting workflows
- 54.2 Editing and revision loops
- 54.3 Style matching and voice preservation
- 54.4 Research-to-draft pipelines

### 55. AI for Image Creation
- 55.1 Concept ideation
- 55.2 Iterative prompting workflows
- 55.3 Style development and consistency
- 55.4 Asset production pipelines

### 56. AI for Video
- 56.1 Storyboarding with AI
- 56.2 Text-to-video generation workflow
- 56.3 AI-assisted video editing
- 56.4 Subtitling, dubbing, and translation

### 57. AI for Music and Audio
- 57.1 Music generation workflow
- 57.2 Voice design and synthetic narrators
- 57.3 Podcast production with AI
- 57.4 Stem separation and remixing

### 58. AI for Coding (From a Non-Developer's Angle)
- 58.1 Understanding unfamiliar code
- 58.2 Scripting and automation
- 58.3 Building simple tools without writing code from scratch
- 58.4 No-code platforms × AI
- 58.5 Spreadsheet and document automation
- 58.6 When to lean on AI vs. learn to code properly

### 59. Workflow and Automation Platforms (Conceptual)
- 59.1 Visual workflow builders (n8n, Make, Zapier)
- 59.2 Agent-first platforms (conceptual)
- 59.3 The "AI inside a workflow" vs. "workflow inside an agent" distinction

---

## Part XIII — Evaluation and Critical Thinking

### 60. Evaluating AI Outputs
- 60.1 Correctness
- 60.2 Factuality and groundedness
- 60.3 Relevance
- 60.4 Style, tone, and format fit
- 60.5 Safety and appropriateness

### 61. Benchmarks (Conceptually)
- 61.1 What benchmarks measure — and don't
- 61.2 Major benchmark categories
  - 61.2.1 General knowledge and reasoning
  - 61.2.2 Coding
  - 61.2.3 Math
  - 61.2.4 Agentic tasks
  - 61.2.5 Long context
  - 61.2.6 Multimodal
- 61.3 Benchmark saturation and gaming
- 61.4 Why "vibes" testing still matters

### 62. Evals for Your Own Use
- 62.1 Building a golden dataset
- 62.2 LLM-as-judge (strengths and traps)
- 62.3 Human evaluation
- 62.4 A/B testing prompts and models
- 62.5 Regression testing as models update

### 63. Critical Thinking About AI
- 63.1 Detecting hallucinations in practice
- 63.2 Source verification habits
- 63.3 Recognizing sycophancy
- 63.4 When to trust, when to verify, when to discard
- 63.5 The "AI told me so" cognitive trap
- 63.6 Epistemic humility about your own prompts

---

## Part XIV — Ethics, Safety, Law, and Society

### 64. AI Bias and Fairness
- 64.1 Sources of bias (data, labels, design, deployment)
- 64.2 Types of bias (representation, measurement, aggregation)
- 64.3 Real-world harms
- 64.4 Mitigation approaches and their limits

### 65. AI Safety and Alignment
- 65.1 The alignment problem stated clearly
- 65.2 Specification gaming and reward hacking
- 65.3 Deceptive alignment (conceptual)
- 65.4 Interpretability research
  - 65.4.1 Mechanistic interpretability
  - 65.4.2 Feature circuits and activation patching
- 65.5 Responsible Scaling Policies and frontier-model commitments
- 65.6 Existential-risk perspectives — faithful coverage
- 65.7 AI-safety skeptics — faithful coverage

### 66. Misinformation, Deepfakes, and Trust
- 66.1 The synthetic-media landscape
- 66.2 Detection tools and their limits
- 66.3 Provenance standards (C2PA, Content Credentials)
- 66.4 Watermarking approaches
- 66.5 Media literacy in the AI age

### 67. Privacy and Data Rights
- 67.1 What AI companies collect and why
- 67.2 Training-data rights
- 67.3 Opting out of training
- 67.4 Privacy-preserving techniques (federated learning, differential privacy)
- 67.5 Personal AI as a privacy strategy

### 68. Intellectual Property and Copyright
- 68.1 Training-data copyright controversies
- 68.2 Ownership of AI-generated output
- 68.3 Major legal themes and precedents
- 68.4 Using AI output commercially — practical guardrails

### 69. Regulation Landscape (Evergreen Framing)
- 69.1 Risk-based regulatory frameworks
- 69.2 Jurisdictional differences (EU, US, UK, China, Brazil)
- 69.3 Industry self-regulation and voluntary commitments
- 69.4 The compute-governance debate
- 69.5 Model cards, system cards, and transparency

### 70. AI and Work
- 70.1 Augmentation vs. replacement — nuanced reality
- 70.2 Skill shifts more than role disappearance
- 70.3 New roles emerging
- 70.4 Distributional and economic questions

---

## Part XV — Personal Mastery and Staying Current

### 71. Building AI Literacy
- 71.1 Core mental models every AI-literate person carries
- 71.2 Evaluating AI tools critically
- 71.3 Personal AI stack curation
- 71.4 Building an experimentation habit

### 72. Staying Current Without Drowning
- 72.1 Reading research papers without a PhD
  - 72.1.1 Abstract-introduction-conclusion-discussion skim pattern
  - 72.1.2 How to read arXiv strategically
- 72.2 Newsletters, podcasts, blogs — categories to follow
- 72.3 Researchers, labs, and communities — categories to follow
- 72.4 The signal-vs-noise problem
- 72.5 Personal AI research journal habit

### 73. Leading AI Adoption (For Teams and Orgs)
- 73.1 Identifying high-leverage use cases
- 73.2 Running pilot programs
- 73.3 Writing a responsible AI policy
- 73.4 Managing expectations and measuring ROI
- 73.5 Communicating AI decisions to non-technical stakeholders

### 74. Frontiers (Evergreen Framing)
- 74.1 Reasoning and planning frontiers
- 74.2 Embodied AI and robotics
- 74.3 AI × science (the AlphaFold pattern)
- 74.4 AGI definitions, debates, and milestones
- 74.5 Open questions no one has answered yet

---

# 🟡 TRACK B — CURRENT LANDSCAPE (2025–2026)

> ⚠️ **Everything below is time-sensitive.** Refresh yearly. The evergreen core above does not depend on any of these specifics.

---

## Part XVI — Current Model Families

### 75. Frontier Closed Models
- 75.1 OpenAI
  - 75.1.1 GPT-5 family
  - 75.1.2 o-series reasoning models
  - 75.1.3 GPT-realtime / voice models
- 75.2 Anthropic
  - 75.2.1 Claude Opus 4.x
  - 75.2.2 Claude Sonnet 4.x
  - 75.2.3 Claude Haiku 4.x
- 75.3 Google DeepMind
  - 75.3.1 Gemini 2.x / 3.x
  - 75.3.2 Gemini reasoning variants
- 75.4 xAI — Grok family
- 75.5 Mistral — closed-tier models
- 75.6 Others worth watching (Inflection, Cohere, AI21)

### 76. Current Open-Weight Leaders
- 76.1 Llama (current generation)
- 76.2 Qwen (current generation)
- 76.3 DeepSeek (current generation)
- 76.4 Mistral / Mixtral open releases
- 76.5 Phi (current small models)
- 76.6 Gemma (current small models)
- 76.7 Specialized open models
  - 76.7.1 Coding (Qwen Coder, DeepSeek Coder, etc.)
  - 76.7.2 Vision (Qwen-VL, LLaVA family)
  - 76.7.3 Multilingual
  - 76.7.4 Reasoning (open "thinking" models)

### 77. Current Benchmark Standings
- 77.1 General reasoning
- 77.2 Coding (SWE-bench Verified, LiveCodeBench)
- 77.3 Agentic tasks (OSWorld, WebArena)
- 77.4 Long context (needle-in-haystack, RULER)
- 77.5 Multimodal
- 77.6 Safety and refusal evaluations

---

## Part XVII — Current Tool Ecosystem

### 78. Consumer Chat Interfaces
- 78.1 ChatGPT
- 78.2 Claude (web, desktop, mobile)
- 78.3 Gemini
- 78.4 Perplexity
- 78.5 Microsoft Copilot
- 78.6 Grok
- 78.7 Open-source chat frontends
  - 78.7.1 Open WebUI
  - 78.7.2 LibreChat
  - 78.7.3 AnythingLLM

### 79. Coding Assistants (Current)
- 79.1 Claude Code (CLI and beyond)
- 79.2 Cursor
- 79.3 GitHub Copilot (and Copilot Workspace / Spaces)
- 79.4 Aider
- 79.5 Cline / Roo Code
- 79.6 Codex CLI (OpenAI)
- 79.7 Windsurf
- 79.8 Zed AI
- 79.9 JetBrains AI Assistant

### 80. Productivity Integrations
- 80.1 Microsoft 365 Copilot
- 80.2 Google Workspace AI
- 80.3 Notion AI
- 80.4 Obsidian AI plugins
- 80.5 Raycast AI
- 80.6 Arc / Dia browser AI
- 80.7 Claude in Chrome and similar browser agents

### 81. Research and Search
- 81.1 Perplexity
- 81.2 ChatGPT Search and Deep Research
- 81.3 Claude Research
- 81.4 Gemini Deep Research
- 81.5 Elicit, Consensus, Semantic Scholar
- 81.6 NotebookLM

### 82. Image, Video, Voice, Music (Current Leaders)
- 82.1 Image
  - 82.1.1 Midjourney (current version)
  - 82.1.2 DALL-E / GPT Image
  - 82.1.3 Google Imagen
  - 82.1.4 FLUX family
  - 82.1.5 Stable Diffusion (current releases)
  - 82.1.6 Ideogram
- 82.2 Video
  - 82.2.1 Sora
  - 82.2.2 Google Veo
  - 82.2.3 Runway
  - 82.2.4 Kling
  - 82.2.5 Pika
  - 82.2.6 Luma
- 82.3 Voice
  - 82.3.1 ElevenLabs
  - 82.3.2 OpenAI Voice
  - 82.3.3 Play.ai
  - 82.3.4 Hume
- 82.4 Music
  - 82.4.1 Suno
  - 82.4.2 Udio

### 83. Agent and Automation Platforms (Current)
- 83.1 Zapier with AI actions
- 83.2 n8n (self-hostable)
- 83.3 Make
- 83.4 LangGraph
- 83.5 CrewAI
- 83.6 AutoGen
- 83.7 Relevance AI
- 83.8 Lindy
- 83.9 Dify

### 84. Local Inference (Current)
- 84.1 Ollama (current features)
- 84.2 LM Studio
- 84.3 Open WebUI
- 84.4 vLLM
- 84.5 llama.cpp ecosystem
- 84.6 MLX community
- 84.7 GPT4All / Jan

---

## Part XVIII — Current Frontier Topics

### 85. Reasoning Models (Current State)
- 85.1 Test-time compute as a scaling dimension
- 85.2 Chain-of-thought as training signal
- 85.3 When reasoning models help vs. hurt
- 85.4 Visible vs. hidden reasoning traces

### 86. MCP Ecosystem (Current State)
- 86.1 Major MCP servers in the wild
- 86.2 MCP adoption across vendors
- 86.3 Tooling for building and hosting MCP servers

### 87. Computer-Use Agents (Current State)
- 87.1 Anthropic Computer Use
- 87.2 OpenAI Operator and Agent Mode
- 87.3 Google Project Mariner
- 87.4 Browser-Use, Stagehand, and similar libraries

### 88. Current Skills Ecosystem
- 88.1 Anthropic's official skills
- 88.2 Community skill repositories
- 88.3 Skill marketplaces and sharing platforms

### 89. Governance Developments (Current)
- 89.1 EU AI Act — current implementation status
- 89.2 US federal and state AI action
- 89.3 China's regulatory approach
- 89.4 Voluntary commitments and frontier-model reports
- 89.5 AI Safety Institutes and third-party evaluations

---

## Part XIX — Staying Current (Living Resources)

### 90. Researchers and Thinkers to Follow (2026 Snapshot)
- 90.1 Safety and alignment voices
- 90.2 Capability-research voices
- 90.3 Applied and practitioner voices
- 90.4 Critical and heterodox voices

### 91. Newsletters and Blogs (2026 Snapshot)
- 91.1 Daily / weekly roundups
- 91.2 Technical deep-dives
- 91.3 Business and strategy
- 91.4 Policy and governance

### 92. Podcasts (2026 Snapshot)

### 93. YouTube Channels (2026 Snapshot)

### 94. Communities (2026 Snapshot)
- 94.1 Discord servers
- 94.2 Reddit subreddits
- 94.3 Hugging Face communities
- 94.4 X / Bluesky AI circles
- 94.5 Local meetups and conferences

### 95. Conferences and Events (2026 Snapshot)

---

*End of roadmap. Start anywhere, skip anything, but when in doubt — follow the numbers.*
