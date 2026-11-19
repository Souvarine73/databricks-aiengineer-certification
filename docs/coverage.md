# Mapa de cobertura – Study Notes

Una fila por apartado de `Databricks_GenAI_Engineer_Associate_Study_Notes.md`, en el orden del documento.

**Leyenda**
- Tipo: 📘 conceptual (teoría + preguntas) · 🛠️ práctico (se construye en Free Edition)
- Estado: ⬜ pendiente · 🟡 parcial · ✅ hecho · 💳 solo en workspace de pago (explicado + alternativa)
- FE (disponibilidad en Free Edition): ✅ verificado · ❓ por comprobar en el workspace
- D: dominio del examen (D1–D6); orientativo

## Proyecto (prácticas que van creciendo)
| # | Práctica | Lecciones | Estado |
|---|---|---|---|
| P1 | Setup, Playground, `ai_query` | M01, M02 | 🟡 |
| P2 | Pipeline de documentos → chunks en Delta + CDF | RAG04 | ⬜ |
| P3 | Retrieval: índice AI Search, modos de búsqueda, Genie Agent / Lakebase | RAG01, RAG06, RAG08 | ⬜ |
| P4 | Tools: UC functions, MCP, Genie como tool, Unity Gateway | AGT01, DEP3·A | ⬜ |
| P5 | Agente con frameworks + orquestación + multi-agente + tracing | AGT04, DEP3·B | ⬜ |
| P6 | Agent Bricks y Genie | AGT07 | ⬜ |
| P7 | Evaluación offline: dataset, `evaluate()`, jueces, `@scorer`, `make_judge()` | EVAL1.1–EVAL2.5 | ⬜ |
| P8 | Evaluación online: scorers en producción, muestreo, backfill, trazas en UC | EVAL3.1, DEP5 | ⬜ |
| P9 | Despliegue: Databricks Apps + DABs, resource injection, CLI | DEP1, DEP8 | ⬜ |

---

## M01 — Introduction to Generative AI (p. 3)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A1–A3 What GenAI is, what it creates, use cases | 📘 | D1 | ✅ | – | ✅ |
| B1 LLMs and foundation models | 📘 | D3 | ✅ | – | ✅ |
| B2 From text to output | 📘 | D3 | ✅ | ✅ P1 | ✅ |
| C1 Proprietary API vs open-weight | 📘 | D3 | ✅ | – | ✅ |
| C2 Choosing a model | 🛠️ | D3 | ✅ | ✅ P1 (ai_query, 3 modelos) | ✅ |
| D1 Context engineering | 📘 | D1 | ✅ | – | ✅ |
| D2 RAG (indexing / query) | 📘 | D1 | ✅ | → P2/P3 | ✅ |
| D3 Model customization / fine-tuning | 📘 | D3 | ✅ | – | ✅ |
| E1 Agents beyond RAG | 📘 | D1 | ✅ | – | ✅ |
| Glosario | | | ✅ | | |

## M02 — Finding Success with Generative AI (p. 12)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A1–A2 Data advantage, data-native architecture | 📘 | D1 | ⬜ | – | ⬜ |
| B1 AI Functions | 🛠️ | D4 | ⬜ | ⬜ P1 | ⬜ |
| B2 Compound applications | 📘 | D1 | ⬜ | – | ⬜ |
| B3–B4 Platform & components by stage | 📘 | D4 | ⬜ | – | ⬜ |
| C1 Organizational shifts | 📘 | D1 | ⬜ | – | ⬜ |
| D1 Adoption roadmap | 📘 | D1 | ⬜ | – | ⬜ |
| E1 Data leakage, prompt injection, misuse | 📘 | D5 | ⬜ | – | ⬜ |
| E2 Defense in depth | 📘 | D5 | ⬜ | – | ⬜ |
| E3 Unity Gateway | 📘 | D6 | ⬜ | → P4 | ⬜ |
| F1 Evaluation & LLM-as-judge | 📘 | D6 | ⬜ | → P7 | ⬜ |
| Glosario | | | ⬜ | | |

