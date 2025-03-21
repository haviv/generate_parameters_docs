# Do Not Mail Business Process Schedule Report

**Technical Name:** DoNotMailBusinessProcessScheduleReport

**Category:** Reporting

**Default Value:** 

**Impact Level:** Medium

**Description:** The `DoNotMailBusinessProcessScheduleReport` parameter controls whether a scheduled report about business process schedules is emailed out or not. When enabled, it prevents the auto-generation and mailing of error logs or reports related to scheduling failures or issues within business processes, ensuring sensitive data is not unintentionally distributed via email.

**Business Impact:** Enabling this setting enhances data privacy and security by ensuring that detailed error reports, which may contain sensitive business process information, are not disseminated through email. It's particularly relevant for organizations aiming to tighten their data security measures and mitigate the risk of unintentional data exposure.

**Technical Impact when configured:** When this parameter is configured to withhold mailing, any errors or failures in scheduling business process reports are not emailed but may be logged or stored in another specified manner. This configuration helps in controlling the flow of potentially sensitive information outside the organization's secure environment.

**Examples Scenario:** If a business process related to financial reporting fails to execute its scheduled task, instead of sending an email with a detailed error log (which may contain sensitive financial data or insights into the system's structure), the system will refrain from distributing this information via email, adhering to the organization's data security protocols.

**Related Settings:** 

**Best Practices:** configure when sensitive information is involved in business processes to prevent data leakage via email, avoid when immediate email alerts are critical for business process monitoring and issue resolution.