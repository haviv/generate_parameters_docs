# Product Key Expiration Warning Days

**Technical Name:** ProductKeyExperisionWarningDays

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls the number of days in advance users are warned about the impending expiration of the product key. Ensuring users are informed ahead of time allows for necessary preparations and renewals, avoiding any interruptions in service.

**Business Impact:**

The setting of this parameter directly impacts the operational continuity of the Pathlock Cloud GRC platform. Adequate warning ensures that all compliance, risk management, and security operations continue without disruption due to an expired product key.

**Technical Impact when configured:**

When this parameter is configured, the system begins to send out warning notifications to users via email this many days before the product key is set to expire. This aids in proactive renewal processes and prevents potential access issues or functionality limitations within the Pathlock platform.

**Examples Scenario:**

- Scenario: A company has set the `ProductKeyExperisionWarningDays` to 30 days. One month before the product key expires, all relevant stakeholders receive an email notification, reminding them to renew their product key. This advanced notice ensures that there is ample time to process the renewal without affecting the company's GRC processes.

**Related Settings:**

- `Portal_ShowProductHeader`
- `PowerShellExePath`

**Best Practices:** 

- **Configure when:** You want to ensure there's adequate lead time for product key renewal processes, allowing for uninterrupted use of the Pathlock platform.
- **Avoid when:** If the organization has an automated renewal process or does not require advanced notice for license renewals, setting this parameter might be unnecessary but consider keeping a minimal value to serve as an additional safeguard.