## RAG01 — Retrieval Agents and Lakebase Search (p. 24)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A1–A2 Why retrieval agents, retrieval pipeline | 📘 | D1 | ⬜ | – | ⬜ |
| B1 Prompt → context → harness engineering | 📘 | D1 | ⬜ | – | ⬜ |
| C1 Genie Agents: attach a volume | 🛠️ FE ❓ | D3 | ⬜ | ⬜ P3 | ⬜ |
| C2 Knowledge source types | 📘 | D2 | ⬜ | – | ⬜ |
| C3 Declarative vs code-first | 📘 | D1 | ⬜ | – | ⬜ |
| D Lakebase | 📘 | D4 | ⬜ | – | ⬜ |
| E/E1 Lakebase Search modes | 🛠️ FE ❓ | D4 | ⬜ | ⬜ P3 | ⬜ |
| Glosario | | | ⬜ | | |

## RAG04 — Document Parsing and Chunking (p. 33)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A1 Document processing pipeline | 📘 | D2 | ⬜ | – | ⬜ |
| B1 `ai_parse_document` | 🛠️ FE ✅ | D2 | ⬜ | ⬜ P2 | ⬜ |
| C `variant_explode` | 🛠️ | D2 | ⬜ | ⬜ P2 | ⬜ |
| C1 `ai_classify` | 🛠️ | D2 | ⬜ | ⬜ P2 | ⬜ |
| C2 `ai_extract` | 🛠️ | D2 | ⬜ | ⬜ P2 | ⬜ |
| D1 `ai_prep_search` | 🛠️ FE ❓ | D2 | ⬜ | ⬜ P2 | ⬜ |
| D2 Chunking strategy | 📘 | D2 | ⬜ | – | ⬜ |
| D3 Embed vs retrieve columns | 📘 | D2 | ⬜ | ⬜ P2 | ⬜ |
| E1 Creating an index | 🛠️ FE ❓ | D4 | ⬜ | ⬜ P3 | ⬜ |
| E2 Sync with Change Data Feed | 🛠️ | D2 | ⬜ | ⬜ P2 | ⬜ |
| F Other AI SQL Functions | 📘 | D4 | ⬜ | – | ⬜ |
| Glosario | | | ⬜ | | |

## RAG06 — AI Search on Databricks (p. 40)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A1–A2 Embeddings, similarity search pipeline | 📘 | D4 | ⬜ | – | ⬜ |
| A3 What is AI Search | 🛠️ FE ❓ | D4 | ⬜ | ⬜ P3 | ⬜ |
| A4 Index types | 🛠️ | D4 | ⬜ | ⬜ P3 | ⬜ |
| A5 CDF for RAG / Lakebase CDF | 🛠️ | D2 | ⬜ | ⬜ P2/P3 | ⬜ |
| A6 Semantic, keyword, hybrid | 🛠️ | D2 | ⬜ | ⬜ P3 | ⬜ |
| B1 Managed vs custom RAG | 📘 | D1 | ⬜ | – | ⬜ |
| B2 Governance with UC | 📘 | D5 | ⬜ | – | ⬜ |
| C AI Search vs Lakebase Search | 📘 | D1 | ⬜ | – | ⬜ |
| Glosario | | | ⬜ | | |

## RAG08 — Appendix: Search Primitives (p. 47)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| 1 Distance metrics | 📘 | D4 | ⬜ | – | ⬜ |
| 2 ANN vector search | 📘 | D4 | ⬜ | – | ⬜ |
| 3 Lakebase ANN parameters | 📘 | D4 | ⬜ | – | ⬜ |
| 4 BM25 | 📘 | D2 | ⬜ | – | ⬜ |
| Glosario | | | ⬜ | | |

## AGT01 — Agents, MCP, and AI Governance (p. 51)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A1 Single agents | 📘 | D1 | ⬜ | – | ⬜ |
| A2 Multi-agent supervisors | 🛠️ | D3 | ⬜ | ⬜ P5 | ⬜ |
| A3 Single vs multi-agent | 📘 | D1 | ⬜ | – | ⬜ |
| A4 Agents on Databricks | 📘 | D3 | ⬜ | – | ⬜ |
| B1 MCP | 🛠️ | D4 | ⬜ | ⬜ P4 | ⬜ |
| B2 Genie Agents as tools | 🛠️ FE ❓ | D3 | ⬜ | ⬜ P4 | ⬜ |
| B3 Other tools & patterns | 📘 | D1 | ⬜ | – | ⬜ |
| C / C1 Unity Gateway, fallback | 🛠️ | D6 | ⬜ | ⬜ P4 | ⬜ |
| C2 Workspace endpoints vs UC model services | 📘 | D4 | ⬜ | ⬜ P1 | ⬜ |
| Glosario | | | ⬜ | | |

