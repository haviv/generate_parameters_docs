# Send Mail Only To Specific Addresses

**Technical Name:** SendMailOnlyToSpecificAddresses

**Category:** Configuration

**Default Value:** True

**Impact Level:** Medium

**Description:** This parameter controls whether emails sent from the Pathlock platform are filtered to only include specific recipient addresses, allowing for enhanced control over who receives certain communications.

**Business Impact:** Ensuring that only intended recipients, such as those within specific roles or with specific security clearances, receive sensitive or critical information, helping in maintaining compliance and preventing data leaks.

**Technical Impact when configured:** Limits email notifications from the Pathlock platform to a predefined list of allowed addresses or users. Additionally, it can filter out recipients based on domain, user type, or other criteria to ensure only authorized parties receive the emails.

**Examples Scenario:** In a scenario where a company needs to send out compliance reports to a select group of senior managers without including lower-level staff, this setting would ensure that only the email addresses of those senior managers are included in the distribution list, thus maintaining the confidentiality of the reports.

**Related Settings:** Not applicable

**Best Practices:** 
- **Configure when** you need to restrict the distribution of sensitive emails to a select group of recipients or when operating within a tightly regulated industry where information dissemination is subject to compliance requirements.
- **Avoid when** broader communication is necessary, and there are no concerns regarding the sensitivity of the information being distributed via email.