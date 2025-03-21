# Show system's date and time for each event

**Technical Name:** ShowSystemTime

**Category:** Audit

**Default Value:**

**Impact Level:** Medium

**Description:**

Enables the display of the system's local date and time for each event within the Pathlock GRC platform’s reporting features. This setting is crucial for accurate event logging and audit trails.

**Business Impact:**

Including the system's date and time for each event enhances the traceability and accountability of actions within the system. It aids in compliance audits by providing precise timestamps, thus facilitating the reconstruction of events for investigative purposes. This feature is particularly beneficial for organizations that need to adhere to strict regulatory standards.

**Technical Impact when configured:**

Upon enabling, all reports that detail events will include the local system's date and time for when each event occurred. This detail adds a layer of transparency and makes logs more informative for audit and review processes.

**Examples Scenario:**

A compliance officer needs to investigate an anomaly reported in a security audit. By having the system's date and time displayed for each event, they can quickly pinpoint when the irregularity occurred, aiding in a faster resolution.

**Related Settings:**

- ShowOnlyEndUsers
- ShowPortalLinkOnRequestSubmittedPage
- ShowRoleTypeColumnInReports

**Best Practices:** 

- Configure when: Detailed audit trails are necessary for compliance or investigation purposes.
- Avoid when: The inclusion of timestamps may clutter reports or where such detail is not necessary for casual review or analysis.