## AGT04 — Building Agents with Popular Frameworks (p. 59)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A1 LLM-driven orchestration | 🛠️ | D1 | ⬜ | ⬜ P5 | ⬜ |
| A2 Code-driven orchestration | 🛠️ | D1 | ⬜ | ⬜ P5 | ⬜ |
| B Tool decorators (`@function_tool`, `@tool`, DSPy) | 🛠️ | D3 | ⬜ | ⬜ P5 | ⬜ |
| B1 Prototype → governed tool | 🛠️ | D4 | ⬜ | ⬜ P4 | ⬜ |
| C `McpServer` (databricks_openai) | 🛠️ | D4 | ⬜ | ⬜ P4 | ⬜ |
| D Multi-agent concepts | 🛠️ | D3 | ⬜ | ⬜ P5 | ⬜ |
| E Other frameworks | 📘 | D3 | ⬜ | – | ⬜ |
| F1 Traditional ML vs agents | 📘 | D6 | ⬜ | – | ⬜ |
| F2 Hierarchical spans | 🛠️ | D6 | ⬜ | ⬜ P5 | ⬜ |
| F3 Traces in UC | 🛠️ FE ❓ | D6 | ⬜ | ⬜ P8 | ⬜ |
| Glosario | | | ⬜ | | |

## AGT07 — Agent Bricks and Genie (p. 74)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A Agent Bricks | 📘 | D1 | ⬜ | – | ⬜ |
| A1 Three-step development cycle | 🛠️ FE ❓ | D1 | ⬜ | ⬜ P6 | ⬜ |
| B Genie | 🛠️ FE ❓ | D3 | ⬜ | ⬜ P6 | ⬜ |
| Summary: which option when | 📘 | D1 | ⬜ | – | ⬜ |
| Glosario | | | ⬜ | | |

## EVAL1.1 — The Challenge of Evaluating AI Agents (p. 82)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A1–A2 Deterministic testing vs agents | 📘 | D6 | ⬜ | – | ⬜ |
| B1–B2 Multi-dimensional, safety | 📘 | D6 | ⬜ | – | ⬜ |
| C1–C2 Continuous evaluation | 📘 | D6 | ⬜ | – | ⬜ |
| D1–D3 Evaluation dataset & setup | 🛠️ | D6 | ⬜ | ⬜ P7 | ⬜ |
| Glosario | | | ⬜ | | |

## EVAL1.3 — MLflow's Evaluation Framework (p. 88)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A Evaluation stack | 📘 | D6 | ⬜ | – | ⬜ |
| B1 Dataset, scorers, predict function | 🛠️ | D6 | ⬜ | ⬜ P7 | ⬜ |
| C1–C4 `mlflow.genai.evaluate()` | 🛠️ | D6 | ⬜ | ⬜ P7 | ⬜ |
| D1–D3 Tracing, span types | 🛠️ | D6 | ⬜ | ⬜ P5 | ⬜ |
| E AI Gateway & production monitoring | 📘 | D6 | ⬜ | – | ⬜ |
| Glosario | | | ⬜ | | |

## EVAL2.1 — Built-In Judges (p. 95)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A1 Judge spectrum | 📘 | D6 | ⬜ | – | ⬜ |
| B1–B2 Built-in judges (y cuáles necesitan ground truth) | 📘 | D6 | ⬜ | – | ⬜ |
| B3 Usage pattern | 🛠️ | D6 | ⬜ | ⬜ P7 | ⬜ |
| Glosario | | | ⬜ | | |

## EVAL2.3 — Guideline Judges (p. 99)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A1 Global vs per-row (`Guidelines` vs `ExpectationsGuidelines`) | 📘 | D6 | ⬜ | – | ⬜ |
| A2 Implementation | 🛠️ | D6 | ⬜ | ⬜ P7 | ⬜ |
| B1–B2 Best practices | 📘 | D6 | ⬜ | – | ⬜ |
| Glosario | | | ⬜ | | |

