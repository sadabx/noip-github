# No-IP Toolkit: Hosting & Auto-Renewal

![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Automation-blue?style=for-the-badge&logo=github-actions)
![No-IP](https://img.shields.io/badge/No--IP-Dynamic_DNS-orange?style=for-the-badge&logo=rss)

**A complete solution for No-IP users.**
This repository serves two purposes:
1.  📘 **Documentation:** A step-by-step guide to connecting No-IP domains to GitHub Pages.
2.  🤖 **Automation:** A script to automatically renew free No-IP hosts so they don't expire.

---

## 📚 Part 1: Connect No-IP to GitHub Pages
> *Follow these steps to use your free `ddns.net` domain as a custom URL for your GitHub site.*

### 1️⃣ Set Up Your Repository
* Create a new repository (or use this one).
* Go to **Settings** > **Pages**.
* Select the branch you want to publish (e.g., `main`) and click **Save**.

### 2️⃣ Configure No-IP DNS
* Log in to [No-IP.com](https://www.noip.com/login).
* Go to **My Services** > **DNS Records**.
* Create a **CNAME Record** for your domain (e.g., `sadab.ddns.net`) pointing to `sadabx.github.io`.

### 3️⃣ Add CNAME File
* Create a file named `CNAME` (all caps, no extension) in your repository root.
* Inside, write **only** your domain name:
  ```text
  sadab.ddns.net
  ```

### 4️⃣ Verify in GitHub
* Go back to **Settings** > **Pages**.
* In the **Custom domain** box, enter your domain and click **Save**.
* Check the **Enforce HTTPS** box once it becomes available (can take up to 24h).

---

## 🤖 Part 2: Auto-Renewer Bot
> *Free No-IP domains expire every 30 days unless you confirm them. This bot does it for you.*

### 📂 Files Required
Ensure your repository contains these files (found in this repo):
* `renew.py` (The script)
* `requirements.txt` (Dependencies)
* `.github/workflows/schedule.yml` (The schedule)

### ⚙️ Setup Instructions

#### Step 1: Get Your Login Cookie
Since No-IP checks for bots, we use a session cookie to bypass the login screen.
1. Log in to [No-IP.com](https://www.noip.com/login) on your browser and check **"Keep me logged in"**.
2. Open Developer Tools (`F12`) > **Application** tab > **Cookies**.
3. Find the cookie named `nexus_session` (or `session`).
4. Copy its **Value** (a long string of random characters).

#### Step 2: Add GitHub Secrets
To keep your credentials safe, do not save them in code.
1. Go to **Settings** > **Secrets and variables** > **Actions**.
2. Click **New repository secret**.
3. Create a secret named `NOIP_COOKIE` and paste your cookie value.

#### Step 3: Enable the Workflow
1. Go to the **Actions** tab.
2. Select **No-IP Auto Renew** on the left.
3. Click **Run workflow** to test it immediately.

---

## 📂 Repository Structure

| File | Description |
| :--- | :--- |
| `index.html` | The landing page tutorial website. |
| `renew.py` | The Python script that performs the renewal. |
| `.github/workflows/` | Contains the automation schedule. |
| `CNAME` | Config file linking the custom domain. |

---

## ⚠️ Disclaimer
This project is for educational purposes. Please use responsibly and ensure you comply with No-IP's Terms of Service.
