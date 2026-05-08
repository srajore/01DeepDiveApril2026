# Chatbot Application – Specification Document

## 1. Overview

This document defines the full specification for building a **modular, testable, CLI-based chatbot** using:

- LangChain Core (LCEL)
- ChatOllama (`gpt-oss:120b-cloud`)
- Python

The implementation MUST strictly follow this specification and MUST pass the provided pytest test suite.

---

## 2. Goals

- Build a **stateless chatbot (no memory)**
- Ensure **clean, modular architecture**
- Implement **robust error handling**
- Guarantee **test compatibility**
- Maintain **simple and readable code**

---

## 3. High-Level Architecture

The system must be implemented in a single module:


The module MUST expose the following functions:

1. `initialize_llm`
2. `create_prompt`
3. `build_chain`
4. `get_user_input`
5. `generate_response`
6. `run_chatbot`

---

## 4. Detailed Functional Specification

---

### 4.1 initialize_llm()

#### Purpose
Initialize the LLM instance.

#### Behavior
- Instantiate:


The module MUST expose the following functions:

1. `initialize_llm`
2. `create_prompt`
3. `build_chain`
4. `get_user_input`
5. `generate_response`
6. `run_chatbot`

---

## 4. Detailed Functional Specification

---

### 4.1 initialize_llm()

#### Purpose
Initialize the LLM instance.

#### Behavior
- Instantiate:

- Return the instance

#### Error Handling
- Wrap in try-except
- On failure:
- Print error message
- Exit using:
  ```
  raise SystemExit(1)
  ```

---

### 4.2 create_prompt()

#### Purpose
Create prompt template.

#### Behavior
- Use `ChatPromptTemplate`
- Structure MUST be:


#### Output
- Return `ChatPromptTemplate` object

---

### 4.3 build_chain(prompt, llm)

#### Purpose
Create LCEL chain.

#### Behavior
- Return:


#### Output
- Return `ChatPromptTemplate` object

---

### 4.3 build_chain(prompt, llm)

#### Purpose
Create LCEL chain.

#### Behavior
- Return:


---

### 4.4 get_user_input()

#### Purpose
Handle user input safely.

#### Behavior
- Read input via `input()`
- Strip whitespace

#### Return Values
| Scenario | Return |
|--------|--------|
| Normal input | stripped string |
| Empty input | "" |
| KeyboardInterrupt | "quit" |
| EOFError | "quit" |

---

### 4.5 generate_response(chain, user_input)

#### Purpose
Invoke LLM chain.

#### Behavior
- Call:


#### Response Handling
| Type | Action |
|------|--------|
| Message object | return `response.content` |
| String | return directly |

#### Error Handling
- Catch ALL exceptions
- Return formatted message:


---

### 4.6 run_chatbot()

#### Purpose
Main execution loop.

#### Flow

1. Initialize:
 - LLM
 - Prompt
 - Chain

2. Loop:


---

### 4.6 run_chatbot()

#### Purpose
Main execution loop.

#### Flow

1. Initialize:
 - LLM
 - Prompt
 - Chain

2. Loop:


3. Get input

4. Exit Conditions:
- `"exit"`
- `"quit"`

5. Empty Input:
- Print:
  ```
  Assistant: Please enter a question or statement.
  ```
- Continue loop

6. Generate response

7. Print:


---

## 5. CLI Interaction Contract

Example session:

---

## 6. Error Handling Requirements

| Component | Requirement |
|----------|------------|
| LLM Init | Must exit with SystemExit(1) |
| Input | Must handle KeyboardInterrupt, EOFError |
| Chain | Must NOT crash on failure |
| Errors | Must be user-friendly |

---

## 7. Code Quality Requirements

### Mandatory
- Type hints
- Docstrings for all functions
- Clean naming conventions
- Readable structure

### Recommended
- Minimal logging (optional)

---

## 8. Constraints

- MUST use LCEL (`prompt | llm`)
- MUST use `ChatOllama`
- MUST use model:

- MUST NOT use:
- Memory
- Agents
- Tools
- External frameworks

---

## 9. Test Compliance (CRITICAL)

The implementation MUST pass all tests defined in:

:contentReference[oaicite:0]{index=0}

---

### 9.1 Required Behaviors from Tests

#### LLM
- Returns ChatOllama instance
- Failure → SystemExit(1)

#### Prompt
- Must include:

- MUST NOT use:
- Memory
- Agents
- Tools
- External frameworks

---

## 9. Test Compliance (CRITICAL)

The implementation MUST pass all tests defined in:

:contentReference[oaicite:0]{index=0}

---

### 9.1 Required Behaviors from Tests

#### LLM
- Returns ChatOllama instance
- Failure → SystemExit(1)

#### Prompt
- Must include:


---

## 11. Deliverables

Claude must generate:

### 1. chatbot.py
- Fully working
- No placeholders
- No pseudo-code

### 2. Compatible with pytest
- Must pass all tests without modification

---

## 12. Success Criteria

The implementation is COMPLETE only if:

- All pytest cases pass
- Code is modular and readable
- Error handling is robust
- CLI behaves exactly as specified
- No deviation from architecture

---

## 13. Anti-Patterns (DO NOT DO)

- Do NOT add memory
- Do NOT add LangChain agents
- Do NOT hardcode responses
- Do NOT ignore error handling
- Do NOT modify test expectations
- Do NOT introduce unnecessary abstractions

---

## 14. Final Instruction to Code Generator

Generate complete `chatbot.py` implementation that strictly adheres to this specification and passes all tests.