# Structa

Structa is a Python architecture generator that compiles high-level design paradigms (DDD, EDD, Clean Architecture, Hexagonal, and custom styles) into real project structures.

It helps developers generate consistent, rule-based codebases instead of manually scaffolding folders and files.

---

## 🧠 Core Idea

Instead of templates, Structa uses **architecture paradigms**:

- A paradigm defines structure rules
- Structa compiles those rules into a project
- You get consistent, scalable codebases every time

Example paradigms:
- Domain-Driven Design (DDD)
- Event-Driven Design (EDD)
- Hexagonal Architecture
- Modular Monolith

---

## 🚀 Goals

- Remove boilerplate scaffolding
- Enforce architectural consistency
- Support multiple architecture styles
- Make system structure declarative

---

## 📦 Status

Early stage (v0.0.1)

- Repository initialized
- Core engine not implemented yet
- CLI not available yet

---

## 🛠 Planned CLI

- structa init my_project --paradigm ddd
- structa create module billing
- structa create command create_invoice
- structa create event invoice_created
