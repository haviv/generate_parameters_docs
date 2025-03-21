**Send Mail Excluded Domains**

**Technical Name:** SendMailExcludedDomains

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The SendMailExcludedDomains parameter is designed to specify which email domains should be excluded from receiving automated emails sent by the Pathlock GRC platform. This setting is particularly useful for organizations looking to prevent sending notifications, alerts, or any automated communication to certain domains, which may include external consultants, temporary workers, or domains associated with high-risk or non-compliant entities.

**Business Impact:**

Configuring the SendMailExcludedDomains parameter allows organizations to maintain control over the dissemination of sensitive information, reduce the risk of unintentional data exposure to untrusted domains, and ensure that compliance requirements related to communication are met. It aids in securing the communication flow and upholding data governance standards.

**Technical Impact when configured:**

When configured, this parameter actively filters out recipients belonging to the specified email domains from the list of email addresses scheduled to receive messages from the Pathlock platform. It ensures that no automated emails, whether they are part of compliance notifications, security alerts, or regular updates, are sent to these excluded domains.

**Example Scenario:**

An organization may decide to exclude external contractor domains from receiving automated security alerts and compliance notifications to ensure that only internal staff members or trusted domains are informed. By setting SendMailExcludedDomains to include "contractor.com", the platform will automatically omit any recipients with that domain from its email dispatches.

**Related Settings:**

- SendMailOnlyToSpecificAddresses

**Best Practices:** 

- Configure when you have specific domains that should not receive communications from the Pathlock platform to maintain security and compliance postures.
- Avoid when there is a need for wide dissemination of information across varied domains without restrictions.