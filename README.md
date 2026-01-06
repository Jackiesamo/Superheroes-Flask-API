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
