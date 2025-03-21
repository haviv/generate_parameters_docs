# Events Summary Mail - Header

**Technical Name:** DailyEmailHeader

**Category:** Reporting

**Default Value:** (Not provided in the code references)

**Impact Level:** Medium

**Description:** This parameter configures the header content of the daily summary email reports sent by the Pathlock Cloud GRC platform. It allows for the customization of email reports to include specific header information, enhancing readability and relevance for recipients.

**Business Impact:** Effective use of the DailyEmailHeader parameter ensures that recipients of the daily summary emails can quickly identify the emails' purpose and context, facilitating better communication and awareness of security, risk, and compliance events within the organization.

**Technical Impact when configured:** When the DailyEmailHeader is properly configured, it ensures that each email sent has a consistent and identifiable header, which can include important details such as the reporting period, the specific system reporting, and the user for whom the events are being reported. This leads to an improved user experience and ensures that the critical information is noticed and can be acted upon more efficiently.

**Example Scenario:**
- Scenario: An organization wants to make the daily summary emails instantly recognizable to its IT security team. By configuring the DailyEmailHeader to include "[IT Security Events Summary]" at the beginning of each email subject line, team members can quickly identify and prioritize these emails in their inboxes.

**Related Settings:**
- DailyEmailConfig
- DailyEmailFooter

**Best Practices:** 
- Configure when: You want to ensure clarity and quick identification of daily summary email reports for specific groups within the organization.
- Avoid when: The default email header settings are sufficient for your organizational needs or if changes may confuse the report recipients.