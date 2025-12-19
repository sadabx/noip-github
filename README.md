# No-IP Auto Renewer (GitHub Actions)

![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automated-blue?style=for-the-badge&logo=github-actions)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Automate the 30-day confirmation for free No-IP hostnames using GitHub Actions.**

Free No-IP accounts require you to manually confirm your hostname every 30 days to keep it active. This repository contains a script and a GitHub Actions workflow that automatically logs in and confirms your hosts for you, so you never lose your domain.

---

## 🚀 Features
- **Zero Maintenance**: Runs automatically on a schedule (e.g., every 2 weeks).
- **Serverless**: Uses GitHub Actions, so you don't need a Raspberry Pi or always-on server.
- **Secure**: Credentials are stored in GitHub Secrets, never in the code.
- **Notifications**: (Optional) Can be configured to notify you on failure.

---

## 🛠️ Setup Guide

### 1. Fork or Import this Repository
If you haven't already, fork this repository to your own GitHub account or push this code to your private repo.

### 2. Configure Secrets
To keep your No-IP login details safe, do **not** put them in the code. Use GitHub Secrets:

1. Go to your repository **Settings** > **Secrets and variables** > **Actions**.
2. Click **New repository secret**.
3. Add the following secrets:

| Secret Name | Value |
| :--- | :--- |
| `NOIP_USERNAME` | Your No-IP Username or Email |
| `NOIP_PASSWORD` | Your No-IP Password |

### 3. Enable GitHub Actions
1. Go to the **Actions** tab in your repository.
2. If prompted, click **"I understand my workflows, go ahead and enable them"**.
3. Ensure the `noip-renew.yml` (or similar) workflow is present and active.

---

## ⏳ Scheduling
The workflow is configured to run automatically using a cron schedule.
By default, it runs **every 15 days** to ensure the 30-day limit is never reached.

You can modify the schedule in `.github/workflows/main.yml`:
```yaml
on:
  schedule:
    - cron: '0 0 */15 * *' # Runs at 00:00 every 15th day
  workflow_dispatch:       # Allows manual triggering
