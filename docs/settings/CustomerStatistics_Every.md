# Customer Statistics Every

**Technical Name:** CustomerStatistics_Every

**Category:** Reporting

**Default Value:**

**Impact Level:** High

**Description:**

The "Customer Statistics Every" parameter is designed to configure the frequency at which customer statistics are gathered and reported in the Pathlock Cloud GRC platform. This involves collecting data across various systems within an organization to compile metrics that are essential for understanding and improving security, risk, and compliance postures.

**Business Impact:**

Proper configuration of this parameter ensures that stakeholders have access to timely and accurate information about their security and compliance status, enabling informed decision-making. Regular updates on customer statistics can highlight potential issues early, allowing for proactive measures to mitigate risk. It also supports compliance efforts by ensuring relevant data is always available for audit purposes.

**Technical Impact when configured:**

When configured, this parameter triggers the gathering of statistical data from configured systems, which is then serialized into XML for storage or reporting purposes. This ensures a centralized overview of critical compliance and security metrics, supporting effective governance and risk management strategies.

**Examples Scenario:**

- **Compliance Auditing:** An organization needs to present compliance reports every quarter. Configuring this parameter to compile statistics in line with these requirements ensures that the necessary data is always ready for review.
- **Security Monitoring:** Setting the parameter to gather data more frequently can help in identifying unusual patterns or potential security breaches, enabling faster response times.

**Related Settings:** POSITION_RolePrefix

**Best Practices:** 

- **Configure when:** 
    - Regular monitoring of compliance and security status is required.
    - Preparing for upcoming audits, to ensure that all necessary data is available and up-to-date.
- **Avoid when:** 
    - Systems are resource-constrained, as the frequent gathering of statistics may impact performance.