## EVAL2.5 — Custom Judges and Feedback (p. 102)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A1 `@scorer` | 🛠️ | D6 | ⬜ | ⬜ P7 | ⬜ |
| B1 When custom LLM judges | 📘 | D6 | ⬜ | – | ⬜ |
| B2 `make_judge()` | 🛠️ | D6 | ⬜ | ⬜ P7 | ⬜ |
| C1–C2 `Feedback`, rationales | 🛠️ | D6 | ⬜ | ⬜ P7 | ⬜ |
| Glosario | | | ⬜ | | |

## EVAL3.1 — Offline vs. Online Evaluation (p. 107)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A1 Two approaches | 📘 | D6 | ⬜ | – | ⬜ |
| B1 Offline workflow | 🛠️ | D6 | ⬜ | ⬜ P7 | ⬜ |
| C1 Online workflow | 🛠️ FE ❓ | D6 | ⬜ | ⬜ P8 | ⬜ |
| D1–D2 When to use each, feedback loop | 📘 | D6 | ⬜ | – | ⬜ |
| E1–E2 UC governance, traces in UC | 🛠️ FE ❓ | D6 | ⬜ | ⬜ P8 | ⬜ |
| Glosario | | | ⬜ | | |

## DEP1 — Agent Deployment (p. 112)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A1 Prototype → production | 📘 | D4 | ⬜ | – | ⬜ |
| B1 Databricks Apps | 🛠️ FE ❓ | D4 | ⬜ | ⬜ P9 | ⬜ |
| B2 DABs (two-step deploy) | 🛠️ | D4 | ⬜ | ⬜ P9 | ⬜ |
| B3 Comparing deployment patterns | 📘 | D4 | ⬜ | – | ⬜ |
| B4 Resource injection | 🛠️ | D4 | ⬜ | ⬜ P9 | ⬜ |
| B5 Unity Gateway | 🛠️ | D6 | ⬜ | ⬜ P4 | ⬜ |
| Glosario | | | ⬜ | | |

## DEP3 — Tool Integration and Observability (p. 120)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A1–A2 MCP on Databricks (UC objects, Unity Gateway) | 📘 | D4 | ⬜ | – | ⬜ |
| A3 MCP lifecycle | 🛠️ FE ❓ | D4 | ⬜ | ⬜ P4 | ⬜ |
| A4 MCP in a deployed app | 🛠️ | D4 | ⬜ | ⬜ P9 | ⬜ |
| B1 Adding tracing | 🛠️ | D6 | ⬜ | ⬜ P5 | ⬜ |
| B2 Traces in production | 🛠️ | D6 | ⬜ | ⬜ P8 | ⬜ |
| B3 Traces in UC | 🛠️ FE ❓ | D6 | ⬜ | ⬜ P8 | ⬜ |
| Glosario | | | ⬜ | | |

## DEP5 — Production Evaluation and Monitoring (p. 129)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A1–A4 Scorer types in production | 🛠️ | D6 | ⬜ | ⬜ P8 | ⬜ |
| B1–B2 Multi-turn judges, sessions | 🛠️ | D6 | ⬜ | ⬜ P8 | ⬜ |
| C / C1 Online evaluation, sampling | 🛠️ FE ❓ | D6 | ⬜ | ⬜ P8 | ⬜ |
| C2 Scorer lifecycle | 🛠️ | D6 | ⬜ | ⬜ P8 | ⬜ |
| D1–D2 `get_scorer()`, stop/delete | 🛠️ | D6 | ⬜ | ⬜ P8 | ⬜ |
| E1 Metric backfill | 🛠️ | D6 | ⬜ | ⬜ P8 | ⬜ |
| E2 Traces in UC | 🛠️ | D6 | ⬜ | ⬜ P8 | ⬜ |
| Glosario | | | ⬜ | | |

## DEP8 — Appendix: Agent Bricks CLI (p. 140)
| Apartado | Tipo | D | Teoría | Práctica | Quiz |
|---|---|---|---|---|---|
| A What the CLI does | 📘 | D4 | ⬜ | – | ⬜ |
| B Three-command lifecycle | 🛠️ FE ❓ | D4 | ⬜ | ⬜ P9 | ⬜ |
| C `agent.toml` | 🛠️ | D4 | ⬜ | ⬜ P9 | ⬜ |
| D Bringing an existing agent | 📘 | D4 | ⬜ | – | ⬜ |
| E CLI vs Apps vs DABs | 📘 | D4 | ⬜ | – | ⬜ |
| Glosario | | | ⬜ | | |
