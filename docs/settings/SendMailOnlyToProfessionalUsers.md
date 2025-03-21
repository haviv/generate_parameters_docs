# Send Mail Only To Professional Users

**Technical Name:** SendMailOnlyToProfessionalUsers

**Category:** User Management

**Default Value:** ""

**Impact Level:** Medium

**Description:**

This setting controls the behavior of the email sending functionality within the Pathlock Cloud GRC platform, specifically limiting the sending of emails to only those recipients classified as "professional users." A professional user, in this context, is determined by the organization's internal criteria, which might include specific roles, responsibilities, or attributes defining a professional status within the system.

**Business Impact:**

Implementing this parameter helps ensure that critical and sensitive information circulated via email is received only by intended and appropriately classified recipients. It aids in compliance by preventing accidental or unauthorized disclosure of information to non-professional or unintended users, thereby minimizing risk.

**Technical Impact when configured:**

- Ensures email notifications and communications are sent exclusively to users deemed professional, based on the organization’s criteria.
- Helps in maintaining the confidentiality and integrity of the information being shared via email.
- Reinforces compliance with internal policies and potentially with external regulatory requirements concerning information dissemination.

**Examples Scenario:**

An organization needs to send out a financial report email to its employees. However, due to the sensitive nature of the report, it's vital that only authorized personnel with the "professional" classification receive this email. By enabling and appropriately configuring the `SendMailOnlyToProfessionalUsers` setting, the organization can ensure that the email is only dispatched to those who meet the defined criteria, thus safeguarding sensitive information.

**Related Settings:**

- SendMailOnlyToSpecificAddresses

**Best Practices:** 

- **Configure when:** It is essential to restrict email communication to users within specific roles or classifications to protect sensitive data and comply with internal or external regulatory policies.
- **Avoid when:** Broad communication is necessary, and there is no risk of sensitive information being leaked, or when the professional user criteria are so restrictive that it impedes necessary communication within the organization.