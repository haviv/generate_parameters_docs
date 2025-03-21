# External email address postfix

**Technical Name:** ExternalStmpDomainPostfix

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:** 

The parameter 'ExternalStmpDomainPostfix' is used to specify a domain postfix for external email addresses that are generated or utilized within the Pathlock Cloud GRC platform. This setting is crucial for configuring the system's ability to send emails outside of the organization's primary domain.

**Business Impact:**

Proper configuration of this parameter has significant implications for communication with external stakeholders, such as partners or consultants, ensuring that automated notifications, alerts, and reports are correctly routed to recipients outside of the organization's primary email domain.

**Technical Impact when configured:**

- Ensures emails sent by the system to external addresses are correctly formatted and deliverable.
- Supports compliance and security protocols by segregating internal from external electronic communications.
- Facilitates accurate and reliable delivery of automated emails to external stakeholders.

**Examples Scenario:**

- **Audit Notifications:** In an audit scenario where findings must be communicated to an external auditor with an email address not hosted on the organization's primary domain. By configuring this parameter, the platform can automatically send formatted emails to the auditor's external domain.

**Related Settings:**

- *EventsDetailsTableText*: This setting relates to the customization of email content, which may include sending summaries to external addresses configured with the ExternalStmpDomainPostfix.

**Best Practices:** 

- **Configure when** setting up the platform for environments where communication with external parties is required via email.
- **Avoid when** there is no business need to send emails to external domains, to eliminate unnecessary exposure or complexity in the system configuration.