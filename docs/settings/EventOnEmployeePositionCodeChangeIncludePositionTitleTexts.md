**Event On Employee Position Code Change Include Position Title Texts**

**Technical Name:** EventOnEmployeePositionCodeChangeIncludePositionTitleTexts

**Category:** Configuration

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:** This setting controls whether the position title texts are included in events triggered by changes in an employee's position code. If enabled, any change in the employee's position code or job title leads to the addition of the position title texts in the event details.

**Business Impact:** Enables organizations to closely monitor and audit changes in employee positions and job titles, ensuring a higher level of detail in change records. This is crucial for maintaining accurate and comprehensive audit trails, necessary for compliance with internal policies and external regulations.

**Technical Impact when configured:** When this parameter is configured to include position title texts, it enhances the auditing capabilities by providing an additional layer of detail. This facilitates better tracking of position and role changes within the organization, which is vital for security, compliance, and operational integrity.

**Example Scenario:** An HR manager modifies an employee's job title in the company's HR system from "Junior Analyst" to "Senior Analyst". With EventOnEmployeePositionCodeChangeIncludePositionTitleTexts enabled, the change event recorded not only captures the change in job code but also includes the old and new job titles, providing a complete before-and-after snapshot of the change.

**Related Settings:** Not explicitly mentioned in the provided code references.

**Best Practices:** 
- **Configure when** tracking detailed information about position and title changes is crucial for your organization's operational, compliance, or security policies.
- **Avoid when** such detailed tracking is unnecessary, as it may lead to information overload or unnecessary storage use.