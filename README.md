# Phishing-Email-Analysis-Lab
This repository documents my analysis of a phishing email as part of a cybersecurity lab exercise. The goal was to identify and extract threat indicators, analyze email metadata, investigate the linked URL, and observe web behavior using dynamic analysis tools like ANY.RUN.
🛡️ Phishing Email Analysis Lab

🔍 Email Analysis Summary
Detail	Value
Recipient	kinnar1975@yahoo.co.uk
Subject	Undeliverable: Website contact form submission
Date Sent	18 March 2021, 04:14
Originating IP	103.9.171.10
Reverse DNS	c5s2–1e-syd.hosting-services.net.au
Attachment Name	Website contact form submission.eml
URL in Attachment	https://35000usdperwwekpodf.blogspot.sg?p=9swg...
Hosting Platform	Blogspot
Heading Text (via URL2PNG)	Blog has been removed

🧪 Dynamic Analysis with ANY.RUN
Tool Used: ANY.RUN – interactive malware analysis sandbox

Purpose: To observe any redirects, scripts, or network behavior of the embedded URL

Result: The blog page had been taken down, but metadata and initial behavior were captured for documentation.

⚠️ Key Takeaways
Phishing emails often disguise links behind legitimate-looking domains (e.g., Blogspot).

Headers and originating IPs offer critical leads for tracing the source.

Sandbox tools like ANY.RUN enable safe exploration of malicious web content.

Even removed or inactive content can reveal IOCs useful for defense and alerting.

🧰 Tools Used
ANY.RUN

URL2PNG

WHOIS / DomainTools

Manual EML file inspection

📁 Files
email-analysis-notes.md – Breakdown of each question and answer

screenshots/ – Header details, ANY.RUN snapshots

Website contact form submission.eml – Sample phishing email (sanitized)
