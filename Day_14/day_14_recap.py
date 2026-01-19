
"""DAY 14 RECAP — MUST MEMORIZE (School API Integration)

Big idea:
- Flask is the "waiter" (handles requests).
- JSON file is the "memory" (persists after restart).
- A Python dict is the in-memory "database" (fast lookups).

1) Persistence Rule (THIS is the whole project)
- If you only store data in variables, it disappears when Python stops.
- To remember data after restart:
	1) data = load_db()      # read JSON -> dict
	2) change data           # add/update/remove
	3) save_db(data)         # dict -> JSON

2) The DB Shape (very important)
- data is a dictionary like:
		data = {
				"101": {"name": "John", "age": 20},
				"102": {"name": "Ayesha", "age": 22}
		}
- Keys are strings ("101" not 101) because URLs + JSON keys are strings.

3) Routes (memorize what each one does)
- GET /students
	- loads DB, returns ALL students
- POST /students
	- reads request.json (the student object)
	- validates required fields (ex: name)
	- loads DB, adds new student, saves DB
	- returns message + new id
- GET /students/<student_id>
	- loads DB
	- if id exists: return that student
	- else: return 404

4) request.json vs jsonify (don’t mix them up)
- request.json = incoming JSON from the user (client -> server)
- jsonify(...) = outgoing JSON response (server -> client)

5) Why dict lookup is "fast"
- "if student_id in data" is an O(1) average-time lookup.

6) Common mistakes (avoid these)
- Forgetting to call save_db(data) after changing data.
- Expecting browser typing to "POST" (browser address bar only does GET).
- Visiting / and getting 404 (normal unless you create a route for '/').
- Generating ids with len(data)+101 can repeat if you ever delete students.

One-line summary to memorize:
"Load JSON -> change dict -> save JSON; routes decide when this happens." 
"""

