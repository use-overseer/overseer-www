# Overseer — Public Website Content

[![Sync Markdown to Server](https://github.com/use-overseer/overseer-www/actions/workflows/sync_to_server.yml/badge.svg)](https://github.com/use-overseer/overseer-www/actions/workflows/sync_to_server.yml)

This repository contains the Markdown files used across Overseer's public website.  
Each page is designed to stay simple, clear, and easy to maintain.

All content stored here is synchronized automatically with our storage layer whenever a new release is published.

---

## Structure

The repository includes the public pages of the site:

- About  
- Donate  
- Contact  
- Compare  
- Legal Notice  
- Privacy  
- Terms  

All files are written in Markdown for clarity and version control.

---

## Workflow

When a release is published, a GitHub Action uploads the updated Markdown files to our object storage.  
The website then renders them dynamically.

---

## Purpose

By keeping content separate from the application code, Overseer remains clean, modular, and easy to evolve.

If you'd like to contribute improvements to these pages, feel free to open a pull request.
