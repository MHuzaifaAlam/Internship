# Python Mastery Project: Task Manager

One project, built in phases. Each phase adds real features to the same
codebase, and each feature is chosen specifically to force you to use a
group of concepts from your list. Check items off as you complete them.

---

## Phase 0 — Foundation (already started)
**Concepts:** Variables, data types, strings, f-strings, conditionals, logical operators, lists, functions, scope

- [ ] `Task` class: `title`, `done` attribute, `mark_done()`, `__str__`
- [ ] Plain functions (not yet class methods) to add/remove/list tasks from a list
- [ ] Practice variable **scope**: a function that modifies a list vs. one that tries to reassign it (see why reassignment inside a function doesn't leak out)

---

## Phase 1 — Core Data Handling
**Concepts:** Number operations, augmented assignment, slicing, string methods, `isinstance()`, list methods, list comprehension

- [ ] Task IDs auto-increment (`+=`)
- [ ] `search_tasks(keyword)` — use string methods (`.lower()`, `in`) to search titles
- [ ] `tasks[:5]` — show only the 5 most recent tasks (slicing)
- [ ] Input validation using `isinstance()` (reject non-string titles)
- [ ] Rewrite one loop-based filter as a **list comprehension**
  (e.g. `[t for t in tasks if not t.done]`)

---

## Phase 2 — Tuples, Sets, Dictionaries
**Concepts:** Tuples, `in` keyword, `*` unpacking, tuple slicing, tuple methods, dict + dict methods, sets

- [ ] Each task gets a `tags` field stored as a **tuple** (immutable once set), e.g. `("work", "urgent")`
- [ ] Use `*` unpacking to split "first tag" vs "rest of tags": `first, *rest = task.tags`
- [ ] Store tasks in a **dictionary** keyed by ID: `tasks = {1: Task(...), 2: Task(...)}`
- [ ] Use a **set** to track all unique tags used across every task (`all_tags.add(tag)`)
- [ ] `.get()`, `.keys()`, `.values()`, `.items()` on the tasks dict

---

## Phase 3 — Loops, Functional Tools
**Concepts:** `range()`, `enumerate()`, `map()`, `filter()`, `sum()`, `lambda`

- [ ] `enumerate()` to number tasks when printing a numbered list
- [ ] `filter(lambda t: t.done, tasks.values())` — get completed tasks
- [ ] `map(lambda t: t.title, tasks.values())` — get just the titles
- [ ] `sum(1 for t in tasks.values() if t.done)` — count completed tasks
- [ ] `sorted(tasks.values(), key=lambda t: t.title)` — alphabetical sort

---

## Phase 4 — Standard Library
**Concepts:** `math`, `random`, `re`, `datetime`, importing libraries

- [ ] `import random` — generate a random task ID or shuffle daily task order
- [ ] `import datetime` — add `created_at` / `due_date` to each task; sort by due date
- [ ] `import re` — validate task titles (no special characters, length limits)
- [ ] `import math` — compute stats, e.g. average tasks completed per day (rounding, ceiling)

---

## Phase 5 — Iterators & Generators
**Concepts:** Iterators, generators

- [ ] Make `TaskManager` itself iterable: implement `__iter__` and `__next__`
      so you can do `for task in manager:`
- [ ] Write a **generator function** `pending_tasks()` that `yield`s only
      incomplete tasks one at a time, instead of building a full list

---

## Phase 6 — OOP Deep Dive
**Concepts:** Attributes, class attributes, instance methods, access/property methods,
decorators, encapsulation, inheritance, polymorphism, abstraction

- [ ] **Class attribute**: `Task.total_created` — a counter shared across all instances, incremented in `__init__`
- [ ] **Encapsulation**: make `done` private (`self._done`), add a `@property` getter and a controlled setter
- [ ] **Decorator**: write `@log_action` that wraps `add_task`/`complete_task` and prints a log line every time they're called
- [ ] **Inheritance**: create `RecurringTask(Task)` and `UrgentTask(Task)` subclasses that override behavior
- [ ] **Polymorphism**: call `.describe()` on a mixed list of `Task`/`RecurringTask`/`UrgentTask` objects — each returns a different string, same method name
- [ ] **Abstraction**: define an `abstract base class` (`from abc import ABC, abstractmethod`) that forces every task subtype to implement `.describe()`

---

## Phase 7 — Collections Module
**Concepts:** `Counter`, `OrderedDict`, `defaultdict`, `ChainMap`, `namedtuple`, `deque`, `UserDict`, `UserString`

- [ ] `Counter` — count how many tasks exist per tag
- [ ] `defaultdict(list)` — group tasks by tag automatically without checking "does this key exist"
- [ ] `deque` — implement an **undo history** (push completed/removed actions, pop to undo)
- [ ] `namedtuple` — lightweight `TaskSummary(id, title, done)` for quick reporting, without a full class
- [ ] (Optional, exploratory) `ChainMap` — merge default settings + user settings for the app; `UserDict`/`UserString` — subclass to build a custom dict/string type with extra validation

---

## Phase 8 — itertools, Stack & Queue
**Concepts:** `itertools`, stack, queue

- [ ] Implement **undo** as a stack (Python list, `.append()`/`.pop()` from the end)
- [ ] Implement a **task processing queue** using `collections.deque` (`.popleft()`)
- [ ] `itertools.combinations` — generate all possible tag-pair filters
- [ ] `itertools.groupby` — group a sorted task list by tag or due date

---

## Phase 9 — Algorithms & Complexity
**Concepts:** Time complexity, space complexity, binary search, divide and conquer, merge sort

- [ ] Implement **binary search** yourself to find a task by ID in a sorted list — compare against a linear search, discuss Big-O difference
- [ ] Implement **merge sort** yourself to sort tasks by due date — compare against Python's built-in `sorted()`
- [ ] Write a short note (in comments) on the time/space complexity of each function you've built so far — this is the habit that matters most long-term

---

## How to work through this

1. **Don't skip ahead** — each phase assumes the previous phase's code still works. You're extending one growing file, not writing throwaway snippets.
2. **One checkbox at a time.** Write it, test it, then bring it to me to review before moving to the next.
3. When a phase introduces something genuinely new (decorators, generators, ABCs), expect to spend more time there — that's normal, not a sign you're behind.
4. By the end of Phase 9, you'll have one command-line app that legitimately exercises almost every concept on your list, and — more importantly — you'll have felt *why* each concept exists, because you needed it to solve a real problem in your own code.
