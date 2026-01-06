# Superheroes Flask API

A RESTful API for tracking superheroes and their superpowers.  
This API allows you to view heroes, their powers, and assign powers to heroes with strength levels.

---

## Author

**Jacklyne Owuor**

---

## Features / Routes

### Heroes
- `GET /heroes`  
  Returns a list of all heroes.

- `GET /heroes/<id>`  
  Returns a single hero by ID, including nested hero powers.  
  **404** returned if hero does not exist.

### Powers
- `GET /powers`  
  Returns a list of all powers.

- `GET /powers/<id>`  
  Returns a single power by ID.  
  **404** returned if power does not exist.

- `PATCH /powers/<id>`  
  Updates the description of a power.  
  Validations:
  - Description is required
  - Minimum 20 characters  
  Returns **400** if validation fails, **404** if power does not exist.

### Hero Powers
- `POST /hero_powers`  
  Assigns a power to a hero with a strength level.  
  Validations:
  - Strength must be `'Strong'`, `'Weak'`, or `'Average'`
  - Hero and Power must exist  
  Returns **400** if validation fails, **201** on success.

---

## Setup Instructions

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd Superheroes-Flask-API
start flask server<flask run>

            MIT License

Copyright (c) 2026 Jacklyne Owuor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.



