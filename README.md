# Connect No-IP Domain to GitHub Pages

![No-IP](https://img.shields.io/badge/No--IP-Dynamic_DNS-orange?style=flat-square&logo=rss)
![GitHub Pages](https://img.shields.io/badge/Hosting-GitHub_Pages-blue?style=flat-square&logo=github)
![Guide](https://img.shields.io/badge/Type-Tutorial-green?style=flat-square)

> A step-by-step tutorial showing you how to use your No-IP dynamic DNS domain with GitHub Pages for free hosting.

---

## 📖 Overview
This guide explains how to connect a free hostname (e.g., `my-site.ddns.net`) from **No-IP** to a static website hosted on **GitHub Pages**.

[**▶️ Watch the Video Tutorial**](https://www.youtube.com/embed/g1bgefvaXjQ)

---

## 🚀 Setup Guide

### 1️⃣ Set Up Your GitHub Pages Repository
* Create a new repository on GitHub or use an existing one.
* Go to **Settings** > **Pages**.
* Enable GitHub Pages and choose your publishing source (e.g., `main` branch).

### 2️⃣ Configure Your No-IP Domain
* Log in to your **[No-IP Account](https://www.noip.com/login)**.
* Navigate to the **DNS Management** section.
* Update your DNS records (A Records or CNAME) to point to GitHub's servers.

### 3️⃣ Add CNAME File to Your Repository
* Create a new file named `CNAME` in the root of your repository.
* **Important:** Do not add a file extension (like .txt).
* Add your No-IP domain name as the only content inside the file (e.g., `example.ddns.net`).

### 4️⃣ Update GitHub Pages Settings
* Return to your repository **Settings** > **Pages**.
* Under the **Custom domain** field, type your No-IP domain.
* Click **Save**.

### 5️⃣ Wait for DNS Propagation
* DNS changes can take anywhere from a few minutes up to **24 hours** to propagate globally.
* Be patient if the site doesn't load immediately.

### 6️⃣ Test Your Configuration
* Once propagation is complete, visit your No-IP domain in a browser.
* Verify that your GitHub Pages site loads correctly.

---

## 🛠️ Troubleshooting
* **HTTPS Error?** It may take some time for GitHub to generate a certificate. Once available, check "Enforce HTTPS" in settings.
* **404 Error?** Ensure your `CNAME` file is in the *root* directory, not a subfolder.

---

<div align="center">
  <sub>This guide is for educational purposes.</sub>
</div>
