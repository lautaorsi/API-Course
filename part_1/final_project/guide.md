# TechConnect Ltd. — Project Specification

> This document defines what the system needs to do, the data it works with, and what "done" looks like. How you build it is entirely up to you.

---

## The Setting

**TechConnect Ltd.** manages a unified digital platform for the city of **Riverside**. The platform serves two purposes:

1. **City Services** — keeping track of public resources across the city so residents and staff always have accurate, up-to-date information
2. **Online Bookstore** — running a catalog and order system for a city-affiliated bookstore

Riverside has 5 districts: Downtown, Northside, Eastside, Westside, and Southside. The city operates libraries, parks, clinics, and recreation centers across all of them.

---

## Your Datasets

| File | What it contains |
|---|---|
| `books.csv` | The bookstore's catalog — 20 books with pricing, stock levels, and metadata |
| `city_services.csv` | 18 city services across all categories and districts |

Load these into a database as your starting data.

---

## What the System Needs to Do

### City Services

Staff need to be able to:
- See a list of all city services
- Look up a specific service by its ID
- Add a new service to the system
- Update any details of an existing service
- Make a quick update to just a service's current occupancy or open/closed status without touching anything else
- Remove a service from the system

Residents and staff should also be able to narrow down the list by filtering services by type (library, park, clinic, recreation), by district, by whether they're currently open, and by whether they're wheelchair accessible.

---

### Books

Staff need to be able to:
- Browse the full book catalog
- Look up a specific book
- Add new books to the catalog
- Update a book's details
- Quickly adjust just a book's price or stock quantity
- Remove a book from the catalog

Shoppers should be able to filter books by genre, author, price range, and whether a book is currently in stock. Results should be sortable and paginated.

The system must prevent two books from sharing the same ISBN.

---


### Real-Time Service Updates

The system should be able to push live updates to anyone who is watching, without them needing to manually refresh. These updates should fire whenever a service's status or occupancy changes.

The `service_events.csv` file represents a sample of what a day's worth of these updates looks like — use it to simulate a live feed.

Watchers should be able to choose to only receive updates for a specific service category rather than everything at once.

---

### Flexible Data Querying

Beyond the standard ways of fetching data, the system should support a more flexible querying interface where clients can ask for exactly the fields they want and combine data across resources in a single request — for example, fetching a list of books alongside a list of open clinics in one go, rather than making two separate calls.

---

## Performance Requirements

The system should not make clients wait unnecessarily. Specifically:

- Responses that haven't changed since the last time a client asked should not waste bandwidth re-sending the same data
- Clients should be able to ask "has this changed since I last checked?" and get a lightweight confirmation if it hasn't
- Frequently-requested lists can be considered stable enough to cache briefly; individual records should be cached a bit longer

---

## Documentation

Any developer who picks up this project should be able to understand how to use it without asking anyone. That means:

- Every available operation must be documented with what it expects as input and what it returns
- There should be concrete examples showing how to actually make a request and what a response looks like
- Error cases should be documented, not just the happy path
- Setup instructions should be clear enough that someone can run the project locally from scratch

---

## Testing

The system should have automated tests so that bugs don't slip through unnoticed. The following scenarios must all be covered:

- Placing an order correctly reduces a book's stock
- Trying to order more books than are in stock is rejected
- Cancelling an order correctly restores the stock
- Looking up a service or book that doesn't exist returns a clear "not found" response
- Trying to add a book with a duplicate ISBN is rejected
- Pagination returns the right number of results
- Filtering by category or district returns only the matching records

There should also be end-to-end test flows, for example:
- The full lifecycle of a book order from placement through to cancellation, verifying stock at each step
- Requesting the same resource twice and confirming the second request uses cached data
- Filtering and sorting returning consistent, correct results

---

## Deployment

Releases should not require manual steps. When code is pushed, the system should automatically build, run all tests, and deploy. Deploying to production should only happen intentionally (e.g. when a release is tagged), not on every push.

Sensitive configuration like database credentials should never be hardcoded — they must be injected as environment variables.

---

## Monitoring

The running system should be observable. At minimum:

- Every request should produce a log entry recording what was requested, what happened, and how long it took
- There should be a dedicated check that confirms the system is up and healthy, including whether the database is reachable and how many live connections exist
- Errors should be logged in a way that makes them easy to find and diagnose

---

## Definition of Done

The project is complete when:

- All operations listed above work correctly against the seed data
- Real-time updates are functional and demonstrable
- Flexible querying works for at least books and city services
- All documented test scenarios pass automatically
- A new developer can set up and run the project using only the README
- The deployment pipeline runs without manual intervention

---

*All data in the CSV files is fictional and generated for this portfolio project.*