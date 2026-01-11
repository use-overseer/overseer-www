# Overseer — Public Website Content

[![Sync to Server](https://github.com/use-overseer/overseer-www/actions/workflows/sync_to_server.yml/badge.svg)](https://github.com/use-overseer/overseer-www/actions/workflows/sync_to_server.yml)

This repository contains the Markdown files used across Overseer's public website.  
Each page is designed to stay simple, clear, and easy to maintain.

All content stored here is synchronized automatically with our storage layer whenever a new release is published.

---

## Workflow

When a release is published, a GitHub Action uploads the updated Markdown files to our object storage.  
The website then renders them dynamically.

---

## Purpose

By keeping content separate from the application code, Overseer remains clean, modular, and easy to evolve.

If you'd like to contribute improvements to these pages, feel free to open a pull request.

---

## Accessing Files (CDN)

All files uploaded to the Object Storage are globally accessible through a CDN.

**Base CDN URL:**

[https://1xg7ah.leapcellobj.com/overseer-www-zc3f-zpkk-ui4kx74n](https://1xg7ah.leapcellobj.com/overseer-www-zc3f-zpkk-ui4kx74n)

### How to Use It

If you upload a file such as:

```

public-content/about.md

```

You can access it directly at:

[https://1xg7ah.leapcellobj.com/overseer-www-zc3f-zpkk-ui4kx74n/about.md](https://1xg7ah.leapcellobj.com/overseer-www-zc3f-zpkk-ui4kx74n/about.md)


This allows you to integrate the content anywhere on the site or consume it from other services.

