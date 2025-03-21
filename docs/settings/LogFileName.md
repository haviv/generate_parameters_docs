# Log File Name

**Technical Name:** LogFileName

**Category:** Configuration

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

The LogFileName parameter specifies the name of the file where logs from the Pathlock Cloud GRC platform's logging system, specifically within the Xpandion ProfileTailor Client, are stored. This setting influences how log files are generated, named, and organized, facilitating easier access and analysis of log data for troubleshooting, auditing, and compliance purposes.

**Business Impact:**

Selecting an appropriate log file name and location ensures that system administrators and compliance officers can quickly locate and analyze the log files for security incidents, system errors, user activities, and compliance with internal and external regulations. It supports operational integrity and regulatory compliance by enabling efficient log management practices.

**Technical Impact when configured:**

- Organized and consistent logging, easing the process of monitoring and managing system activities.
- Improved auditability of the system by providing clear, accessible logs for review.
- Eases integration with log analysis tools and SIEM systems by adhering to expected logging formats and conventions.

**Examples Scenario:**

For a financial institution using the Pathlock Cloud GRC platform, setting the LogFileName to "FinancialSystemAudit.log" enables IT security and compliance teams to quickly identify and access logs relevant to auditing financial transactions and ensuring compliance with financial regulations.

**Related Settings:** UserModernLogger

**Best Practices:** 

- **Configure when:**
  - Setting up the system for the first time to ensure logs are correctly named and stored from the outset.
  - Changing logging strategies or implementing new compliance requirements that necessitate a different log file naming convention.
- **Avoid when:**
  - Log file names are set to be overly generic or confusing, leading to difficulty in distinguishing log files.
  - Sensitive information might be inferred from the log file name, potentially leading to security risks.