> These STAR stories are based on real university and project experiences.
> They are regularly refined before interviews.

# Behavioral Interview STAR Method Prep

## The STAR Technique

- **Situation:** What was the problem?
- **Task:** What did you need to do?
- **Action:** What did YOU do? (Not "we")
- **Result:** What was the outcome?

---

## Common Behavioral Questions

### The "Failure" Question
**Tell me about a time you made a mistake. How did you handle it?**

- **Situation:** During my internship, I was working on a feature for a web application involving POS system data handling.
- **Task:** I was responsible for implementing big data handling functionality.
- **Action:** I completed the work but failed to test it thoroughly before deploying to production.
- **Result:** The feature caused downtime. I took responsibility, quickly fixed the issue, worked overtime, and established a rigorous testing process to prevent future mistakes.

### The "Weakness" Question
**What is your biggest weakness?**

- **Situation:** I sometimes become too focused on details, which can impact project timelines.
- **Task:** I needed to balance attention to detail with project deadlines.
- **Action:** I set specific time limits for tasks and arranged peer reviews when needed.
- **Result:** This approach maintained quality while helping me meet deadlines more consistently.

### The "Challenge" Question
**Tell me about a time you disagreed with a team member.**

- **Situation:** A teammate preferred MongoDB while I believed SQL was more appropriate for our project.
- **Task:** We needed to decide on the database technology for our application.
- **Action:** I built a SQL prototype demonstrating its advantages and actively listened to my teammate's MongoDB arguments.
- **Result:** We compromised by using SQL for structured data and MongoDB for unstructured data, which significantly benefited the project.

---

## Technical Architecture Questions

### Explain Your App's Architecture

**Architecture Flow:**
```
Client (JSON/POST) → Flask (Validation) → Joblib (Pre-trained Model) → Response (200 OK)
```

**Detailed Breakdown:**

1. **The Client:** Sends a JSON payload via a POST request to my Flask API.
2. **The Server (Flask):** The API first validates the input to ensure no data is missing (returning a 400 error if it is).
3. **The Logic (MLOps):** Instead of training a model on the fly, I use a pre-trained model that I serialized using `joblib`. This ensures the response time is fast, typically under 100ms.
4. **The Brain:** The model (Linear Regression) receives the input, applies the learned weights ($y = mx + c$), and generates a float value.
5. **The Response:** The server formats this into a user-friendly JSON response and sends it back with a 200 OK status.

### Why Docker & CI/CD?

**Docker:** Removes "dependency hell" and ensures consistency across environments.

**CI/CD:** Automated Unit Testing prevents bugs from merging into the main branch.

> *"I used Docker to solve the 'It works on my machine' problem. By containerizing the app, I bundled the OS, Python version (3.9), and libraries (Scikit-learn) together. This guarantees that whether I deploy to AWS, Azure, or a local server, the behavior is identical.*
>
> *I used GitHub Actions (CI) to prevent bugs from reaching production. Every time I push code, the pipeline automatically runs my Unit Tests. If I accidentally break the API, the pipeline fails, and I know immediately before any user sees the error."*

---

### Q: List vs Dict (Big-O)?

**List = O(n)** (Slow for search)  
**Dict = O(1)** (Instant lookup via Hashing) — Best for databases

> *"If I use a List, searching for an employee requires checking items one by one. In the worst case (if the employee is last), this is O(n) or Linear Time. For 10 million users, that's too slow.*
>
> *A Dictionary uses a Hash Function to calculate the memory address of the record instantly. This gives us O(1) or Constant Time lookup. Whether we have 10 users or 10 million, the search speed remains nearly instant."*